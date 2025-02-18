<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/anunciarRemover.css">
    <title>Remover Anúncios</title>
</head>
<body>
<h1>Seus Anúncios:</h1>
<div class="anuncio-grid">
    % if anuncios:
        % for anuncio in anuncios:
            <div class="anuncio-card" role="button" tabindex="0" data-id="{{anuncio.id_anuncio}}">
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
        </div>
        <div class= "button-container">
            <form action="/anunciar/criar" method="get">
                <button type="submit">Criar Anúncios</button>
            </form>
        </div>
    % end
</div>
<script src="/static/js/anunciarRemover.js"></script>
</body>
</html>