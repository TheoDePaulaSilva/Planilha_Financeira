create database Planilha_Financeira;
use Planilha_Financeira;

create table usuario(
	id int primary key,
    email varchar(255),
    nome varchar(255) not null,
    senha_hash varchar(60) not null,
    data_criacao datetime not null
);
