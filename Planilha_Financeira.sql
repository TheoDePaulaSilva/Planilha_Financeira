create database Planilha_Financeira;
use Planilha_Financeira;

create table usuario(
	id int primary key,
    nome varchar(255),
    senha_hash varchar(60),
    data_criacao datetime
);
