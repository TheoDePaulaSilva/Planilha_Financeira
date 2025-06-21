create database Planilha_Financeira;
use Planilha_Financeira;

create table usuario(
	id int primary key auto_increment,
    nome varchar(255) not null,
    email varchar(255) not null unique,
    senha_hash varchar(60) not null,
    data_criacao date not null
);

CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE
);

create table movimentação(
	id int primary key auto_increment,
    usuario_id INT NOT NULL,
    tipo ENUM('ganho','gasto') not null,
    valor DECIMAL(15,2) not null,
    categoria_id int,
    descricao TEXT,
    data_mov DATE not null,
    
    foreign key (usuario_id) references usuario(id) on delete cascade,
    foreign key (categoria_id) references categoria(id) on delete set null
);


select * from usuario;