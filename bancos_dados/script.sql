CREATE DATABASE banco_de_dados_pessoal;
USE banco_de_dados_pessoal;

CREATE TABLE pessoas (
  id INT PRIMARY KEY,
  nome_completo VARCHAR(100),
  idade INT,
  genero VARCHAR(20),
  nacionalidade VARCHAR(50),
  email VARCHAR(100),
  estado_civil VARCHAR(20),
  nome_pai VARCHAR(100),
  nome_mae VARCHAR(100)
);

INSERT INTO pessoas (id, nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae)
VALUES
  (1, 'João Souza', 51, 'Masculino', 'Brasileiro', 'joaosouzaps9@gmail.com', 'solteiro', 'Geraldo Pereira', 'Ana Souza'),
  (2, 'Eluane', 25, 'Feminino', 'Brasileira', 'elua@gmail.com.com', 'Solteira', 'Carlos', 'Laura'),
  (3, 'Aline Gomes', 33, 'Feminina', 'Argentina', 'alineg@outlook.com', 'Dirvorciada', 'Luiz Santos', 'Helena Santos');
  
  SELECT nome_completo, idade, genero, estado_civil FROM pessoas;
  
  UPDATE pessoas
SET estado_civil = 'Casado'
WHERE id = 1;

 DELETE FROM pessoas
WHERE id = 2;

 SELECT nome_completo, idade, genero, estado_civil, nacionalidade FROM pessoas;