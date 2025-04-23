// script.js
document.addEventListener('DOMContentLoaded', () => {
    const novaTarefaInput = document.getElementById('novaTarefa');
    const adicionarBtn = document.getElementById('adicionarBtn');
    const listaDeTarefas = document.getElementById('listaDeTarefas');
    const indiceRemoverInput = document.getElementById('indiceRemover');
    const removerBtn = document.getElementById('removerBtn');
    const indiceConcluirInput = document.getElementById('indiceConcluir');
    const concluirBtn = document.getElementById('concluirBtn');
    const mensagemDiv = document.getElementById('mensagem');

    let tarefas = [];

    function exibirMensagem(mensagem, tipo = 'info') {
        mensagemDiv.textContent = mensagem;
        mensagemDiv.className = `message-area ${tipo}`;
    }

    function renderizarTarefas() {
        listaDeTarefas.innerHTML = '';
        if (tarefas.length === 0) {
            const li = document.createElement('li');
            li.textContent = 'Nenhuma tarefa adicionada ainda.';
            listaDeTarefas.appendChild(li);
            return;
        }
        tarefas.forEach((tarefa, index) => {
            const li = document.createElement('li');
            li.textContent = `${index + 1}. ${tarefa.texto}`;
            if (tarefa.concluida) {
                li.classList.add('completed');
            }
            listaDeTarefas.appendChild(li);
        });
    }

    adicionarBtn.addEventListener('click', () => {
        const novaTarefaTexto = novaTarefaInput.value.trim();
        if (novaTarefaTexto) {
            tarefas.push({ texto: novaTarefaTexto, concluida: false });
            novaTarefaInput.value = '';
            renderizarTarefas();
            exibirMensagem('Tarefa adicionada com sucesso!');
        } else {
            exibirMensagem('Por favor, digite o nome da tarefa.', 'error');
        }
    });

    removerBtn.addEventListener('click', () => {
        const indiceRemover = parseInt(indiceRemoverInput.value) - 1;
        if (!isNaN(indiceRemover) && indiceRemover >= 0 && indiceRemover < tarefas.length) {
            const tarefaRemovida = tarefas.splice(indiceRemover, 1);
            renderizarTarefas();
            indiceRemoverInput.value = '';
            exibirMensagem(`Tarefa "${tarefaRemovida[0].texto}" removida.`);
        } else {
            exibirMensagem('Índice inválido.', 'error');
        }
    });

    concluirBtn.addEventListener('click', () => {
        const indiceConcluir = parseInt(indiceConcluirInput.value) - 1;
        if (!isNaN(indiceConcluir) && indiceConcluir >= 0 && indiceConcluir < tarefas.length) {
            tarefas[indiceConcluir].concluida = !tarefas[indiceConcluir].concluida;
            renderizarTarefas();
            indiceConcluirInput.value = '';
            exibirMensagem(`Tarefa "${tarefas[indiceConcluir].texto}" marcada como ${tarefas[indiceConcluir].concluida ? 'concluída' : 'não concluída'}.`);
        } else {
            exibirMensagem('Índice inválido.', 'error');
        }
    });

    renderizarTarefas(); // Renderiza as tarefas iniciais (se houver alguma)
});