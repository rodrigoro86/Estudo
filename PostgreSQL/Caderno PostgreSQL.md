# PostgreSQL
### Curso - Udemy - Curso completo de PostgreSQL! Do Básico ao Avançado v2022! 

#### SQL - Structured Query Language

##### Conectando ao banco 
`
mysql -uroot teste
`  
##### SHOW TABLES
Mostra todas as tabelas do banco 
`
SHOW TABLES;
`  
##### SELECT  
- Seleciona tudo da tabela AREA
`
SELECT * FROM AREA;
`  
- Seleciona todos os dados das colunas DEPTNUM, NOME, SALARIO da tabela FUN
`
SELECT DEPTNUM, NOME, SALARIO FROM FUN;
`  
- Seleciona todos os dados da tabela FUN que contém o valor 10 na coluna DEPTNUM  
`
SELECT * FROM FUN WHERE DEPTNUM = 10;
`  
- Utiliando o "as" ele troca o nome -> Traduz o nome da coluna SALARIO para SALARY e COMISSAO para COMMISION  
`
SELECT SALARIO as SALARY, COMISSAO as COMMISION from FUN;
`  
- Traduz o nome das coluna e salva a tradução na memória, e com o X é possível filtrar as linhas com WHERE utilizando qualquer nome da coluna por exemplo WHERE SALARIO ou WHERE SALARY. 
`  
SELECT * FROM (SELECT SALARIO as SALARY, COMISSAO as COMMISION from FUN) X WHERE SALARY < 5000;
`  
- Concatenar os valores  
`
SELECT NOME, CARGO from FUN WHERE DEPTNUM=10;
`  

| NOME     | CARGO     |
|-|-|
| CLARA    | GERENTE   |
| REYNALDO | CEO       |
| MILLENA  | ATENDENTE |

`
SELECT CONCAT(NOME, ' tem o cargo de ', CARGO) AS MSG from FUN WHERE DEPTNUM=10;
`  
| MSG                              |
|-|
| CLARA tem o cargo de GERENTE     |
| REYNALDO tem o cargo de CEO      |
| MILLENA tem o cargo de ATENDENTE |  
- IF e ELSE
`
select NOME, SALARIO, case when SALARIO <= 2000 then 'BAIXO' when SALARIO >= 4000 then 'ALTO' else 'MEDIO' end as RESULTADO from FUN;
`  

| NOME     | SALARIO | RESULTADO |
|-|-|-|
| SILVIA   |     800 | BAIXO     |
| ALAN     |    1600 | BAIXO     |
| WALDIR   |    1250 | BAIXO     |
| JOAO     |    2975 | MEDIO     |
| MARTINS  |    1250 | BAIXO     |
| BIANCA   |    2850 | MEDIO     |
| CLARA    |    2450 | MEDIO     |
| DARIO    |    3000 | MEDIO     |
| REYNALDO |    5000 | ALTO      |
| CARLOS   |    1500 | BAIXO     |
| ADAO     |    1100 | BAIXO     |
| JAIMES   |     950 | BAIXO     |
| HENRY    |    3000 | MEDIO     |
| MILLENA  |    1300 | BAIXO     |

- Pega a cinco primeiras linhas 
`
SELECT * FROM FUN limit 5;
`  
- Pega todos os valores nulos. 
`
SELECT * from FUN WHERE COMISSAO is null;
`  
- Pega todas as linhas que não são nulas
`
SELECT * from FUN WHERE COMISSAO is not null;
`  
- Traduz o resultado NULL para 0
`
SELECT coalesce(comissao, 0) from FUN;
`  
- Seleciona algumas colunas filtra os valores e ordena pela coluna salário de ordem decrescente. 
`
SELECT NOME, CARGO, SALARIO from FUN where DEPTNUM=10 order by SALARIO DESC;
`  
ou ordena pela terceira coluna que é a coluna salário.
`
SELECT NOME, CARGO, SALARIO from FUN where DEPTNUM=10 order by 3 DESC;
`  
- Ordena os valores inteiros e depois nulos  
`
SELECT NOME, SALARIO, COMISSAO FROM (SELECT NOME, SALARIO, COMISSAO, CASE WHEN COMISSAO is null then 0 else 1 end as is_null from FUN) X ORDER BY is_null DESC, COMISSAO; 
`  

##### Junção das tabelas  
-  Une duas partes da mesma tabela numa tabela temporária  
`
SELECT NOME, DEPTNUM FROM FUN WHERE DEPTNUM = 10 UNION ALL SELECT '------', null FROM TABELA1 UNION ALL SELECT NOME, DEPTNUM FROM AREA;
`  

| NOME          | DEPTNUM |
|-|-|
| CLARA         |      10 |
| REYNALDO      |      10 |
| MILLENA       |      10 |
| ------        |    NULL |
| CONTABILIDADE |      10 |
| PESQUISADOR   |      20 |
| VENDAS        |      30 |
| OPERAÇÕES     |      40 |  

- Filtra os números repetidos  
`
SELECT DEPTNUM FROM FUN UNION SELECT DEPTNUM FROM AREA;
`  
- Filtra o DEPTNIM de duas planilhas. f e a são nomes definidos para as tabelas. 
`
SELECT f.NOME, a.CIDADE FROM FUN f, AREA a WHERE f.DEPTNUM = a.DEPTNUM AND f.DEPTNUM = 10;
`  
- Mostra o valor de uma coluna de uma tabela que não tem na outra tabela.
`
SELECT DEPTNUM from AREA WHERE DEPTNUM not in (SELECT DEPTNUM FROM FUN);
` 
ou  
`
SELECT DISTINCT DEPTNUM from AREA WHERE DEPTNUM not in (SELECT DEPTNUM FROM FUN);
`  
- Seleciona os valores da coluna NOME da tabela FUN e os valores da coluna CIDADE da tabela AREA enquanto os valores DEPTNUM da tabela FUN for igual a 10 e os valores DEPTNUM da tabela area sejam iguais aos valores DEPTNUM da tabela FUN.  
`
SELECT f.NOME, a.cidade from FUN f, AREA a where f.DEPTNUM = 10 and a.DEPTNUM = f.DEPTNUM;
`  
- Transforma todos os valores NULL da coluna COMISSAO em 0 e retorna todos os valores que são menores que o valor da COMISSAO do NOME WALDIR. 
`
SELECT NOME, COMISSAO, coalesce(COMISSAO, 0) from FUN where coalesce(COMISSAO, 0)<(select COMISSAO from FUN where NOME='WALDIR');
`  

##### NÚMEROS
- Cálcular a média 
`
SELECT avg(SALARIO) AS media_salarial from FUN;
`  
- Cálcular a média por departamento
`
SELECT DEPTNUM, avg(SALARIO) as media_salarial from FUN group by DEPTNUM;
`  
- Busca o salário minimo e máximo e retorna em uma tabela 
`
select min(SALARIO) as salário_minimo, max(SALARIO) as salário_máximo from FUN;
`  
- Retorna o salário mínimo e máximo separados por departamento.
`
 SELECT DEPTNUM, min(SALARIO) as salário_mínimo, max(SALARIO) as salário_máximo FROM FUN group by DEPTNUM;
`  

| DEPTNUM | salário_mínimo   | salário_máximo   |
|-|-|-|
|      10 |             1300 |             5000 |
|      20 |              800 |             3000 |
|      30 |              950 |             2850 |

- Soma todos os valores da coluna SALARIO. 
`
select sum(SALARIO) from FUN;
`  
- Conta a quantidade de linhas de uma tabela
`
select count(*) from FUN;
`  
- Conta a quantidade de linhas dos grupos DEPTNUM. 
`
select DEPTNUM, count(*) from FUN group by DEPTNUM;
`  
- COUNT não conta valores NULL 
- Cria um coluna com a progração do salário. 
`
select NOME, SALARIO, sum(SALARIO) over (order by SALARIO, FUNNUM) as TOTAL from FUN order by 2;
`  

| NOME     | SALARIO | TOTAL |
|-|-|-|
| SILVIA   |     800 |   800 |
| JAIMES   |     950 |  1750 |
| ADAO     |    1100 |  2850 |
| WALDIR   |    1250 |  4100 |
| MARTINS  |    1250 |  5350 |
| MILLENA  |    1300 |  6650 |
| CARLOS   |    1500 |  8150 |
| ALAN     |    1600 |  9750 |
| CLARA    |    2450 | 12200 |
| BIANCA   |    2850 | 15050 |
| JOAO     |    2975 | 18025 |
| DARIO    |    3000 | 21025 |
| HENRY    |    3000 | 24025 |
| REYNALDO |    5000 | 29025 |  

##### Inserir

- Insere um dado na tabele
`
INSERT into AREA (DEPTNUM, NOME, CIDADE) values (60, 'TI', 'São Paulo');
`  
- Insere valor default caso a coluna tenha prédefinido um valor default. 
`
insert into TABELALA (id) values (default);
`
- Inserir valores NULL
`
insert into TABELALA (id) values (null);
`  
- Copia dos dados de uma coluna e cola em outra tabela.
`
INSERT into AREA2 (DEPTNUM, NOME, CIDADE) SELECT DEPTNUM, NOME, CIDADE from AREA;
`
##### Update
- Atualiza o salário em 20 % do departamento 20.
`
update FUN set SALARIO = SALARIO*1.20 where DEPTNUM = 20;
`  
##### Remoção  
- Remove tudão 
`
DELETE from FUN;
`
- Remove um linha.
`
DELETE from FUN where DEPTNUM = 10;
`  
- Remove as linhas de uma tabela que não existem o valor do departamento em outra tabela. 
`
DELETE from FUN where not exists (select * from AREA where ARE.DEPTNUM = FUN.DEPTNUM);
`  
- Remove os valores repetidos mantendo o menor id.
`
DELETE from TESTE where id not in (select min(id) from TESTE group by nome);
`  
##### Criação de tabela  
- Cria uma tabela
`
CREATE TABLE TABELALA (id integer default 0);
`  
##### Alteração da tabela
- Altera o id para primary key
`
ALTER TABLE TABELALA ADD CONSTRAINT pk_id PRIMARY KEY (id);
`  
##### Remove uma tabela 
- Para remover uma tabela 
`
DROP TABLE TABELALA
`
