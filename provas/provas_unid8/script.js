// --- Classe Livro ---
class Livro {
    constructor(titulo, autor, ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }

    exibirInformacoes() {
        return `Título: ${this.titulo}, Autor: ${this.autor}, Ano: ${this.ano}`;
    }
}

// --- Variáveis Globais ---
const biblioteca = [];

// --- Elementos do DOM ---
const formCadastro = document.querySelector('#cadastro form');
const inputTitulo = document.getElementById('titulo');
const inputAutor = document.getElementById('autor');
const inputAno = document.getElementById('ano');
const mensagemCadastro = document.getElementById('mensagemCadastro');

const inputBuscaTitulo = document.getElementById('buscaTitulo');
const btnBuscar = document.getElementById('btnBuscar');
const resultadoBusca = document.getElementById('resultadoBusca');

const btnListar = document.getElementById('btnListar');
const listaLivros = document.getElementById('listaLivros');
const mensagemLista = document.getElementById('mensagemLista');

const btnEstatisticas = document.getElementById('btnEstatisticas');
const resultadoEstatisticas = document.getElementById('resultadoEstatisticas');
const mensagemEstatisticas = document.getElementById('mensagemEstatisticas');

// --- Funções de Manipulação da Biblioteca ---

/**
 * Adiciona um novo livro à biblioteca e atualiza a exibição.
 * @param {string} titulo
 * @param {string} autor
 * @param {number} ano
 */
function adicionarLivro(titulo, autor, ano) {
    // Validação básica para evitar livros vazios ou anos inválidos
    if (!titulo || !autor || !ano || ano > new Date().getFullYear()) {
        exibirMensagem(mensagemCadastro, 'Por favor, preencha todos os campos corretamente.', 'error');
        return;
    }

    const novoLivro = new Livro(titulo, autor, ano);
    biblioteca.push(novoLivro);
    exibirMensagem(mensagemCadastro, `"${titulo}" adicionado à biblioteca com sucesso!`, 'success');
    limparCamposCadastro();
    // Atualiza a lista e estatísticas automaticamente após adicionar
    listarLivrosHTML();
    calcularEstatisticasHTML();
}

/**
 * Busca um livro pelo título e exibe o resultado na página.
 * @param {string} titulo
 */
function buscarLivro(titulo) {
    if (!titulo.trim()) {
        exibirMensagem(resultadoBusca, 'Por favor, digite um título para buscar.', 'error');
        return;
    }

    const livroEncontrado = biblioteca.find(livro => livro.titulo.toLowerCase() === titulo.toLowerCase());
    if (livroEncontrado) {
        resultadoBusca.innerHTML = `<strong>Livro Encontrado:</strong><br>${livroEncontrado.exibirInformacoes()}`;
        resultadoBusca.classList.remove('error');
        resultadoBusca.classList.add('success'); // Adiciona classe para estilização de sucesso
    } else {
        resultadoBusca.innerHTML = `Livro com o título "${titulo}" não encontrado na biblioteca.`;
        resultadoBusca.classList.remove('success');
        resultadoBusca.classList.add('error'); // Adiciona classe para estilização de erro
    }
}

/**
 * Lista todos os livros na biblioteca em uma lista HTML.
 */
function listarLivrosHTML() {
    listaLivros.innerHTML = ''; // Limpa a lista antes de preencher

    if (biblioteca.length === 0) {
        exibirMensagem(mensagemLista, 'A biblioteca está vazia.', 'warning');
        return;
    }

    mensagemLista.textContent = ''; // Limpa qualquer mensagem de lista vazia

    biblioteca.forEach(livro => {
        const li = document.createElement('li');
        li.textContent = livro.exibirInformacoes();
        listaLivros.appendChild(li);
    });
}

/**
 * Calcula e exibe as estatísticas da biblioteca na página.
 */
function calcularEstatisticasHTML() {
    if (biblioteca.length === 0) {
        exibirMensagem(mensagemEstatisticas, 'Não há livros na biblioteca para calcular estatísticas.', 'warning');
        resultadoEstatisticas.textContent = '';
        return;
    }

    mensagemEstatisticas.textContent = ''; // Limpa mensagens de aviso
    const anoAtual = new Date().getFullYear();
    const somaIdades = biblioteca.reduce((acumulador, livro) => {
        return acumulador + (anoAtual - livro.ano);
    }, 0);

    const mediaIdades = somaIdades / biblioteca.length;
    resultadoEstatisticas.innerHTML = `Média de idade dos livros na biblioteca: <strong>${mediaIdades.toFixed(2)} anos</strong>.`;
    resultadoEstatisticas.classList.remove('error', 'success'); // Remove classes de erro/sucesso para estatísticas
}

// --- Funções Auxiliares de UI ---

/**
 * Exibe uma mensagem na página com um estilo específico.
 * @param {HTMLElement} elemento O elemento onde a mensagem será exibida.
 * @param {string} texto O texto da mensagem.
 * @param {string} tipo 'success', 'error' ou 'warning' para estilização.
 */
function exibirMensagem(elemento, texto, tipo) {
    elemento.textContent = texto;
    elemento.className = `message ${tipo}`; // Define a classe para estilização
    setTimeout(() => {
        elemento.textContent = '';
        elemento.className = 'message'; // Remove a classe após alguns segundos
    }, 5000); // Mensagem desaparece após 5 segundos
}

/**
 * Limpa os campos do formulário de cadastro.
 */
function limparCamposCadastro() {
    inputTitulo.value = '';
    inputAutor.value = '';
    inputAno.value = '';
}

// --- Event Listeners ---

// Adicionar Livro
formCadastro.addEventListener('submit', (event) => {
    event.preventDefault(); // Impede o recarregamento da página
    const titulo = inputTitulo.value.trim();
    const autor = inputAutor.value.trim();
    const ano = parseInt(inputAno.value);
    adicionarLivro(titulo, autor, ano);
});

// Buscar Livro
btnBuscar.addEventListener('click', () => {
    const titulo = inputBuscaTitulo.value.trim();
    buscarLivro(titulo);
});

// Listar Livros
btnListar.addEventListener('click', listarLivrosHTML);

// Calcular Estatísticas
btnEstatisticas.addEventListener('click', calcularEstatisticasHTML);

// --- Inicialização (Adicionar alguns livros de exemplo e exibir na página ao carregar) ---
document.addEventListener('DOMContentLoaded', () => {
    adicionarLivro("O Hobbit", "J.R.R. Tolkien", 1937);
    adicionarLivro("1984", "George Orwell", 1949);
    adicionarLivro("Dom Quixote", "Miguel de Cervantes", 1605);
    adicionarLivro("Cem Anos de Solidão", "Gabriel García Márquez", 1967);
    // As funções adicionarLivro já chamam listarLivrosHTML e calcularEstatisticasHTML
    // Não precisamos chamá-las novamente aqui, pois os livros de exemplo já são adicionados
    // através da função `adicionarLivro` que já contém a lógica de atualização da UI.
});