<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal</title>
    <link rel="stylesheet" type="text/css" href="static/css/portal.css">
    <script src="static/js/portal.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        <form action="/portal" method="post" id="loginForm">
            <div class="form-group">
                <label for="username">Nome:</label>
                <input id="username" name="username" type="text" required />
            </div>

            <div class="form-group">
                <label for="password">Senha:</label>
                <input id="password" name="password" type="password" required />
                <!-- Botão para mostrar ou ocultar a senha -->
                <button type="button" id="toggle-password-btn" onclick="togglePassword()">Mostrar Senha</button>
            </div>

            <div class="form-group">
                <input value="Login" type="submit" />
            </div>
        </form>

        <!-- Área para exibir mensagem de erro -->
        <div id="error-message" class="error-message"></div>

        <!-- Formulário de Logout -->
        <form action="/logout" method="post">
            <div class="form-group">
                <button type="submit">Logout</button>
            </div>
        </form>
    </div>
</body>
</html>
