from app.models.user_account import UserAccount, SuperAccount
from app.models.user_message import UserMessage
from app.models.anuncio import Anuncio
from app.models.categoria import categoria
from app.models.comprador import comprador
from app.models.vendedor import vendedor
from app.models.mensagem import mensagem
import json
import uuid


class MessageRecord():
    """Banco de dados JSON para o recurso: Mensagem"""

    def __init__(self):
        self.__user_messages= []
        self.read()


    def read(self):
        try:
            with open("app/controllers/db/user_messages.json", "r") as fjson:
                user_msg = json.load(fjson)
                self.__user_messages = [UserMessage(**msg) for msg in user_msg]
        except FileNotFoundError:
            print('Não existem mensagens registradas!')


    def __write(self):
        try:
            with open("app/controllers/db/user_messages.json", "w") as fjson:
                user_msg = [vars(user_msg) for user_msg in \
                self.__user_messages]
                json.dump(user_msg, fjson)
                print(f'Arquivo gravado com sucesso (Mensagem)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Mensagem)!')


    def book(self,username,content):
        new_msg= UserMessage(username,content)
        self.__user_messages.append(new_msg)
        self.__write()
        return new_msg


    def getUsersMessages(self):
        return self.__user_messages


# ------------------------------------------------------------------------------

class UserRecord():
    """Banco de dados JSON para o recurso: Usuário"""

    def __init__(self):
        self.__allusers= {'user_accounts': [], 'super_accounts': []}
        self.__authenticated_users = {}
        self.read('user_accounts')
        self.read('super_accounts')


    def read(self,database):
        account_class = SuperAccount if (database == 'super_accounts' ) else UserAccount
        try:
            with open(f"app/controllers/db/{database}.json", "r") as fjson:
                user_d = json.load(fjson)
                self.__allusers[database]= [account_class(**data) for data in user_d]
        except FileNotFoundError:
            self.__allusers[database].append(account_class('Guest', '000000'))


    def __write(self,database):
        try:
            with open(f"app/controllers/db/{database}.json", "w") as fjson:
                user_data = [vars(user_account) for user_account in \
                self.__allusers[database]]
                json.dump(user_data, fjson)
                print(f'Arquivo gravado com sucesso (Usuário)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Usuário)!')



    def setUser(self,username,password):
        for account_type in ['user_accounts', 'super_accounts']:
            for user in self.__allusers[account_type]:
                if username == user.username:
                    user.password= password
                    print(f'O usuário {username} foi editado com sucesso.')
                    self.__write(account_type)
                    return username
        print('O método setUser foi chamado, porém sem sucesso.')
        return None


    def removeUser(self, user):
        for account_type in ['user_accounts', 'super_accounts']:
            if user in self.__allusers[account_type]:
                print(f'O usuário {"(super) " if account_type == "super_accounts" else ""}{user.username} foi encontrado no cadastro.')
                self.__allusers[account_type].remove(user)
                print(f'O usuário {"(super) " if account_type == "super_accounts" else ""}{user.username} foi removido do cadastro.')
                self.__write(account_type)
                return user.username
        print(f'O usuário {user.username} não foi identificado!')
        return None


    def book(self, username, password, permissions):
        account_type = 'super_accounts' if permissions else 'user_accounts'
        account_class = SuperAccount if permissions else UserAccount
        new_user = account_class(username, password, permissions) if permissions else account_class(username, password)
        self.__allusers[account_type].append(new_user)
        self.__write(account_type)
        return new_user.username


    def getUserAccounts(self):
        return self.__allusers['user_accounts']


    def getCurrentUser(self,session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id]
        else:
            return None


    def getAuthenticatedUsers(self):
        return self.__authenticated_users


    def checkUser(self, username, password):
        for account_type in ['user_accounts', 'super_accounts']:
            for user in self.__allusers[account_type]:
                if user.username == username and user.password == password:
                    session_id = str(uuid.uuid4())  # Gera um ID de sessão único
                    self.__authenticated_users[session_id] = user
                    return session_id  # Retorna o ID de sessão para o usuário
        return None


    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id] # Remove o usuário logado

# ------------------------------------------------------------------------------

class AnuncioRecord():
    
    def __init__(self):
        self.__storeanuncios = []
        self.read()
    
    def read(self):
        try:
            with open("app/controllers/db/anuncios.json", "r") as fjson:
                anuncios = json.load(fjson)
                self.__storeanuncios = [Anuncio(**anuncio) for anuncio in anuncios]
        except FileNotFoundError:
            print('Não existem anúncios registrados')

    def __write(self):
        try:
            with open("app/controllers/db/anuncios.json", "w") as fjson:
                anuncios = [vars(anuncio) for anuncio in self.__storeanuncios]
                json.dump(anuncios, fjson, indent=4, ensure_ascii=False)
                print('Arquivo gravado com sucesso (Anúncio)!')
        except FileNotFoundError:
            print('O sistema não conseguiu gravar o arquivo (Anúncio)!')

    def book(self, titulo, descricao, preco, vendedor, data, imagem, id_anuncio):
        new_anuncio = Anuncio(titulo, descricao, preco, vendedor, data, imagem, id_anuncio)
        self.__storeanuncios.append(new_anuncio)
        try:
            self.__write()
        except Exception as e:
            print(f"Erro em salvar anuncios.json: {e}")
        return new_anuncio

    def setAnuncio(self, titulo, descricao, preco):
        for anuncio in self.__storeanuncios:
            if titulo == anuncio.titulo:
                anuncio.titulo = titulo
                anuncio.descricao = descricao
                anuncio.preco = preco
                print(f'O Anúncio {anuncio.titulo} foi editado com sucesso.')
                self.__write()
                return anuncio
        print('O método setAnuncio foi chamado, porém sem sucesso.')
        return None
        
    def removeAnuncio(self, anuncio_id):
        for anuncio in self.__storeanuncios:
            if anuncio_id in anuncio.id_anuncio:
                self.__storeanuncios.remove(anuncio)
                print(f'O anúncio {anuncio.titulo} foi removido do cadastro.')
                self.__write()
                return anuncio
            print(f'O Anúncio {anuncio.titulo} não foi identificado!')
        
    def getAnuncios(self):
        return self.__storeanuncios
    
        
    