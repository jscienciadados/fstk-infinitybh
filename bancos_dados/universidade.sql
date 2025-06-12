CREATE DATABASE universidade;

USE universidade;


CREATE TABLE aluno_unids (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    endereco TEXT
);

CREATE TABLE professores_unid (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100),
    endereco TEXT
);

CREATE TABLE turmas_unid (
    id INT AUTO_INCREMENT PRIMARY KEY,
    horario_inicio TIME,
    dia_semana VARCHAR(20)
);

CREATE TABLE disciplinas_univ (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    qtd_aulas INT
);

CREATE TABLE alunos_turmas_univ (
    aluno_id INT,
    turma_id INT,
    PRIMARY KEY (aluno_id, turma_id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

CREATE TABLE disciplinas_turmas_univ (
    disciplina_id INT,
    turma_id INT,
    PRIMARY KEY (disciplina_id, turma_id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

CREATE TABLE professores_disciplinas_univ (
    professor_id INT,
    disciplina_id INT,
    PRIMARY KEY (professor_id, disciplina_id),
    FOREIGN KEY (professor_id) REFERENCES professores(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas_univ(id)
);

INSERT INTO aluno_unids (matricula, nome, idade, endereco) VALUES ('A1001', 'Lucas Silva', 15, 'Rua D, 101');
INSERT INTO aluno_unids (matricula, nome, idade, endereco) VALUES ('A1002', 'Ana Costa', 15, 'Av. E, 202');
INSERT INTO aluno_unids (matricula, nome, idade, endereco) VALUES ('A1003', 'João Souza', 17, 'Rua A, 123');
INSERT INTO aluno_unids (matricula, nome, idade, endereco) VALUES ('A1004', 'Mariana Lima', 15, 'Trav. C, 789');
INSERT INTO aluno_unids (matricula, nome, idade, endereco) VALUES ('A1005', 'Carlos Mendes', 16, 'Av. E, 202');

INSERT INTO professores_unid (matricula, nome, especialidade, endereco) VALUES ('P2001', 'Paulo Andrade', 'Matemática', 'Rua D, 101');
INSERT INTO professores_unid (matricula, nome, especialidade, endereco) VALUES ('P2002', 'Fernanda Torres', 'Português', 'Av. E, 202');

SELECT * FROM disciplinas_univ;
SELECT * FROM professores_unid;
SELECT * FROM aluno_unids;

SELECT 
    a.nome AS aluno,
    t.id AS turma,
    d.nome AS disciplina,
    p.nome AS professor
FROM 
    alunos a
JOIN alunos_turmas_univ at ON a.id = at.aluno_id
JOIN turmas_unid t ON at.turma_id = t.id
JOIN disciplinas_turmas dt ON t.id = dt.turma_id
JOIN disciplinas_univ d ON dt.disciplina_id = d.id
JOIN professores_disciplinas_univ pd ON d.id = pd.disciplina_id
JOIN professores_unid p ON pd.professor_id = p.id
ORDER BY a.nome, d.nome;







