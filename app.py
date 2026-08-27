from flask import Flask, jsonify
from routes.usuarios import usuarios_bp

app = Flask(__name__)
app.register_blueprint(usuarios_bp)

@app.route("/")
def inicio():
    return jsonify({"mensagem": "API funcionando"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
