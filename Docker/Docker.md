# Containers
## Docker
**Curso** - Docker para Desenvolvedores (com Docker Swarm e Kubernetes) - *Udemy* 
**Livro** - Descomplicando o Docker 

## Instalação
``
sudo apt-get remove docker docker-engine docker.io containerd runc 
sudo apt-get update 
sudo apt-get install  
    apt-transport-https ca-certificates curl gnupg  
    lsb-release 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg 
sudo apt-get update 
sudo apt-get install docker-ce docker-ce-cli containerd.io 
``