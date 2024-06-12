Aplicação CRUD com autenticação de Usuários com JWT para processo seletivo vaga backend

Requisitos:
- Python 3

Como rodar no Windows:

1. Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-repositorio>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    ./.venv/Scripts/activate (PowerShell)
    .venv\Scripts\activate (CMD)
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    python app.py
    ```

## Exemplos com 'curl' (CMD)
1. Registrar Usuário
    ```bash
    curl -X POST http://127.0.0.1:5000/register -d "{\"email\":\"seu@email.com\", \"password\":\"sua_senha\"}" -H "Content-Type: application/json"
    ```

2. Login Usuário
    ```bash
    curl -X POST http://127.0.0.1:5000/login -d "{\"email\":\"seu@email.com\", \"password\":\"sua_senha\"}" -H "Content-Type: application/json"
    ```

3. Cadastrar Venda
    ```bash
    curl -X POST http://127.0.0.1:5000/sales -H "Authorization: Bearer seu_token_aqui" -H "Content-Type: application/json" -d "{\"nome_cliente\": \"nome\", \"produto\": \"nome_produto\", \"valor\": 1000, \"data_venda\": \"10-06-2024\"}"
    ```

3. Listar Vendas
    ```bash
    curl -X GET http://127.0.0.1:5000/sales -H "Authorization: Bearer seu_token_aqui" -H "Content-Type: application/json"
    ```

## Endpoints

### Autenticação

- `POST /register`: Registrar um novo usuário.
  - **Parâmetros de Entrada:**
    - `email` (string): O email do usuário.
    - `senha` (string): A senha do usuário.
  - **Retorno Esperado:**
    - Status 201: Usuário registrado com sucesso.
    - Status 400: Erro de validação (ex: email já registrado).

- `POST /login`: Login de um usuário.
  - **Parâmetros de Entrada:**
    - `email` (string): O email do usuário.
    - `senha` (string): A senha do usuário.
  - **Retorno Esperado:**
    - Status 200: Login bem-sucedido. Retorna um token de autenticação.
    - Status 401: Credenciais inválidas.

### Vendas

- `GET /sales`: Consultar todas as vendas.
  - **Parâmetros de Entrada:** Nenhum.
  - **Retorno Esperado:**
    - Status 200: Lista de todas as vendas.
      ```json
      [
        {
          "id": 1,
          "nome_cliente": "Cliente A",
          "produto": "Produto A",
          "valor": 100,
          "data_venda": "10-06-2023"
        },
        ...
      ]
      ```

- `POST /sales`: Adicionar uma nova venda.
  - **Parâmetros de Entrada:**
    - `nome_cliente` (string): Nome do cliente.
    - `produto` (string): Nome do produto.
    - `valor` (float): Valor da venda.
    - `data_venda` (string): Data da venda no formato dd-mm-yyyy.
  - **Retorno Esperado:**
    - Status 201: Venda criada com sucesso.
    - Status 400: Erro de validação.

- `PUT /sales/:id`: Editar uma venda existente.
  - **Parâmetros de Entrada:**
    - `id` (int): ID da venda a ser editada (no URL).
    - `nome_cliente` (string): Nome do cliente.
    - `produto` (string): Nome do produto.
    - `valor` (float): Valor da venda.
    - `data_venda` (string): Data da venda no formato dd-mm-yyyy.
  - **Retorno Esperado:**
    - Status 200: Venda atualizada com sucesso.
    - Status 404: Venda não encontrada.
    - Status 400: Erro de validação.

- `DELETE /sales/:id`: Excluir uma venda existente.
  - **Parâmetros de Entrada:**
    - `id` (int): ID da venda a ser excluída (no URL).
  - **Retorno Esperado:**
    - Status 200: Venda excluída com sucesso.
    - Status 404: Venda não encontrada.

### PDF

- `GET /sales/pdf?start_date=DD-MM-YYYY&end_date=DD-MM-YYYY`: Gerar um PDF contendo todas as vendas entre start_date e end_date.
  - **Parâmetros de Entrada:**
    - `start_date` (string): Data de início no formato dd-mm-yyyy.
    - `end_date` (string): Data de término no formato dd-mm-yyyy.
  - **Retorno Esperado:**
    - Status 200: PDF gerado com sucesso.
    - Status 400: Erro de validação (ex: data inválida).
    - Status 404: Nenhuma venda encontrada no período especificado.


## Tecnologias

- Flask
- SQLAlchemy
- JWT
- Reportlab

## Descrição do Projeto

Farei uma breve descrição do porquê das escolhas das tecnologias e escolhas arquitetônicas. Primeiramente, utilizei como ORM (Object Relational Mapper) o SQLAlchemy, que permitiu abstrair configurações e comandos que poderiam ser específicos para um determinado SGBD, tornando mais fácil uma possível alteração do banco, necessitando apenas de um update no driver. Para implementar a autenticação com JWT utilizei o Flask-JWT-Extended que simplifica esse processo sem sacrificar muito o controle sobre configuracões do JWT. Porém, uma desvantagem de se utilizar essa biblioteca é que ela pode ser descontinuada com o passar dos anos, podendo levar a problemas de manutenção e compatibilidade no longo prazo. Por último, para criar o PDF, utilizei a biblioteca Reportlab que é versátil, flexível e dá controle total sobre o layout e conteúdo.

No quesito de decisões arquitetônicas, utilizei a arquitetura em camadas. Não sei se no Python ela faz sentido, mas as dividi da seguinte forma:
- Modelos: aqui ficam as classes que são utilizadas no banco de dados e representam entidades
- Rotas: aqui ficam todas as rotas que são mapeadas para métodos
- Serviços: aqui fica a lógica de negócios e validação de atributos
- Repositórios: aqui fica a interação com o banco de dados que encapsulam as consultas e operações do banco

No quesito segurança e regras de negócio, fiz com que um usuário logado possa alterar vendas criadas por outros usuários, se isso acontecer, o user_id da venda também é atualizado. Além disso, fiz com que possam ser criadas duas vendas com inputs iguais. Essas e outras diretrizes podem ser modificadas facilmente se esse não for o comportamento desejado.

Além disso, uma abordagem com blueprints poderia ser recomendada para organizar as rotas de forma mais modular e escalável. No entanto, devido à falta de conhecimento avançado em Flask, optei por uma abordagem mais direta na definição das rotas.

Como o escopo desse projeto é pequeno só foram criados um arquivo para cada camada, porém ao ter mais entidades, o certo seria ter um arquivo para cada entidade, por exemplo:

- models/
  - user.py
  - sale.py
  - ...
- routes/
  - user_routes.py
  - sale_routes.py
  - ...
- services/
  - user_service.py
  - sale_service.py
  - ...
- repositories/
  - user_repository.py
  - sale_repository.py
  - ...

  Na questão de Error Handling, utilizei a criação de exceções personalizadas que são 'raised' pela camada de serviço, porém por não ter um conhecimento tão avançado de Flask, não achei que ficou bom, queria fazer o 'handle' delas no arquivo exceptions.py ao invés de no app.py.