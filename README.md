# API de Livros (Flask)

## 1. Objetivo

API REST simples em Flask para gerenciar uma lista de itens (livros/jogos). Permite **consultar**, **criar**, **editar** e **excluir** registros. Os dados ficam em memória, então são perdidos quando o servidor reinicia.

## 2. URL base

```
http://localhost:5000
```

## 3. Como rodar

```bash
pip install flask flask-cors
python app.py
```

O servidor sobe em `localhost:5000` com `debug=True`.

Para testar, use o Postman ou o `index.html` (front-end que acompanha o projeto). Se for usar o front abrindo o arquivo direto no navegador, adicione o CORS no `app.py`:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

## 4. Endpoints

| Método | Rota            | Descrição                         |
|--------|-----------------|-----------------------------------|
| GET    | `/livros`       | Lista todos os livros             |
| GET    | `/livros/<id>`  | Busca um livro pelo id            |
| POST   | `/livros`       | Cria um novo livro                |
| PUT    | `/livros/<id>`  | Edita um livro existente          |
| DELETE | `/livros/<id>`  | Exclui um livro pelo id           |

## 5. Recurso disponibilizado

Cada livro tem esta estrutura:

```json
{
  "id": 1,
  "Titulo": "Brawl Stars",
  "autor": "G.G.Engel"
}
```

| Campo    | Tipo   | Descrição                         |
|----------|--------|-----------------------------------|
| `id`     | inteiro | Identificador único do livro     |
| `Titulo` | texto  | Título (atenção ao **T** maiúsculo) |
| `autor`  | texto  | Autor                             |

## 6. Exemplos de uso

**Listar todos**

```
GET /livros
```

**Buscar um**

```
GET /livros/3
```

**Criar** (o `id` precisa ser enviado, a API não gera sozinha)

```
POST /livros
Content-Type: application/json

{ "id": 11, "Titulo": "Hollow Knight", "autor": "T. Knight" }
```

Retorna a lista completa com o novo item.

**Editar** (só os campos enviados são alterados)

```
PUT /livros/11
Content-Type: application/json

{ "autor": "Hornet" }
```

Retorna o livro atualizado.

**Excluir**

```
DELETE /livros/11
```

Retorna a lista completa sem o item removido.

## 7. Observações

- Os dados vivem na lista `livros` em memória, sem banco de dados.
- Corpo das requisições POST e PUT deve ser JSON.
- Pontos a melhorar: o GET por id retorna 404 já no primeiro item que não bate (o `return` está dentro do `for`), e PUT/DELETE não tratam id inexistente.
