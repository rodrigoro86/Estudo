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
## Volumes  
Uma forma prática de persistir dados em aplicação e não depender de containers para isso 
Todo dado criado por um container é salvo nele, quando o container é removido perdemos os dados  
Então precismaos dos volumes para gerenciar os dados e também conseguir fazer backups de forma mais simples 
### Tipos de Volumes  
**Anônimos** (anonymous): Diretórios criados pela flag –v, porém com um nome aleatório 
**Nomeados** (named): São volumes com nomes, podemos nos referir a estes facilmente e saber para que são utilizados no nosso ambiente 
**Bind mounts:** Uma forma de salvar dados na nossa máuina, sem o gerenciamento do Docker, informamos um diretório para este fim;  

#### Volume Anônimos  
`
docker run –v /data 
`  
`
docker volume ls -> mostra todos os volumes do ambiente 
`  
#### Volumes Nomeados  
`
docker run –v nomedovolume:/data 
`  
#### Bind mounts  
Bind mount também e um volume, porém ele fica em um diretório que nós especificamos 
Não cria volume, apenas aponta  
`
docker run /dir/data:/data 
`
Dessa forma o diretório /dir/data no nosso computador, será o volume deste container 
Bind mount não serve apenas para volumes  
Podemos utilizar esta técnica para atualização em tempo real do projeto  
Sem ter que refaer o build  a cada atualização 

#### Criar um volume 
`
docker volume create <nome> 
`
Desta maneira temos um named volume cirado, podemos atrelar a algum container na execução do mesmo 

### Redes 
As redes são criadas separadas do containers, como os volumes  
Além disso existem alguns drivers de rede 
#### Tipos de conexão  
**Externa:** conexão com uma API de um servidor remoto 
**Com o host:** comunicação com a máquina que está executando o Docker.
**Entre containers:** comunicação que utiliza o driver bridge e permite entre dois ou mais containers 

#### Tipos de Drivers 
**Bridge:** o mais comum e default do Docker, utilizado quando containers precisam se conectar  
**Host:** permite a conexão entre um container a máquina que está hosteando o Docler 
**Macvla:** permite a conexão a um conteiner por um MAC  
**None:** remo todas conexões de rede de um container  
**Plugins:** permite extensões de terceiros para criar outras redes.  
#### Listando networks  
`
docker network ls  
`
#### Criando redes 
` 
docker network create <nome>  
`  
Está rede será do tipo bridge  
`  
docker network create –d macvlan <nome> 
`  
Define o drive para mcvlan  
#### Removendo redes  
`
docker network rm <nome>  
`  
#### Removendo redes não utilizadas  
`
docker network prune 
`  
#### Instalando do Postman 
Vamos criar API para testar conexão entre containers  
Para isso vamos utilizar o software Postman, que é o mais utilizado do mercado ára desenvolvimento de APIs 
#### Conexão com o host  
- Conectar um container com o host do docker 
- Estabelecer uma conexão entre containers; 
- Duas imagens distintas rodando em containers separados que precisam se conectar para inserir um dado no anco  
#### Conectar container 
`
docker network connect <rede> <container> 
`  
#### Desconectar container  
`
docker network disconnect <rede> <container> 
`  
#### Inspecionando redes  
`
docker network inspect <none>  
`  
### Docker Compose  
Docker Compose é uma ferramenta para rodar múltiplos containers 
Teremos apenas um arquivo de configuração, que orquestra esta situação  
É uma forma de rodar múltiplos builds e runs com um comando  
Criando o primeiro Compose  
Primeiro criar uma arquivo chamado docker-compose.yml na raiz do projeto  
Este arquivo vai coordenar os containers e imagens, e possui algumas chaves muito utilizadas 
**Version:** versão do Compose 
**Services:** Containers/Serviços que vão rodar nossa aplicação  
**Volume:** Possível adição de volumes   