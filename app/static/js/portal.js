// Função para pegar o valor de um cookie
function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([.$?*|{}()[]\/+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

// Função para mostrar/ocultar a senha
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleButton = document.getElementById('toggle-password-btn');

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.textContent = "Ocultar Senha";
    } else {
        passwordInput.type = "password";
        toggleButton.textContent = "Mostrar Senha";
    }
}

window.onload = function() {
    // Verifica se há um erro no cookie
    var errorMessage = getCookie('auth_error');
    if (errorMessage) {
        // Exibe a mensagem de erro em uma div
        var errorDiv = document.getElementById('error-message');
        errorDiv.textContent = errorMessage;
        errorDiv.style.display = 'block';  // Exibe a div
        // Remove o cookie após mostrar a mensagem
        document.cookie = "auth_error=; Max-Age=0; path=/";
    } else {
        // Caso não haja erro, a mensagem permanece oculta
        var errorDiv = document.getElementById('error-message');
        errorDiv.style.display = 'none';
    }
};
