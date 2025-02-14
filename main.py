import uuid
#################################################################################################
class usuario:
    def __init__(self, nome, email, telefone):
        self.__id = uuid.uuid4()
        self.nome = nome 
        self.email = email
        self.telefone = telefone
        self.avaliacao = 5.0
        self.notas = []
        self.comentarios = []
        #Iniciar anuncio 
        self.anuncio = anuncio()
        
    def get_id(self):
        return self.__id
    
    def atualizar_perfil(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def calcular_avaliacao_media(self):
        if self.notas:
            self.avaliacao = sum(self.notas) / len(self.notas)
        else:
            self.avaliacao = 5.0 
    
    #métodos da classe anuncio
    def criar_anuncio(self, nome, descricao, preco, estado, categoria, fotos):
        return self.anuncio.criar_anuncio(nome, descricao, preco, estado, categoria, fotos)
    
    def ver_anuncio(self):
        return self.anuncio.ver_anuncio()
    
    def editar_anuncio(self, anuncio_nome, **kwargs):
        return self.anuncio.editar_anuncio(anuncio_nome, **kwargs)
    
    def remover_anuncio(self, anuncio_nome):
        return self.anuncio.remover_anuncio(anuncio_nome)
#################################################################################################
#################################################################################################
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
#################################################################################################
class produto:
    def __init__(self, nome, descricao, preco, estado, categoria, fotos):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estado = estado
        self.categoria = categoria
        self.fotos = fotos   
##Criar método para fazer perguntas
##Criar método para adicionar produto aos favoritos
##Criar método para confirmar recebimento e registrar em historico de compras e historico de vendas
##Passar avaliação da classe usuario para a classe comprador
#################################################################################################
class anuncio:
    def __init__(self):
        self.itens_anunciados = []
        
    def criar_anuncio(self, nome, descricao, preco, estado, categoria, fotos):
        anuncio = produto(nome = nome, descricao = descricao, preco = preco, estado = estado, categoria = categoria, fotos = fotos)
        self.itens_anunciados.append(anuncio)
    
    def ver_anuncio(self):
        if not self.itens_anunciados:
            print("Nenhum anúncio disponível.")
            return
        for item in self.itens_anunciados:
            print(f"Produto: {item.nome}, Preço: {item.preco}, Descrição: {item.descricao}, Categoria: {item.categoria}, Estado: {item.estado}")
    
    def editar_anuncio(self, anuncio_nome, **kwargs):
        for anuncio in self.itens_anunciados:
            if anuncio.nome == anuncio_nome:
                for key, value in kwargs.items():
                    if hasattr(anuncio, key):
                        setattr(anuncio, key, value)

    def remover_anuncio(self, anuncio_nome):
        for anuncio in self.itens_anunciados:
            if anuncio.nome == anuncio_nome:
                self.itens_anunciados.remove(anuncio)
#################################################################################################
##Criar método para adicionar produto a venda
##Criar método para remover produto da venda
##Criar método para registrar envio
usuario1 = usuario("João", "joaonaruto@gmail.com", "999999999")

usuario1.criar_anuncio("MacBook Pro 2019", "MacBook em ótimo estado", 5000, "novo", "eletrônicos", ["foto1", "foto2", "foto3"])
usuario1.criar_anuncio("controle", "para controlar", 50, "usado", "eletronicos", ["foto1", "foto2", "foto3"])
usuario1.ver_anuncio()
usuario1.remover_anuncio("controle")
usuario1.ver_anuncio()
