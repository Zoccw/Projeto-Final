document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.anuncio-card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            const id = this.getAttribute('data-id');
            submitAnuncio(id);
        });
    });
});

function submitAnuncio(id) {
    if (confirm('Tem certeza que deseja remover este anúncio?')) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/anunciar/remover';

        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'id';
        input.value = id;

        form.appendChild(input);
        document.body.appendChild(form);
        form.submit();
    }
}