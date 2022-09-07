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