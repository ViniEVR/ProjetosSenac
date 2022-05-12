create database hamburgueria;

use hamburgueria;

create table lanche(
	codigo int not null auto_increment,
    nome varchar(30) not null,
    ingredientes varchar(200) not null,
    preco double not null,
    primary key(codigo)
    );
    
INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Holly Fantástico', 'Pão brioche, burger 180g, 
rúcula, creme de gorgonzola, bacon bits e maionese defumada.', '39.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Pulp Ficton Vincent', 'Pão, burger de 150g, 
american cheese, ketchup, mostarda, cebola branca e picles.', '26.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Pulp Fiction Jules', 'Pão brioche, burger de 150g,
 cheddar e cebola caramelizada - acompanha maionese clássica.', '29.90');
 
INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Holly Smoked Jam', 'Pão brioche, burger de 180g, queijo Gouda,
 maionese defumada, geléia de bacon apimentada.', '36.90');
 
 INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Holly Salad', 'Pão brioche, burger de 150g, american cheese, alface, tomate, 
 cebola roxa(acompanha maionese verde).', '28.90');
 
INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Holly Cheese', 'Pão brioche + burger 150g + american cheese
(acompanha maionese verde).', '24.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Holly Bacon', 'Pão brioche, burger 150g, american cheese e
bacon caramelizado.', '24.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Hulk', 'Pão brioche, double smashburger de 150g, cheddar,
rúcula, cebola caramelizada e picles.', '29.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'King Kong', 'Pão, 2 burgers de 180g, american cheese, alface,
tomate, cebola roxa, bacon e acompanha maionese de tabasco.', '47.90');

INSERT INTO lanche(codigo, nome, ingredientes, preco) values('', 'Kill Bill', 'Pão brioche, burger 180g, cheddar cremoso e bacon bits.
O cheddar e o bacon vão separados para você colocar como desejar.', '47.90');
select * from lanche;
DELETE FROM lanche WHERE codigo = 12;

    
create table bebida(
	codigo int not null auto_increment,
    nome varchar(30) not null,
    preco double not null,
    primary key(codigo)
    );
INSERT INTO bebida(codigo, nome, preco) values('', 'Coca-cola', '7.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Sprite', '6.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Fanta uva', '6.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Fanta laranja', '6.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Suco de laranja', '8.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Suco de maracuja', '8.90');
INSERT INTO bebida(codigo, nome, preco) values('', 'Limonada', '8.90');
select * from bebida;


    
create table sobremesa(
	codigo int not null auto_increment,
    nome varchar(30) not null,
    ingredientes varchar(200) not null,
    preco double not null,
    primary key(codigo)
    );    
INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('', 'Torta Gelada Negresco', 'Torta gelada
com base de bolacha Negresco e mousse de maracujá.', '64.90');

INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('', 'Torta Gelada Maracuja', 'Torta gelada com base de pão de ló ou casquinha de bolacha
com recheio a base de maracujá, creme de leite e leite condensado.', '64.90');
 
INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('', 'Mousse Sabores', 'Escolha entre os sabores chocolate,
 maracujá, morango ou napolitano(chocolate, morango e baunilha).', '59.00');
 
 INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('', 'Cheesecake Gelado', 'Sobremesa com base de bolacha e recheio
 composto de cream cheese e leite condensado, com cobertura de frutas vermelhas.', '69.00');
 
  INSERT INTO sobremesa(codigo, nome, ingredientes, preco) values('', 'Sobremesa de Amendoim', 'Sobremesa cremosa composta de amendoim,
  açúcar, manteiga e creme de leite.', '52.00');
  select * from sobremesa;
 
create table funcionario(
codigo int not null auto_increment,
nome varchar(40) not null,
senha varchar(30) not null,
primary key (codigo));

select * from funcionario;

    
    
  
    
