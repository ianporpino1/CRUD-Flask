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

## Descrição do Projeto

Farei uma breve descrição do porquê das escolhas das tecnologias e escolhas arquitetônicas. Primeiramente, utilizei como ORM (Object Relational Mapper) o SQLAlchemy, que permitiu abstrair configurações e comandos que poderiam ser específicos para um determinado SGBD, tornando mais fácil uma possível alteração do banco, necessitando apenas de um update no driver. Para implementar a autenticação com JWT utilizei o Flask-JWT-Extended que simplifica esse processo sem sacrificar muito o controle sobre configuracões do JWT. Porém, uma desvantagem de se utilizar essa biblioteca é que ela pode ser descontinuada com o passar dos anos, podendo levar a problemas de manutenção e compatibilidade no longo prazo. Por último, para criar o PDF, utilizei a biblioteca Reportlab que é versátil, flexível e dá controle total sobre o layout e conteúdo.

No quesito de decisões arquitetônicas, utilizei a arquitetura em camadas. Não sei se no Python ela faz sentido, mas as dividi da seguinte forma:
- Modelos: aqui ficam as classes que são utilizadas no banco de dados e representam entidades
- Rotas: aqui ficam todas as rotas que são mapeadas para métodos
- Serviços: aqui fica a lógica de negócios e validação de atributos
- Repositórios: aqui fica a interação com o banco de dados que encapsulam as consultas e operações do banco

No quesito segurança e regras de negócio, fiz com que um usuário logado possa alterar vendas criadas por outros usuários, se isso acontecer o user_id da venda também é atualizado e, ao gerar o pdf só aparecerão as vendas cadastradas pelo usuário logado. Essas diretrizes podem ser modificadas facilmente se esse não for o comportamento esperado.

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