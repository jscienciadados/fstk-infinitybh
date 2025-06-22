CREATE DATABASE estoque;

CREATE TABLE Estoque (
    EstoqueID INT AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT,
    DataEntrada DATE,
    
    -- Definição da chave primária
    CONSTRAINT PK_Estoque PRIMARY KEY (EstoqueID),
    
    -- Definição das chaves estrangeiras
    CONSTRAINT FK_Produto FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    CONSTRAINT FK_Fornecedor FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

SELECT *
FROM Estoque
FULL OUTER JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID
FULL OUTER JOIN Fornecedores ON Estoque.FornecedorID = Fornecedores.FornecedorID;

SELECT FornecedorID, SUM(Quantidade) as TotalProdutos
FROM Estoque
GROUP BY FornecedorID;

ALTER TABLE Estoque
ADD COLUMN ValorUnitario DECIMAL(10,2);