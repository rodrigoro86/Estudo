# Comandos Docker

#### Roda o ubuntu de forma interativa  
`
docker run –ti ubuntu  
`
#### Exibe quais container estão sendo executados no momento  
`
docker ps ou docker container ls  
`
#### Mostra os container que não estão rodando 
`
docker ps –a  
`
#### Atalho CTRL+P+Q sai do container sem fechar 
`
exit 
`
#### Utilizando o –d roda o container em background 
`
docker run –d  nginx 
`
#### Pausa o container  
`
docker stop nomeContainer 
`
#### -p -> compartilha a porta, porta 80 da máquina para 80 do containerx 
` 
docker –run –d –p 80:80 nginx  
`
#### ParaR Container 
Pode para o container com o comando docker stop <nome ou ID>  
`
docker stop <nome ou ID> 
`
#### IniciaR container 
`
docker start <ID> 
` 
#### Defini um nome para o container  

Flag –name  

#### Consulta os logs  
`
docker logs <ID ou Nome> 
`
`
docker logs <id ou nome> -f  
` 
#### Remove containers 
`
docker –rm < id ou nome>  
`
`
docker –rm -f <id ou nome> 
`
Flag –f força a remoção  
#### Removendo imagens
`
docker rmi <imagem> 
`
`
docker rmi –f  <id_imagem> 
`
#### Remove imagens, containers e networks não utilizados 
`
docker system prune 
`
#### Removendo container após utilizar  
`
docker run –rm <container> 
`
--rm executa o conteiner e depois remove  

#### Copiar arquivo de fora do container para dentro 
`
docker cp <arquivo> nome_container:/<pasta> 
`
#### Copiando arquivos do container  
`
docker cp  
`
Pode ser utilizado para copiar um arquivo de um diretório para um container 
Ou de um container para um diretório determinado  
`
docker cp nome_container:/<pasta> ./<pasta> 
`
#### Verificar informações de processamento  
Para verificar dados de execução de um container utilzamos:
`
docker top <container>  
`
Desta maneira temos acesso a quando ele foi iniciado, id do processo, descrição do comando CMD;  

#### Verificar dados de um container  
Para verificar diversas informações como: id, data de criação, imagem e muito mais  
`
docker inspect <container>  
`
#### Verificar processamento  
Para verificar os processos que estão sendo executados em um container, utilzamos o comando 
`
docker stats 
`  
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
# docker run /dir/data:/data 
`
#### Listando todos os volumes  
`
docker volume ls  
`
#### Inspecionamdo  o Volume  
`
docker volume inspect nome 
`
#### Removendo Volumes  
`
docker volume rm <nome> 
`
#### Remoção de volumes em massa  
`
docker volume prune 
`
#### Volume apenas de Leitura 
`
docker run –v volume;/data:ro 
`  
Este ro é abreviação de read only 

 