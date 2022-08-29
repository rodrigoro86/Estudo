# Containers
## Docker
**Curso** - Docker para Desenvolvedores (com Docker Swarm e Kubernetes) - *Udemy* 
**Livro** - Descomplicando o Docker 

## Instalação
`
sudo apt-get remove docker docker-engine docker.io containerd runc  
`   
`
sudo apt-get update  
`  
`
sudo apt-get install  
    apt-transport-https ca-certificates curl gnupg  
    lsb-release 
`  
`
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg 
`  
`
sudo apt-get update 
`  
`
sudo apt-get install docker-ce docker-ce-cli containerd.io 
`  
## Oque são Containers 
Um pacote de código que pode executar uma ação, por exemplo: rodar uma aplicação Node.js, PHP, Python ...  
Containers utilizam imagens para poderem ser executados;  
Múltiplos containers podem rodar juntos.  
#### Container X Imagem  
Imagem e Container são recursos fundamentais do Docker; 
Imagem é o "projeto" que será executado peo container, todas as instruções estarão declaradas nela; 
Container é o DOcker rodando alguma imagem, consequentemente executando algum código proposto por ela;  
O fluxo é: programamos uma imagem e a executamos por meio de um container;  
#### Container X VM  
Container é uma aplicação que serve para um determinado fim, não possui sistema operacional, seu tamanho é de alguns mbs; 
VM possui sistema operacional próprio, tamanho de gbs, pode executar diversas funções ao mesmo tempo;  
Container acabam gastando menos recursos para serem executados, por causa do seu uso específico;  
VMs gastam mais recursos, porém podem exercer mais funções;  

## Imagens
Imagens são originadas de arquivos que programamos para que o Docker crie uma estrutura que executa determinadas ações em containers; 
Elas contém informações como: imagens base, diretório base, comandos a serem executados, porta da aplicação e etc; , diretório base, co 
Ao rodar um container baseado na imagem, as instruções serão executadas em camadas; 
#### Criando uma Imagem  
Para criar uma imagem preisa de um arquivo Dockerfile em uma pasta que ficará o projeto; 
Este arquivo precisa de algumas instruções para poder ser executado  

**FROM:** imagem base;  

**WORKDIR:** diretório de aplicação;  

**EXPOSE:** porta da aplicação;  

**COPY:** quais arquivos precisam ser  copiados;   

#### Executando uma imagem  
Para executar a imagem primeiramente vamos precisar fazer o build;  
`
docker build <diretório da imagem>; 
`  
Depois utilizar o docker run <imagem> para executá-la;  

#### Lista as imagens da máquina
`
docker image ls  
`  
#### Alterando uma imagem  
Sempre que alteramos o código de uma imagem vamos precisar fazer o build novamente;  
Para o Docker é como se fosse uma imagem completamente nova;  
Após fazer o build vamos executá-la por o outro id único criada com docler run; 

### Camadas das imagens  
As imagens do Docker são divididas em camadas (layers); 
Cada instrução no Dockerfile representa uma layer; 
Quando algo é atualizado apenas as layers depois da linha atualizada são refeitas;  
O resto permanece em cache, tornando o build mais rápido;  

#### Download de imagens  
Podemos fazer o download de alguma imagem do hub e deixá-la disponível em nosso ambiente;  
Vamos utilizar o comando
`
docker pull <imagem>; 
`  
Desta maneira, caso se use em outro container, a imagem já estará pronta para ser utilizada; 

Todo comando no docker tem acesso a uma flag –help;  

Utilizando desta maneira, podemos ver todas as opções disponíveis nos comandos;  

Para relembrar algo ou executar uma tarefa diferente com o mesmo;  
`
docker run –help 
`   
Múltiplas aplicações, mesmo container  
Podemos incializar vários containers com a mesma imagem;  
As aplicações funcionarão em paralelo;  
Para testar isso, podemos determinar uma porta diferente para cada uma, e rodar no modo detached; 
Podemos nomear a imagem já na sua criação;  
`
docker build -t nome:tag . 
`  
