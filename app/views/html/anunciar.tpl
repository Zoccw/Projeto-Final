<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="static/img/favicon.ico" />
    <title>Criar Anúncio</title>
</head>
<body>
    % if transfered:
        <h1>Seja bem-vindo ao BMVC! (Bottle Powered)</h1>
        <h4>Cadastre o seu anúncio:</h4>
            <form action="/anunciar" method="post">
            <label for="titulo">Título:</label>
            <input id="titulo" name="titulo" type="text" required /><br>
            <label for="descricao">Descrição:</label>
            <input id="descricao" name="descricao" type="text" /><br>
            <label for="preco">Preço:</label>
            <input id="preco" name="preco" type="number" /><br>
            </br>
            <div class= "button-container">
                <input value="Criar" type="submit" />
            </div>
            </form>
            <form action="/portal" method="post">
            <button type="submit">Portal</button>
            </form>
    % else:
        <h1>Página reservada!</h1>
        <h3>Realize seu LOGIN em nosso portal</h3>
        <form action="/portal" method="get">
          <button type="submit">Portal</button>
        </form>
    % end
</body>
</html>