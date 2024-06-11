Aplicação CRUD com autenticação de Usuários com JWT para processo seletivo vaga backend

Requisitos:
- Python 3

Como rodar:

1. Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    ./venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    python app.py
    ```

## Endpoints

### Autenticação

- `POST /register`: Registrar um novo usuário.
- `POST /login`: Login de um usuário.

### Vendas

- `GET /sales`: Consultar todas as vendas.
- `POST /sales`: Adicionar uma nova venda.
- `PUT /sales/:id`: Editar uma venda existente.
- `DELETE /sales/:id`: Excluir uma venda existente.

### PDF

- `GET /sales/pdf?start_date=DD-MM-YYYY&end_date=DD-MM-YYYY`: Gerar um PDF contendo todas as vendas entre start_date e end_date.

## Tecnologias

- Flask
- SQLAlchemy
- JWT
- Reportlab