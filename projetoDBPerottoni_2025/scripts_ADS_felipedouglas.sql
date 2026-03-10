atividade que o professor mando no whatsapp

--código 
CREATE TABLE produto (
ID_produto Integer PRIMARY KEY,
marca Varchar(20),
descricao Varchar(300),
valor_unitario Numeric(5,2)
)

CREATE TABLE compra_produto (
quantde_produto Numeric(5),
vl_parcial Numeric(5,2),
ID_produto Integer,
ID_compra Integer,
PRIMARY KEY(ID_produto,ID_compra),
FOREIGN KEY(ID_produto) REFERENCES produto (ID_produto)
)

CREATE TABLE cliente (
ID_cliente Integer PRIMARY KEY,
CPF Char(11),
email Varchar(80),
DT_nasc Date,
sexo Char(1),
telefone Varchar(50),
CEP Char(8),
endereco Varchar(80),
nome_cliente Varchar(80)
)

CREATE TABLE atendente (
ID_atendente Integer PRIMARY KEY,
matricula Char(11),
CPF Char(11),
RG Char(8),
Pin Char(11),
telefone Varchar(50),
nome_atendente Varchar(80),
email Varchar(80),
endereco Varchar(80),
CEP Char(8)
)

CREATE TABLE compra (
forma_pagamento Varchar(10),
vl_total Numeric(5,2),
hora_pagamento Timestamp,
DT_compra Date,
ID_compra Integer PRIMARY KEY,
ID_cliente Integer,
ID_atendente Integer,
FOREIGN KEY(ID_cliente) REFERENCES cliente (ID_cliente),
FOREIGN KEY(ID_atendente) REFERENCES atendente (ID_atendente)
)

ALTER TABLE compra_produto ADD FOREIGN KEY(ID_compra) REFERENCES compra (ID_compra)

--questao 1 parte 2
--mostrar o banco e as tabelas. Ambos foram criados pelo código do br_modelo (que está aqui em cima)
--codigo usado na população do bando
INSERT INTO public.atendente(
	id_atendente, matricula, cpf, rg, pin, telefone, nome_atendente, email, endereco, cep)
	VALUES (1, 01, '32122377156', '33514119', '12345', '998050404', 'arthur', 'arthur@gmail.com', 'rua dos lirios', '78110000'),
	       (2, 02, '42066670196', '21479112', '54321', '999039582', 'pedro', 'pedro@gmail.com', 'rua das araras', '78025340'),
	       (3, 03, '12345678901', '21089045', '67890', '999097927', 'guilherme', 'guilherme@gmail.com', 'rua das gaivotas', '78250090')

INSERT INTO public.cliente(
	id_cliente, cpf, email, dt_nasc, sexo, telefone, cep, endereco, nome_cliente)
	VALUES (1, '12332187694', 'julianovoemail@gmail.com', '2004-04-21', 'F', '991543242', '78050410', 'avenida miguel sutil', 'julia'),
	       (2, '09876543210', 'carla@gmail.com', '1998-11-15', 'F', '940506070', '78090411', 'casa do caralho', 'carla'),
           (3, '32132132144', 'rafael@gmail.com', '1974-11-20', 'M', '991174929', '78041119', 'puta que pariu', 'rafael');

 INSERT INTO public.produto(
	id_produto, marca, descricao, valor_unitario, estoque)
	VALUES (11, 'Coca-Cola', 'Açucar puro', '11.59', '100'),
	       (21, 'Dunhill', 'cancêr e mal hálito', '15.00', '100'),
           (31, 'Puríssima', 'água', '4.49', '100'),
	       (41, 'Miojo', 'de carne', '1.99', '100'),
           (51, 'óleo', 'seila', '9.99', '100');

INSERT INTO public.compra(
    forma_pagamento, vl_total, hora_pagamento, dt_compra, id_compra, id_cliente, id_atendente)
VALUES
    ('crédito', 45, '2025-10-30 11:32:31', '2025-10-30', 1, 1, 1),
    ('dinheiro', 5.97, '2025-10-30 13:43:17', '2025-10-30', 2, 2, 2),
    ('débito', 29.97, '2025-10-30 09:12:48', '2025-10-30', 3, 3, 3);

INSERT INTO public.compra_produto(
	quantde_produto, vl_parcial, id_produto, id_compra)
	VALUES (3, 45, 11, 1),
           (3, 5.97, 41, 2),
	       (3, 29.97, 51, 3);



--questao 3 exercicio 1 
SELECT nome_cliente,
       nome_atendente,
       vl_total
 FROM cliente,
      atendente,
      compra
 WHERE cliente.ID_cliente = compra.ID_cliente
  AND atendente.ID_atendente = compra.ID_atendente;

--questao 3 exercicio 2 
SELECT marca,
        quantde_produto,
        vl_parcial
 FROM produto,
      compra_produto
	  WHERE produto.ID_produto = compra_produto.ID_produto;
     
--questao 3 exercicio 3
SELECT DT_compra
 FROM compra
 WHERE DT_compra > '2025/10/01'

 --questao 3 exercicio 4 (listar clientes que fizeram mais de uma compra) 

 SELECT COUNT(*) AS total_cliente
FROM (
    SELECT c.id_cliente
    FROM cliente c, compra co
	WHERE c.id_cliente = co.id_cliente
	GROUP BY c.id_cliente
	HAVING COUNT(co.id_compra) > 1
) sub;

--questao 4 exercicio 1 (criar tabela 'estoque', porem ja existe)

ALTER TABLE produto ADD COLUMN estoque Integer;


--questao 4 exercicio 2 (adicionar coluna 'estoque' na tabela 'produto', porem ja existe)
UPDATE produto
SET estoque = estoque + 100
WHERE id_produto = 11;
--apenas mudar o ID para cada produto

--questao 4 exercicio 3 (mudar email, que já está mudado)

UPDATE public.cliente
   SET  email = 'julianovoemail@gmail.com'
   WHERE id_cliente = 1;
SELECT * FROM public.cliente
ORDER BY id_cliente ASC

--questao 5 exercicio 1

SELECT SUM (vl_total)
    FROM public.compra

--questao 5 exercicio 2 (mostrar o produto mais caro e seu valor)

SELECT marca, valor_unitario
   FROM produto
   WHERE valor_unitario =(
  SELECT MAX (valor_unitario) 
     FROM produto
   );

--questao 5 exercicio 3 (mostrar os atendentes e suas respectivas quantidades de vendas realizadas)

SELECT
    A.nome_atendente,
    COUNT(C.id_compra) AS total_compra
FROM
    Atendente AS a
LEFT JOIN
    Compra AS C ON A.id_atendente = C.id_atendente
GROUP BY
    A.nome_atendente, A.id_atendente
ORDER BY
    total_compra DESC;


{tudo certinho, só copiar e colar na hora se quiser criar um banco novo
}
