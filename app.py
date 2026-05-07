from flask import Flask, jsonify
import os

app = Flask(__name__)

whitelist = {"users": []}

# 📋 ver whitelist
@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

# ➕ atualizar whitelist (modo texto simples)
@app.route("/update", methods=["POST"])
def update():
    global whitelist

    try:
        data = ""
        # lê corpo puro
        from flask import request
        data = request.data.decode("utf-8").strip()

        if not data:
            return jsonify({"status": "error", "msg": "empty"}), 400

        # transforma em lista
        whitelist["users"] = [x for x in data.split(",") if x]

        return jsonify({"status": "ok", "users": whitelist["users"]})

    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
