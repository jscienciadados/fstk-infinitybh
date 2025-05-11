function gerenciarListaDeNomes() {
  let listaNomes = [];
  let executando = true;

  while (executando) {
    const escolha = prompt(
      "Escolha uma operação:\n" +
      "1 - Adicionar nome\n" +
      "2 - Filtrar nomes por letra\n" +
      "3 - Buscar um nome específico\n" +
      "4 - Transformar nomes para maiúsculas\n" +
      "5 - Verificar se todos os nomes têm mais de três caracteres\n" +
      "6 - Exibir lista atual\n" +
      "7 - Sair"
    );

    switch (escolha) {
      case "1":
        const novoNome = prompt("Digite o nome a ser adicionado:");
        listaNomes.push(novoNome);
        console.log("Nome adicionado:", novoNome);
        console.log("Lista atualizada:", listaNomes);
        break;

      case "2":
        const letraFiltro = prompt("Digite a letra inicial para filtrar os nomes:");
        const nomesFiltrados = listaNomes.filter(nome => nome.toLowerCase().startsWith(letraFiltro.toLowerCase()));
        console.log(`Nomes que começam com '${letraFiltro.toUpperCase()}':`, nomesFiltrados);
        break;

      case "3":
        const nomeBusca = prompt("Digite o nome a ser buscado:");
        const nomeEncontrado = listaNomes.find(nome => nome === nomeBusca);
        if (nomeEncontrado) {
          console.log("Nome encontrado:", nomeEncontrado);
        } else {
          console.log("Nome não encontrado na lista.");
        }
        break;

      case "4":
        const nomesMaiusculos = listaNomes.map(nome => nome.toUpperCase());
        console.log("Lista de nomes em maiúsculas:", nomesMaiusculos);
        break;

      case "5":
        const todosMaisDeTresCaracteres = listaNomes.every(nome => nome.length > 3);
        console.log("Todos os nomes têm mais de três caracteres?", todosMaisDeTresCaracteres);
        break;

      case "6":
        console.log("Lista de nomes atual:", listaNomes);
        break;

      case "7":
        executando = false;
        console.log("Programa encerrado.");
        break;

      default:
        console.log("Opção inválida. Por favor, escolha uma das opções listadas.");
    }
  }
}

console.log(gerenciarListaDeNomes());