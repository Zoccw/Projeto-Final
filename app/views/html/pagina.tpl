<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha segunda página com o BMVC</title>
        <style>
        /* Reset básico para garantir consistência entre navegadores */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: #4CAF50;
            margin-bottom: 30px;
        }

        h2 {
            color: #333;
            font-size: 1.2em;
            margin-bottom: 10px;
        }

        div {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            max-width: 500px;
            margin: 0 auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        p {
            font-size: 1em;
            line-height: 1.5;
            margin-bottom: 10px;
        }

        h2 {
            text-align: center;
            font-size: 1.2em;
            color: #FF6347;
            margin-top: 50px;
        }

        body {
            background-color: #e9f1f5;
        }
    </style>
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
