-- Criar a tabela Produtos
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10,2)
);

-- Inserir três produtos diferentes
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES 
('Laptop Dell', 15, 3999.99),
('Mouse Logitech', 50, 89.90),
('Teclado Mecânico', 25, 299.99);