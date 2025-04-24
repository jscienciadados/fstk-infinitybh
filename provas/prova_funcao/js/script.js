// Lista de tarefas inicial
let tarefas = [];

// Função anônima para adicionar uma tarefa
const adicionarTarefa = function(tarefa) {
    tarefas.push(tarefa);
    console.log(`Tarefa "${tarefa}" adicionada.`);
};

// Arrow function para listar todas as tarefas
const listarTarefas = () => {
    if (tarefas.length === 0) {
        console.log("A lista de tarefas está vazia.");
        return;
    }
    console.log("\n--- Lista de Tarefas ---");
    tarefas.forEach((tarefa, indice) => {
        console.log(`${indice + 1}. ${tarefa}`);
    });
    console.log("-----------------------\n");
};

// Função que recebe um callback para executar operações na lista
function gerenciarTarefas(acao, indiceOuTarefa, novaTarefa) {
    if (acao === 'remover') {
        if (typeof indiceOuTarefa === 'number' && indiceOuTarefa >= 0 && indiceOuTarefa < tarefas.length) {
            const tarefaRemovida = tarefas.splice(indiceOuTarefa, 1);
            console.log(`Tarefa "${tarefaRemovida[0]}" removida.`);
        } else {
            console.log("Índice inválido para remoção.");
        }
    } else if (acao === 'atualizar') {
        if (typeof indiceOuTarefa === 'number' && indiceOuTarefa >= 0 && indiceOuTarefa < tarefas.length && novaTarefa) {
            tarefas[indiceOuTarefa] = novaTarefa;
            console.log(`Tarefa no índice ${indiceOuTarefa + 1} atualizada para "${novaTarefa}".`);
        } else {
            console.log("Índice inválido ou nova tarefa não especificada para atualização.");
        }
    } else if (acao === 'concluir') {
        if (typeof indiceOuTarefa === 'number' && indiceOuTarefa >= 0 && indiceOuTarefa < tarefas.length) {
            tarefas[indiceOuTarefa] = `[Concluída] ${tarefas[indiceOuTarefa].replace('[Concluída] ', '')}`;
            console.log(`Tarefa no índice ${indiceOuTarefa + 1} marcada como concluída.`);
        } else {
            console.log("Índice inválido para concluir tarefa.");
        }
    } else {
        console.log("Ação de gerenciamento inválida.");
    }
}

// --- Interação com o Usuário via Console ---

function iniciarGerenciador() {
    let opcao;

    do {
        opcao = prompt(
            "Escolha uma ação:\n" +
            "1. Adicionar Tarefa\n" +
            "2. Listar Tarefas\n" +
            "3. Remover Tarefa\n" +
            "4. Atualizar Tarefa\n" +
            "5. Concluir Tarefa\n" +
            "0. Sair"
        );

        switch (opcao) {
            case '1':
                const novaTarefa = prompt("Digite a nova tarefa:");
                if (novaTarefa) {
                    adicionarTarefa(novaTarefa);
                }
                break;
            case '2':
                listarTarefas();
                break;
            case '3':
                listarTarefas();
                const indiceRemover = parseInt(prompt("Digite o número da tarefa para remover:"), 10) - 1;
                gerenciarTarefas('remover', indiceRemover);
                break;
            case '4':
                listarTarefas();
                const indiceAtualizar = parseInt(prompt("Digite o número da tarefa para atualizar:"), 10) - 1;
                const novaDescricao = prompt("Digite a nova descrição da tarefa:");
                if (novaDescricao) {
                    gerenciarTarefas('atualizar', indiceAtualizar, novaDescricao);
                }
                break;
            case '5':
                listarTarefas();
                const indiceConcluir = parseInt(prompt("Digite o número da tarefa para concluir:"), 10) - 1;
                gerenciarTarefas('concluir', indiceConcluir);
                break;
            case '0':
                console.log("Saindo do gerenciador de tarefas.");
                break;
            default:
                console.log("Opção inválida. Tente novamente.");
        }
    } while (opcao !== '0');
}

// Iniciar o gerenciador quando a página carregar
window.onload = iniciarGerenciador;