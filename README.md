# Password Manager API

API REST para gerenciamento de senhas, desenvolvida em Python utilizando FastAPI, PostgreSQL, Pydantic e Cryptography.

O projeto tem como objetivo fornecer uma API simples para criação, consulta, atualização
e exclusão de credenciais armazenadas em um banco de dados PostgreSQL, utilizando criptografia
para proteger informações sensíveis.

## Tecnologias

* Python 3.12
* FastAPI
* PostgreSQL
* Pydantic
* Cryptography
* Uvicorn

## Estrutura do projeto

```text
.
├── db/
│   └── db.py
├── core/
│   ├── config.py
│   └── security.py
├── routes/
│   └── crud.py
├── main.py
└── requirements.txt
```

### `main.py`

Arquivo principal da aplicação.

É responsável por inicializar a aplicação FastAPI e registrar as rotas utilizadas pela API.

### `db/db.py`

Responsável pela configuração e conexão com o banco de dados PostgreSQL.

### `core/config.py`

Centraliza as configurações utilizadas pela aplicação, incluindo variáveis de ambiente
e outras configurações necessárias para o funcionamento do projeto.

### `core/security.py`

Contém a lógica relacionada à segurança e à criptografia das informações sensíveis armazenadas pela aplicação.

### `routes/crud.py`

Contém as rotas responsáveis pelas operações CRUD das credenciais.

## Funcionalidades

A API possui operações para:

* Criar credenciais
* Consultar credenciais
* Atualizar credenciais
* Excluir credenciais
* Persistir dados utilizando PostgreSQL
* Validar dados utilizando Pydantic
* Criptografar informações sensíveis utilizando Cryptography

## Requisitos

* Python 3.12 ou superior
* PostgreSQL
* pip

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

Crie um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

No Windows:

```powershell
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Configure as variáveis necessárias para conexão com o PostgreSQL e funcionamento da aplicação
de acordo com as configurações definidas em `core/config.py`.

Informações sensíveis, como credenciais do banco e chaves utilizadas pela aplicação, não devem ser armazenadas diretamente no código-fonte.

Caso seja utilizado um arquivo `.env`, ele deve ser adicionado ao `.gitignore`.

Exemplo:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

## Banco de dados

O projeto utiliza PostgreSQL para armazenar as informações das credenciais.

Crie um banco de dados PostgreSQL e configure os dados de conexão
de acordo com o que é esperado por `db/db.py` e `core/config.py`.

Exemplo:

```
CREATE DATABASE password_manager;
```

## Executando a aplicação

Inicie a aplicação utilizando Uvicorn:

```bash
uvicorn main:app --reload
```

O servidor ficará disponível por padrão em:

```text
http://127.0.0.1:8000
```

## Documentação da API

O FastAPI fornece documentação interativa automaticamente.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Endpoints

As operações CRUD estão concentradas em `routes/crud.py`.
A estrutura dos endpoints pode ser consultada diretamente pela documentação gerada pelo FastAPI em `/docs`.

## Segurança

Como o projeto trabalha com senhas e outras informações sensíveis, a segurança dos dados é uma parte fundamental da aplicação.

A biblioteca Cryptography é utilizada para proteger informações sensíveis antes de seu armazenamento.

Boas práticas importantes:

* Não armazenar senhas em texto puro.
* Não versionar chaves criptográficas.
* Não armazenar credenciais do banco diretamente no código.
* Utilizar variáveis de ambiente para informações sensíveis.
* Não registrar senhas em logs.
* Utilizar HTTPS em produção.
* Manter as dependências atualizadas.
* Proteger adequadamente a chave utilizada para criptografia.

A criptografia dos dados não substitui mecanismos de autenticação e autorização.
Em um ambiente de produção, esses mecanismos devem fazer parte da arquitetura da aplicação.

## Desenvolvimento

Durante o desenvolvimento, o servidor pode ser executado com:

```bash
uvicorn main:app --reload
```

O parâmetro `--reload` permite que o servidor seja reiniciado automaticamente
quando alterações no código forem detectadas.
Essa opção é destinada ao desenvolvimento e não deve ser utilizada como configuração de produção.

## Dependências

As dependências do projeto estão especificadas em:

```
requirements.txt
```

Para instalar ou atualizar as dependências:

```bash
pip install -r requirements.txt
```

## Objetivo

Este projeto foi desenvolvido para praticar conceitos de desenvolvimento backend utilizando Python, FastAPI e PostgreSQL,
além de trabalhar com validação de dados, operações CRUD, gerenciamento de configurações
e proteção de informações sensíveis.
