# Instruções para rodar o projeto

## Instalar o Docker no Ubuntu:
  # Instale Pacotes de Pré-requisitos
  sudo apt-get install  curl apt-transport-https ca-certificates software-properties-common
  
  # Adicione os Repositórios do Docker
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt update
  apt-cache policy docker-ce
  
  # Rodar a instalação do docker
  sudo apt install docker-ce
  
  # Verificar Status do Docker
  sudo systemctl status docker
  
# Instalar o Docker Compose no Ubuntu:
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verificar se a instalação foi bem-sucedida
docker-compose --version

# Realizar o clone do projeto
git clone https://github.com/benicagit/advicehealth.git

# Buildar e subir as imagens docker:
Dentro da pasta raiz do projeto executar o comando:
sudo docker-compose up --build

 
  
