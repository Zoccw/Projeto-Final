import uuid
class usuario:
    def __init__(self, nome, email, telefone):
        self.__id = uuid.uuid4()
        self.nome = nome 
        self.email = email
        self.telefone = telefone
        self.avaliacao = 5.0
        self.notas = []
        self.comentarios = []
        
    def get_id(self):
        return self.__id
    
    def atualizar_perfil(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def calcular_avaliacao_media(self):
        if self.notas:
            self.avaliacao = sum(self.notas) / len(self.notas)
        else:
            self.avaliacao = 5.0 
        
class produto:
    def __init__(self, nome, preco, descricao, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.categoria = categoria
        self.quantidade = quantidade

    def atualizar_produto(self, nome, preco, descricao, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.descricao = descricao
        self.quantidade = quantidade

class avaliacao:
    def __init__(self, avaliador, avaliado, nota, comentario):
        if not self.validar_nota_comentario(nota, comentario):
            return False
        self.avaliador = avaliador
        self.avaliado = avaliado
        self.nota = nota
        self.comentario = comentario
        self.avaliado.notas.append(self.nota)
        self.avaliado.comentarios.append(self.comentario)
        self.avaliado.calcular_avaliacao_media()
        
        
    def validar_nota_comentario(self, nota, comentario):
        if nota < 0 or nota > 5:
            raise ValueError("Nota inválida. A nota deve estar entre 0 e 5.")
        if not comentario:
            raise ValueError("Comentário inválido. O comentário não pode estar vazio.")
        return True

class comprador(usuario):
    def __init__(self):
        self.historico_compras = []
        self.itens_favoritos = []

##Criar método para fazer perguntas
##Criar método para adicionar produto aos favoritos
##Criar método para confirmar recebimento e registrar em historico de compras e historico de vendas
##Passar avaliação da classe usuario para a classe comprador

class vendedor(usuario):
    def __init__(self):
        self.lista_produtos = []
        self.historico_vendas = []

##Criar método para adicionar produto a venda
##Criar método para remover produto da venda
##Criar método para registrar envio
##Criar método para responder perguntas