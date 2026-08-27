from flask import request, jsonify
from data.usuarios import usuarios

def listar_usuarios():
    return jsonify({"data": usuarios}), 200

def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify({"data": usuario}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404

def cadastrar_usuario():
    novo_usuario = request.get_json(silent=True)

    if not novo_usuario:
        return jsonify({"error": "Dados não enviados"}), 400

    if not novo_usuario.get("nome"):
        return jsonify({"error": "O campo nome é obrigatório"}), 400

    if not novo_usuario.get("email"):
        return jsonify({"error": "O campo email é obrigatório"}), 400

    novo_id = max([usuario["id"] for usuario in usuarios], default=0) + 1

    usuario = {
        "id": novo_id,
        "nome": novo_usuario["nome"],
        "email": novo_usuario["email"]
    }

    usuarios.append(usuario)

    return jsonify({"data": usuario}), 201

def atualizar_usuario(id):
    dados_novos = request.get_json(silent=True)

    if not dados_novos:
        return jsonify({"error": "Dados não enviados"}), 400

    if not dados_novos.get("nome"):
        return jsonify({"error": "O campo nome é obrigatório"}), 400

    if not dados_novos.get("email"):
        return jsonify({"error": "O campo email é obrigatório"}), 400

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados_novos["nome"]
            usuario["email"] = dados_novos["email"]
            return jsonify({"data": usuario}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404

def excluir_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return "", 204

    return jsonify({"error": "Usuário não encontrado"}), 404
