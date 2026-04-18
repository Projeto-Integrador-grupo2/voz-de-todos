// Mensagem simples de debug
console.log("App carregado");

// Exemplo: confirmação ao enviar formulário
document.addEventListener("DOMContentLoaded", () => {
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {
        form.addEventListener("submit", () => {
            console.log("Form enviado");
        });
    });
});

console.log("Rodando...");