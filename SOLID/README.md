# SOLID

#### Curso
ALURA - SOLID com Java: princípios da programação orientada a objetos. 

### Single Resposnibility Principle
Princípio da resposabilidade única  
### Open Closed Principle
Princípio aberto e fechado  
### Liskov Substituition Principle
Princípio da substituição de Liskov  
### Interface Segregation Principal 
Princípio da segregação de interface 
### Dependency Inversion Principal 
Princípio da inversão de dependencias 

## Coesão 
Harmonia entre elementos, onde os atributos, clases e variáveis estão em harmonia sobre a sua função.   
A classe deve ter uma única responsábilidade.  
Classes não coesas tendem a crescer indefinidamente, o que as tornam difíceis de manter.  
Uma classe coesa faz bem uma única coisa.  
Classes coesas não devem ter várias responsabilidades.  

## Encapsulamento 
Incluir ou proteger alguma coisa em uma cápsula.  
Classes não encapsuladas permitem violação de regras de negócio, além de aumentarem o acoplamento.  
Getters e setters não são formas eficientes de aplicar encapsulamento.  
É interessante fornecer acesso apenas ao que é necessário em nossas classes.  
O encapsulamento torna o uso das nossas classes mais fácil e intuitivo.  

## Acoplamento  
Classe que chama outra classe, o problema está quando a dependencia é muito forte onde uma classe utiliza muitas coisas da outra classe caso a outra classe tem alguma alteração isso impactera a primeira classes.  
Classes acopladas causam fragilidade no código da aplicação, o que dificulta sua manutenção.  

## Single Resposnibility Principle
Não é só porque você pode é que você deveria.  
Uma classe deveria ter apenas um único motivo para mudar - Robert(Uncle Bob) Martin.  

## Open Closed Principle
Não precisa fazer um cirurgia de peito aberto para colcar um casaco.  
Entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, porém fechadas para modificação - Bertrand Meyer.  

## Liskov Substituition Principle  
Separece com um pato, faz QUACK como um pato mas precisa de baterias, então não é um pato.  
Se q(x) é uma propriedade demonstrável dos objetos x de tipo T, então q(y) deve ser verdadeiro pára objetos y de tipo S, onde S é um subtipo de T - Barbara Liskov  
Embora a herança favoreça o reaproveitamento de código, ela pode trazer efeitos colaterais quando não utilizada da maneira correta;  
O Princípio de Substituição de Liskov (LSP) diz que devemos poder substituir classes base por suas classes derivadas em qualquer lugar, sem problema.   

## Dependency Inversion Principal 
Abstrações não devem depender de implementações. Implementações devem depender de abstrações - Robert (Uncle Bob) Martin.  

## Interface Segregation Principal 
Uma classe não deveria ser forçada a depender de métodos que não utilizará - Robert (Uble Bob) Martin.  
