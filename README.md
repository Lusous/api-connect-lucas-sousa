# API REST de Gerenciamento de Usuários

Projeto simples feito em Python com Flask para praticar os conceitos de API REST e CRUD.

## Funcionalidades

- Listar usuários
- Buscar usuário por ID
- Cadastrar usuário
- Atualizar usuário
- Excluir usuário
- Respostas em JSON
- Validação de nome e e-mail

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Rotas

- `GET /usuarios`
- `GET /usuarios/<id>`
- `POST /usuarios`
- `PUT /usuarios/<id>`
- `DELETE /usuarios/<id>`

## Exemplo de JSON para cadastro

```json
{
  "nome": "João",
  "email": "joao@email.com"
}
```
