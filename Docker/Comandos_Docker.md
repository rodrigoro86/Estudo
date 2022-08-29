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

#### Copiar arquivo de fora do container para dentro 
`
docker cp <arquivo> nome_container:/<pasta> 
`