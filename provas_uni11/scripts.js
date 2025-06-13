document.addEventListener('DOMContentLoaded', () => {
    const cadastroForm = document.getElementById('cadastroForm');
    const listaUsuarios = document.getElementById('listaUsuarios');
    const limparListaBtn = document.getElementById('limparLista');
    // Novo: Seleciona o botão de reset do formulário
    const resetFormularioBtn = document.getElementById('resetFormulario');
    

    // Função para validar campos
    function validarCampo(campo) {
        if (campo.value.trim() === '') {
            console.error(`Erro: O campo ${campo.previousElementSibling.textContent.replace(':', '')} não pode estar vazio.`);
            campo.style.borderColor = 'red'; // Feedback visual
            return false;
        }
        campo.style.borderColor = '#ddd'; // Resetar borda
        return true;
    }

    // Função para resetar as bordas dos campos para o estado padrão
    function resetarBordasCampos() {
        const campos = cadastroForm.querySelectorAll('input');
        campos.forEach(campo => {
            campo.style.borderColor = '#ddd';
        });
    }

    // Atribuir evento de 'submit' ao formulário
    cadastroForm.addEventListener('submit', function(event) {
        // Previne o comportamento padrão (recarregar a página)
        event.preventDefault();

        const nomeUsuarioInput = document.getElementById('nomeUsuario');
        const senhaInput = document.getElementById('senha');
        const telefoneInput = document.getElementById('telefone');
        const dataNascimentoInput = document.getElementById('dataNascimento');
        const emailInput = document.getElementById('email');

        let todosCamposValidos = true;

        // Valida cada campo. Se um falhar, a flag é atualizada.
        if (!validarCampo(nomeUsuarioInput)) todosCamposValidos = false;
        if (!validarCampo(senhaInput)) todosCamposValidos = false;
        if (!validarCampo(telefoneInput)) todosCamposValidos = false;
        if (!validarCampo(dataNascimentoInput)) todosCamposValidos = false;
        if (!validarCampo(emailInput)) todosCamposValidos = false;

        // Se algum campo não for válido, exibe aviso e interrompe o processo
        if (!todosCamposValidos) {
            console.warn("Por favor, preencha todos os campos obrigatórios.");
            return;
        }

        // Se todos os campos forem válidos, adiciona as informações dinamicamente
        const novoUsuarioItem = document.createElement('li');
        novoUsuarioItem.innerHTML = `
            <strong>Nome de Usuário:</strong> ${nomeUsuarioInput.value}<br>
            <strong>Telefone:</strong> ${telefoneInput.value}<br>
            <strong>Data de Nascimento:</strong> ${dataNascimentoInput.value}<br>
            <strong>E-mail:</strong> ${emailInput.value}
        `;
        listaUsuarios.appendChild(novoUsuarioItem);

        // Reseta o formulário e as bordas dos campos após o envio bem-sucedido
        cadastroForm.reset();
        resetarBordasCampos();
    });

    // Evento para o botão "Limpar Lista"
    limparListaBtn.addEventListener('click', function() {
        if (confirm('Tem certeza que deseja limpar a lista de usuários cadastrados?')) {
            listaUsuarios.innerHTML = '';
            console.log("Lista de usuários limpa.");
        }
    });

    // Novo: Evento para o botão "Limpar Formulário"
    resetFormularioBtn.addEventListener('click', function() {
        cadastroForm.reset(); // Usa o método reset() nativo do formulário
        resetarBordasCampos(); // Reseta as cores das bordas
        console.log("Formulário resetado.");
    });
});



