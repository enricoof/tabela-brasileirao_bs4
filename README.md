# Tabela do Campeonato Brasileiro 2024

## Sobre
Este projeto é uma automação para a coleta de dados por requests no site do UOL, no qual é extraído o nome do clube e os pontos. A coleta de dados é feita em segundos.

### Funcionalidades
- **DADOS COLETADOS:** Os dados coletados são adicionados ao arquivo "Brasileirão BS4" com a extensão ".csv"
- **ELEMENTO A SER PESQUISADO:** O time a ser pesquisado é pela div e pela classe "visible-sm" para acessar o valor. E para os pontos, foi necessário acessar primeiramente a tabela com a TAG "tbody" para que acessando-a fosse possível pegar os pontos pela TAG "tr", assim o valor dentro da tag é acessado.


## Inicio

Passo a passo para rodar a aplicação

### Pré-Requisitos

É necessário ter instalado em seu computador:
- Python 3.12.6

### Instalação

Siga abaixo para a instalação do projeto:

1. Clone o repositório:
```bash
git clone https://github.com/enricoof/teste-python.git
```
2. Crie um Ambiente Virtual (venv) e ative:
```bash
Windows: python -m venv venv
         venv/scripts/activate

Linux/Mac: python3 -m venv venv
           source venv/bin/activate
```

3. Instale as dependências necessárias após ativar a venv:
```bash
pip install -r requirements.txt
```

### Dependências
```bash
attrs==24.2.0
beautifulsoup4==4.12.3
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
h11==0.14.0
idna==3.10
numpy==2.1.1
outcome==1.3.0.post0
pandas==2.2.3
pycparser==2.22
PySocks==1.7.1
python-dateutil==2.9.0.post0
pytz==2024.2
requests==2.32.3
selenium==4.25.0
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
soupsieve==2.6
trio==0.26.2
trio-websocket==0.11.1
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
websocket-client==1.8.0
wsproto==1.2.0
```

## Uso 
Após todos os passos, é só rodar o projeto!

## Contato
Meu nome é Enrico Folheni

Linked In - [Meu perfil!](www.linkedin.com/in/enrico-folheni)
