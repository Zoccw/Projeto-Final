<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/anunciarCriar.css">
    <title>Criar Anúncio</title>
</head>
<body>
        <h1>Cadastre o seu anúncio:</h1>
        <form action="/pagina" method="get">
            <button type="submit">Página Principal</button>
        </form>
        <form action="/anunciar/criar" method="post" enctype="multipart/form-data">
            <div>
                <label for="titulo">Título:</label>
                <input id="titulo" name="titulo" type="text" required />
            </div>
            
            <div>
                <label for="descricao">Descrição:</label>
                <input id="descricao" name="descricao" type="text" />
            </div>
            
            <div>
                <label for="preco">Preço:</label>
                <input id="preco" name="preco" type="number" />
            </div>
            
            <div>
                <label for="imagem">Imagem:</label>
                <input type="file" id="imagem" name="imagem" accept="image/*">
            </div>
            
            <div class="button-container">
                <button value="Criar" type="submit">Criar</button>
            </div>
        </form>    
        <h3>Seus Anúncios:</h3>
        <div class="anuncio-grid">
            % if anuncios:
                % for anuncio in anuncios:
                    <div class="anuncio-card">
                        % if anuncio.imagem:
                            <img 
                                class="anuncio-image"
                                src="{{ anuncio.imagem }}"
                                alt="{{ anuncio.titulo }}"
                                onerror="this.onerror=null; this.src='/static/img/default.png';"
                            />
                        % end
                        <h3>{{ anuncio.titulo }}</h3>
                        <p>{{ anuncio.descricao }}</p>
                        <p>Preço: R$ {{ anuncio.preco }}</p>
                        <p>Vendedor: {{ anuncio.vendedor }}</p>
                        <p>Data: {{ anuncio.data }}</p>
                    </div>
                % end
            % else:
                <p>Você tem nenhum anúncio cadastrado.</p>
            % end
        </div>
</body>
</html>
