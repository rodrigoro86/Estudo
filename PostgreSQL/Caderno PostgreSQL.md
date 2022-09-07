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

