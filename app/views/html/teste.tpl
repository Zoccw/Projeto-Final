<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Testes</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma página de testes.</p>

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