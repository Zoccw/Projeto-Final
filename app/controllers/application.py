import datetime
import uuid
import socketio
import os
from app.controllers.datarecord import UserRecord, MessageRecord, AnuncioRecord
from bottle import template, redirect, request, response, Bottle, static_file, abort

def login_required(func):
    def wrapper(*args, **kwargs):
        app = request.environ.get('application')
        current_user = app.getCurrentUserBySessionId()
        if not current_user:
            redirect('/portal')
            return
        return func(*args, **kwargs)
    return wrapper

class Application:

    def __init__(self):

        self.pages = {
            'portal': self.portal,
            'pagina': self.pagina,
            'create': self.create,
            'delete': self.delete,
            'chat': self.chat,
            'edit': self.edit,
            'anunciar' : self.anunciar,
            'anunciarCriar' : self.anunciarCriar,
            'anunciarRemover' : self.anunciarRemover,
        }
        self.__users = UserRecord()
        self.__messages = MessageRecord()
        self.__anuncios = AnuncioRecord()

        self.edited = None
        self.removed = None
        self.created= None

        # Initialize Bottle app
        self.app = Bottle()
        self.setup_routes()

        # Initialize Socket.IO server
        self.sio = socketio.Server(async_mode='eventlet')
        self.setup_websocket_events()

        # Create WSGI app
        self.wsgi_app = socketio.WSGIApp(self.sio, self.app)


    # estabelecimento das rotas
    def setup_routes(self):
        
    # Rotas Users------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        @self.app.route('/static/<filepath:path>')
        def serve_static(filepath):
            return static_file(filepath, root='./app/static')

        @self.app.route('/favicon.ico')
        def favicon():
            return static_file('favicon.ico', root='.app/static')

        @self.app.route('/pagina', method='GET')
        @login_required
        def pagina_getter():
            return self.render('pagina')

        @self.app.route('/chat', method='GET')
        @login_required
        def chat_getter():
            return self.render('chat')

        @self.app.route('/')
        @self.app.route('/portal', method='GET')
        def portal_getter():
            return self.render('portal')

        @self.app.route('/edit', method='GET')
        @login_required
        def edit_getter():
            return self.render('edit')
        
        @self.app.route('/portal', method='POST')
        def portal_action():
            username = request.forms.get('username')
            password = request.forms.get('password')
            self.authenticate_user(username, password)

        @self.app.route('/edit', method='POST')
        @login_required
        def edit_action():
            username = request.forms.get('username')
            password = request.forms.get('password')
            print(username + ' sendo atualizado...')
            self.update_user(username, password)
            return self.render('edit')

        @self.app.route('/create', method='GET')
        def create_getter():
            return self.render('create')

        @self.app.route('/create', method='POST')
        def create_action():
            username = request.forms.get('username')
            password = request.forms.get('password')
            self.insert_user(username, password)
            return self.render('portal')
                            
        @self.app.route('/logout', method='POST')
        def logout_action():
            self.logout_user()
            return self.render('portal')

        @self.app.route('/delete', method='GET')
        @login_required
        def delete_getter():
            return self.render('delete')

        @self.app.route('/delete', method='POST')
        @login_required
        def delete_action():
            self.delete_user()
            return self.render('portal')
        
    # Rotas Anunciar---------------------------------------------------------------------------------------------------------------------------------------------------------
        
        @self.app.route('/anunciar', method='GET')
        @login_required
        def anunciar_getter():
            return self.render('anunciar')
        
        @self.app.route('/anunciar/remover', method='GET')
        @login_required
        def anunciarRemover_getter():
            return self.render('anunciarRemover')
        
        @self.app.route('/anunciar/remover', method= 'POST')
        @login_required
        def anunciarRemover_action():
            id = request.forms.get('id')
            self.remove_anuncio(id)
            return self.render('anunciar')
        
        @self.app.route('/anunciar/criar', method='GET')
        @login_required
        def anunciarCriar_getter():
            return self.render('anunciarCriar')
        
        @self.app.route('/anunciar/criar', method='POST')
        @login_required
        def anunciarCriar_action():
            self.acaoAnununcioCriar()
            return self.render('anunciar')


    # método controlador de acesso às páginas:
    def render(self, page, parameter=None):
        content = self.pages.get(page, self.portal)
        if not parameter:
            return content()
        return content(parameter)

    # métodos controladores de páginas
    # Métodos Anunciar--------------------------------------------------------------------------------------------------------------
    def anunciar(self):
        current_user = self.getCurrentUserBySessionId()
        anuncios = self.getAnunciosOnUser()
        if current_user:
            return template('app/views/html/anunciar', anuncios=anuncios)
        return template('app/views/html/anunciar')
    
    def acaoAnununcioCriar(self):
        current_user = self.getCurrentUserBySessionId()
        titulo = request.forms.get('titulo')
        descricao = request.forms.get('descricao')
        preco = request.forms.get('preco')
        imagem = request.files.get('imagem')
        caminho_imagem = None
        if current_user:
            if imagem and imagem.filename:
                file_extension = os.path.splitext(imagem.filename)[1]
                unique_filename = (f"file_{datetime.datetime.now().strftime('%d%m%Y_%H%M%S')}{file_extension}")
                save_dir = "app/static/usersImg"
                save_path = os.path.join(save_dir, unique_filename)
                url_path = f'/static/usersImg/{unique_filename}'
                imagem.save(save_path)
                caminho_imagem = url_path
                self.insert_anuncio(titulo, descricao, preco, caminho_imagem)
            else:
                self.insert_anuncio(titulo, descricao, preco, caminho_imagem)

    def anunciarCriar(self):
        anuncios = self.getAnunciosOnUser()
        return template('app/views/html/anunciarCriar', anuncios=anuncios)
    
    def anunciarRemover(self):
        anuncios = self.getAnunciosOnUser()
        return template('app/views/html/anunciarRemover', anuncios=anuncios)
    
    def remove_anuncio(self, id):
        self.removed = self.__anuncios.removeAnuncio(id)
        redirect('/anunciar')
    
    def getAnunciosOnUser(self):
        current_user = self.getCurrentUserBySessionId()
        anuncios = self.__anuncios.getAnuncios()
        anuncios_current_user = []
        if current_user:
            for anuncio in anuncios:
                if current_user.username == anuncio.vendedor:
                    anuncios_current_user.append(anuncio)
            return anuncios_current_user
        return None
    
    def insert_anuncio(self, titulo, descricao, preco, imagem=None):
        current_user = self.getCurrentUserBySessionId()
        if current_user:
            vendedor = current_user.username
            data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            id = uuid.uuid4()
            self.created = self.__anuncios.book(titulo, descricao, preco, vendedor, data, imagem, str(id))
            redirect('/anunciar')
        redirect('/anunciar')
    
# Métodos User--------------------------------------------------------------------------------------------------------------

    def getAuthenticatedUsers(self):
        return self.__users.getAuthenticatedUsers()

    def getCurrentUserBySessionId(self):
        session_id = request.get_cookie('session_id')
        if not session_id:
            return None
        return self.__users.getCurrentUser(session_id)
    
    def create(self):
        return template('app/views/html/create')

    def delete(self):
        current_user = self.getCurrentUserBySessionId()
        user_accounts= self.__users.getUserAccounts()
        return template('app/views/html/delete', user=current_user, accounts=user_accounts)

    def edit(self):
        current_user = self.getCurrentUserBySessionId()
        user_accounts= self.__users.getUserAccounts()
        return template('app/views/html/edit', user=current_user, accounts= user_accounts)

    def portal(self):
        current_user = self.getCurrentUserBySessionId()
        if current_user:
            portal_render = template('app/views/html/portal', \
            username=current_user.username, edited=self.edited, \
            removed=self.removed, created=self.created)
            self.edited = None
            self.removed= None
            self.created= None
            return portal_render
        portal_render = template('app/views/html/portal', username=None, \
        edited=self.edited, removed=self.removed, created=self.created)
        self.edited = None
        self.removed= None
        self.created= None
        return portal_render

    def pagina(self):
        self.update_users_list()
        current_user = self.getCurrentUserBySessionId()
        if current_user:
            return template('app/views/html/pagina', current_user=current_user)
        return template('app/views/html/pagina')

    def is_authenticated(self, username):
        current_user = self.getCurrentUserBySessionId()
        if current_user:
            return username == current_user.username
        return False

    def authenticate_user(self, username, password):
        session_id = self.__users.checkUser(username, password)
        if session_id:
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            redirect('/pagina')
        redirect('/portal')

    def delete_user(self):
        current_user = self.getCurrentUserBySessionId()
        self.logout_user()
        self.removed= self.__users.removeUser(current_user)
        self.update_account_list()
        print(f'Valor de retorno de self.removed: {self.removed}')
        redirect('/portal')

    def insert_user(self, username, password):
        self.created= self.__users.book(username, password,[])
        print(f"insert_user: self.created = {self.created}")
        self.update_account_list()
        redirect('/portal')

    def update_user(self, username, password):
        self.edited = self.__users.setUser(username, password)
        redirect('/portal')

    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__users.logout(session_id)
        response.delete_cookie('session_id')
        self.update_users_list()
        
    def chat(self):
        current_user = self.getCurrentUserBySessionId()
        if current_user:
            messages = self.__messages.getUsersMessages()
            auth_users= self.__users.getAuthenticatedUsers().values()
            return template('app/views/html/chat', current_user=current_user, \
            messages=messages, auth_users=auth_users)
        redirect('/portal')

    def newMessage(self, message):
        try:
            content = message
            current_user = self.getCurrentUserBySessionId()
            return self.__messages.book(current_user.username, content)
        except UnicodeEncodeError as e:
            print(f"Encoding error: {e}")
            return "An error occurred while processing the message."

    # Websocket:
    def setup_websocket_events(self):

        @self.sio.event
        async def connect(sid, environ):
            print(f'Client connected: {sid}')
            self.sio.emit('connected', {'data': 'Connected'}, room=sid)

        @self.sio.event
        async def disconnect(sid):
            print(f'Client disconnected: {sid}')

        # recebimento de solicitação de cliente para atualização das mensagens
        @self.sio.event
        def message(sid, data):
            objdata = self.newMessage(data)
            self.sio.emit('message', {'content': objdata.content, 'username': objdata.username})

        # solicitação para atualização da lista de usuários conectados. Quem faz
        # esta solicitação é o próprio controlador. Ver update_users_list()
        @self.sio.event
        def update_users_event(sid, data):
            self.sio.emit('update_users_event', {'content': data})

        # solicitação para atualização da lista de usuários conectados. Quem faz
        # esta solicitação é o próprio controlador. Ver update_users_list()
        @self.sio.event
        def update_account_event(sid, data):
            self.sio.emit('update_account_event', {'content': data})

    # este método permite que o controller se comunique diretamente com todos
    # os clientes conectados. Sempre que algum usuários LOGAR ou DESLOGAR
    # este método vai forçar esta atualização em todos os CHATS ativos. Este
    # método é chamado sempre que a rota ''
    def update_users_list(self):
        print('Atualizando a lista de usuários conectados...')
        users = self.__users.getAuthenticatedUsers()
        users_list = [{'username': user.username} for user in users.values()]
        self.sio.emit('update_users_event', {'users': users_list})

    # este método permite que o controller se comunique diretamente com todos
    # os clientes conectados. Sempre que algum usuários se removerem
    # este método vai comunicar todos os Administradores ativos.
    def update_account_list(self):
        print('Atualizando a lista de usuários cadastrados...')
