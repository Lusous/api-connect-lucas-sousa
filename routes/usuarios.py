from flask import Blueprint
from controllers.usuarios_controller import (
    listar_usuarios,
    buscar_usuario,
    cadastrar_usuario,
    atualizar_usuario,
    excluir_usuario
)

usuarios_bp = Blueprint("usuarios", __name__)

usuarios_bp.route("/usuarios", methods=["GET"])(listar_usuarios)
usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])(buscar_usuario)
usuarios_bp.route("/usuarios", methods=["POST"])(cadastrar_usuario)
usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])(atualizar_usuario)
usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])(excluir_usuario)
