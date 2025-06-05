class Produto {
    constructor(nome, preco, categoria) {
        this.nome = nome;
        this.preco = preco;
        this.categoria = categoria;
    }

    exibirDetalhes() {
        return `${this.nome} (${this.categoria}): R$${this.preco.toFixed(2)}`;
    }
}

class GerenciadorProdutos {
    constructor() {
        this.produtos = [];
    }

    adicionarProduto(nome, preco, categoria) {
        const produto = new Produto(nome, preco, categoria);
        this.produtos.push(produto);
        return produto;
    }

    listarProdutos() {
        console.log("\nLista de Produtos:");
        this.produtos.forEach(produto => {
            console.log(produto.exibirDetalhes());
        });
    }

    buscarProduto(nome) {
        return this.produtos.find(produto => 
            produto.nome.toLowerCase() === nome.toLowerCase()
        );
    }

    filtrarPorCategoria(categoria) {
        return this.produtos.filter(produto => 
            produto.categoria.toLowerCase() === categoria.toLowerCase()
        );
    }

    resumoEstatisico() {
        const somaPrecos = this.produtos.reduce((total, produto) => 
            total + produto.preco, 0
        );
        
        return {
            quantidade: this.produtos.length,
            somaTotal: somaPrecos,
            mediaPreco: somaPrecos / this.produtos.length || 0
        };
    }
}

// Exemplo de uso
const gerenciador = new GerenciadorProdutos();

// Adicionando produtos
gerenciador.adicionarProduto("Laptop", 3999.99, "Eletrônicos");
gerenciador.adicionarProduto("Mouse", 89.90, "Eletrônicos");
gerenciador.adicionarProduto("Camisa", 79.90, "Vestuário");

// Listando todos os produtos
gerenciador.listarProdutos();

// Buscando um produto específico
const produtoEncontrado = gerenciador.buscarProduto("Laptop");
console.log("\nProduto encontrado:", produtoEncontrado?.exibirDetalhes());

// Filtrando por categoria
const eletronicos = gerenciador.filtrarPorCategoria("Eletrônicos");
console.log("\nProdutos da categoria Eletrônicos:");
eletronicos.forEach(produto => console.log(produto.exibirDetalhes()));

// Mostrando resumo estatístico
const estatisticas = gerenciador.resumoEstatisico();
console.log("\nResumo Estatístico:");
console.log(`Quantidade de produtos: ${estatisticas.quantidade}`);
console.log(`Soma total dos preços: R$${estatisticas.somaTotal.toFixed(2)}`);
console.log(`Média dos preços: R$${estatisticas.mediaPreco.toFixed(2)}`);