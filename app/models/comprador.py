from app.models.user_account import *
class comprador(UserAccount):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.compras = []
        self.avaliacoes = []