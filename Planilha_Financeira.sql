create database Planilha_Financeira;
use Planilha_Financeira;

create table usuario(
	id int primary key,
    nome varchar(255) not null,
    email varchar(255),
    senha_hash varchar(60) not null,
    data_criacao date not null
);

select * from usuario;