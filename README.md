
# Manual de Inicialização

Os comandos a seguir deveram ser executados no local do arquivo onde foram instalados/clonados!


#### Comandos de criação de um ambiente virtual (opcional):

- Windows:

```
python -m venv nome_do_ambiente

nome_do_ambiente\Scripts\activate
```

- Linux:

```
python -m venv nome_do_ambiente

source nome_do_ambiente/bin/activate
```


#### Comando de Instalação das blibliotecas do projeto:

```
pip install -r requirements.txt
```


#### Comando de execução:
```
uvicorn main:app --reload
```


# Projeto1-Banco-Api
Objetivo principal:
    Criar uma API (Python) para acessar um banco de dados (PostegreSQL)


#### Blibliotecas:
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- Psycopg2-binary


#### Nota da versão 1.1: 

- Implementação de objetos (classes):
    - Empresas
    - Acessoria

- Implementação do cadastro (CREATE)


#### Nota da versão 1.2:

- Implementação da visualização (READ)


#### Nota da versão 1.3:

- Implementação da atualização (UPDATE)


#### Nota da versão 1.4:

- Implementação da remoção (REMOVE)
- Correção de bugs de versão 


#### Nota da versão 1.5:

- Implementação da comunicação com o banco de dados PostgreSQL  

#### Nota da versão 1.6:

- Implementação definitiva Banco -> API
- Correção na organização de arquivos


#### Nota da versão 1.7:

- Implementação do CRUD de acessorias
- Correção nas normas de escrita (padronização de código)
