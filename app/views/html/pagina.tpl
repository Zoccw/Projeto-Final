<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha segunda página com o BMVC</title>
</head>
<body>

    <h1>Minha página com interação de modelos :)</h1>

    % if current_user:
        <div>
            <h2>Dados do Usuário:</h2>
            <p>Username: {{ current_user.username }} </p>
            <p>Password: {{ current_user.password }} </p>
        </div>
    % else:
        <h2>Por favor faça seu login em /portal </h2>
    % end

</body>
</html>