from flask import Flask, request, jsonify

app = Flask(__name__)

# whitelist inicial
whitelist = {"users": []}

# 🔥 ver whitelist
@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

# 🔥 atualizar whitelist
@app.route("/update", methods=["POST"])
def update():
    global whitelist

    users = request.form.get("users")

    # bloqueia vazio (isso evita seu bug [""])
    if not users:
        return jsonify({"status": "error", "msg": "empty users"}), 400

    # limpa valores vazios
    clean_list = [u for u in users.split(",") if u.strip() != ""]

    whitelist["users"] = clean_list

    return jsonify({
        "status": "ok",
        "users": whitelist["users"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
