create database os;

use os;

create table clientes(
	id int auto_increment primary key,
	nome varchar(40) not null,
	cpf char(11) not null,
	telefone varchar(15),
	celular varchar(15) not null,
	rua varchar(40) not null,
	bairro varchar(40) not null,
	cidade varchar(40) not null,
	estado char(2) not null,
	CEP varchar(20) 
) engine=innodb;

create table ordem(
  id_os int  auto_increment primary key,
  tipo varchar(10) not null,
  marca varchar (20) not null,
  modelo varchar (20) not null,
  num_serie varchar (30),
  defeito text,
  solucao text,
  valor decimal(10,2),
  status bit,
  id_cliente int,
  data_entrada datetime,
  data_saida datetime
) engine=innodb;

alter table ordem
add constraint fk_cliente
foreign key (id_cliente) references clientes(id);