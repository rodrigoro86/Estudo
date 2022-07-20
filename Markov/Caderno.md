# Cadeias de Markov
## Video-Aula  1
Cadeia de Markov - Aula 1  
link: https://www.youtube.com/watch?v=k6FAZJGTZJo&list=PLSc7xcwCGNh0jSylDm0QrDJaFTC3vAbvc&index=2


## Definição: 
Considere o processo estocástico {$X_{n},n\in N$}. Nós dizemos que este processo é uma cadeia de Markov se:  
$P(X_{n+1}=j|X_{0}=i_{0},X_{1}=i_{1},...,X_{n}=i)=P(X_{n+1}=j|X_{n}=i)$  
Para todos estados $i,j,i_{0},...,i_{n-1}$  
<br>
![](imagens/exemplo_Markov_1.png)  
<br>
Seja P uma matriz quadrada cusjas entradas $P_{ij}$ são definidas para todos os estados i e j. Então, P é chamada matrix Markoviana (ou matriz de probabilidade de transição) se:  
* Para todo $i\in S, P_{ij}\ge0$, onde S é o conjunto de estados. 
* $\sum_{i\in j}P_{ij}=1,\forall i \in S$  
Um processo Markoviano é totalmente definido pela sua matriz de probablidades de transição e a distribuição de probabilidade de $X_{0}$  
### Exemplo:  
Uma cadeia de Markov $X_{0},X_{1},...,X_{n}$ nos estados 0, 1, 2 tem matriz de probabilidade de transição e distribuição de probabilidade inicial:  
![](imagens/exemplo_Markov_2.png)  
$P(X_{0}=0)=0,3  P(X_{0}=1)=0,4 P(X_{0}=2)=0,3$ -> Probabilidade de começar nesses estados  
$P(X_{0}=0).P_{01}.P_{10}.P_{02}.P_{20}=0,3.0,2.0,9.0,7.0,1=0,003$  
<br>
### Exemplo  
Uma cadeia de Markov $X_{0},X_{1},...,X{n}$ nos estados 0, 1, 2 tem matriz de probabilidade de transição e distribuição de probabilidade inicial:  
**Determine**: $P(X_{1}=1,X_{2}=0|X_{0}=0)$ "Determine a probabilidade de ir da posição 1 para posição 0 dado que inicia na posição 0"  
**Resposta:** $P(X_{1}=1,X_{2}=0|X_{0}=0) = P_{01}.P_{10} = 0,2.0,9=0,18$  
<br>
### Exemplo  
Uma cadeia de Markov $X_{0},X_{1},...,X{n}$ nos estados 0, 1, 2 tem matriz de probabilidade de transição e distribuição de probabilidade inicial:  
**Determine**: $P(X_{2}=2,X_{3}=0|X_{1}=0)$ "Determine a probabilidade de ir da posição 2 para posição 3 dado que inicia na posição 0 - $X_{1}$ não é a posição 1 é o tempo 1, '=0' que diz que qual é a posição"   
**Resposta:** $P(X_{2}=2,X_{3}=0|X_{1}=0) = P_{02}.P_{20}=0,7.0,1=0,07$  
<br>
## Teorema: (Equações de Chapman-Kolmogorv)  
A probabilidade de transição no n-ésimo passo para uma cadeia de Markov satisfaz:  
$P_{ij}^{n}=P(X_{m+n}=j|X_{m}=i)=\sum_{k=0}^{\infty}P_{ik}P_{kj}^{n-1}$  
onde definimos $P_{ij}^{0}= \delta = \begin{matrix} 1 & i=j \\ 0 & i \neq j \end{matrix}$  
<br>
### Exemplo
![](imagens/exemplo_Markov_3.png)  
<br>
## Video-Aula 2
Cadeia de Markov - Aula 2  
link: https://www.youtube.com/watch?v=0ymZ2Iv_9q8&list=PLSc7xcwCGNh0jSylDm0QrDJaFTC3vAbvc&index=3  
<br>
![](imagens/exemplo_Markov_4.png)  

## Estados da cadeia 
* Transientes 
* Recorrentes
* Absorventes

#### Perguntas que estamos inressados:
* Probabilidade de absorção:
    * Inciando em um vértice i, qual é a probabilidade de visitar um outro vértice j?
* Tempo média para absorção
    * Inciando em um vértice i, quanto passos, em média, são necessário para visitar o vértice j pela primeira vez?
* Número médio de visitas:
    * Inciando em um vértice i, quantas vissitas um vértice k vai receber antes de chegar em outro vérice j?

![](imagens/exemplo_Markov_Análise.png)  
* **Tempo médio até a absorção:**  
$T=min\{n \ge 0;X_{n}=0$ ou $X_{n}=2\}$
* **Probabilidade de absorção:**$P(X_{T}=0|X_{0}=1)=u$
* **Tempo médio até a absorção:** $E[T|X_{0}=1]=v$

### Análise do primeiro passo
$P(X_{T}=0|X_{0}=1)=u=?$

![](imagens/exemplo_Markov_Análise_2.png) 
![](imagens/exemplo_Markov_Análise_3.png)

 * **Tempo médio até a absorção:**  
$T=min\{n \ge 0;X_{n}=0$ ou $X_{n}=2\}$

$u=P(X_{T}=0|X_{0}=1)=\frac {P_{10}}{P_{10}+P_{P12}}=\frac {P_{10}}{1-P_{P11}}$
$E[T|X_{0}=1]=v=\frac {1}{1-P_{11}}$

![](imagens/exemplo_Markov_Analise_4.png)
![](imagens/exemplo_Markov_Analise_5.png)



## Video-Aula  4
Cadeia de Markov - Aula 4  
link: https://www.youtube.com/watch?v=_N9bZNTaMz8&list=PLSc7xcwCGNh0jSylDm0QrDJaFTC3vAbvc&index=5

#### Classificação de estados
* **Definição**: Um estado j é acessível pelo estado i se $P_{ij}^{n}>0$ para algun $n>0$
Assumimos que cada estado é acessível a si própio, $P_{ii}^{0}=1$
* **Definição**: Dois estados que são acessíveis um ao outro são ditos comunicantes: 
$i <->j:i$ e j se comunicam
* Além disso:
    * Se i <--> j, então j <--> i
    * Se i <--> j e j <--> k, então i <--> k (transitividade)
* Estados que se comunicam formam classes. 

![](imagens/classificacao_estados_1.png)


## Cadeias de Markov: o algoritmo PageRank
Cadeias de Markov: o algoritmo PageRank 
link: https://www.youtube.com/watch?v=iwraRlbubeQ&list=PLSc7xcwCGNh0jSylDm0QrDJaFTC3vAbvc&index=6

* **Ideia geral**
    * Mapear a web como uma cadeia de Markov e transforamar essa cadeia para que ela seja ergótica. 
    * Calcular a distribuição estacionária. 
    * A distribuição estacionária é o PageRank. 

* **Teorema:** Para uma cadeia de Markov **irredutível e aperiódica** com matriz de probabilidade de transição P, se existe uma distribuição estacionária, ela é univocamente determinada por: 
$\pi = \pi P$
onde $\pi _{j}\ge 0, \forall _{j}$ e $\sum _{j=1}^{N} \pi _{k} = 1$
$\pi _{i} = lim _{n \to  \infty} P(X_{n}=i|X_{0}=j)=lim _{n \to  \infty} P(X_{n}=i)$
<br>
* **Definição**: O rank de uma página i é definido por: 
$\pi _{i} = \sum _{j}A_{ji}\frac {\pi _{j}}{k _{j}out}$
para a k-ésima iteração:
$\pi _{i,k+1}=\sum _{j}A_{ji}A_{ji} \frac {\pi _{j,k}}{k _{j}out}$
Sendo
$\pi _{i,0} = \frac {1}{N}, i = 1,2,....,N$ 