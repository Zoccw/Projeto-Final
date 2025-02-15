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
                
class produto:
    def __init__(self, nome, descricao, preco, estado, categoria, fotos):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estado = estado
        self.categoria = categoria
        self.fotos = fotos   