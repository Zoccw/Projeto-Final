from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request


class Application():

    def __init__(self):

        self.pages = {
            'pagina': self.pagina,
            'portal': self.portal
        }

        self.model= DataRecord()
        self.__current_loginusername= None


    def render(self,page,parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)


    def get_session_id(self):
        return request.get_cookie('session_id')


    def helper(self):
        return template('app/views/html/helper')


    def portal(self):
        return template('app/views/html/portal')


    def pagina(self,username=None):
        if self.is_authenticated(username):
            session_id = self.get_session_id()
            user = self.model.getCurrentUser(session_id)
            return template('app/views/html/pagina', current_user=user)
        else:
            return template('app/views/html/pagina', current_user=None)


    def is_authenticated(self, username):
        session_id = self.get_session_id()
        current_username = self.model.getUserName(session_id)
        return username == current_username


    def authenticate_user(self, username, password):
        session_id = self.model.checkUser(username, password)
        if session_id:
            self.logout_user()
            self.__current_username= self.model.getUserName(session_id)
            return session_id, username
        return None


    def logout_user(self):
        self.__current_username= None
        session_id = self.get_session_id()
        if session_id:
            self.model.logout(session_id)
