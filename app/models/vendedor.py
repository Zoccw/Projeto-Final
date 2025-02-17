from app.models.user_account import *

class vendedor(UserAccount):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.anuncios = []
        self.avaliacao = 5
        