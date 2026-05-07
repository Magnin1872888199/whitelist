from flask import Flask, request, jsonify

app = Flask(__name__)

# começa com lista vazia (importante)
whitelist = {"users": []}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

@app.route("/update", methods=["POST"])
def update():
    global whitelist

    data = request.get_json()

    if not data or "users" not in data:
        return jsonify({"status": "error", "msg": "no data"}), 400

    whitelist["users"] = data["users"]

    return jsonify({"status": "ok", "users": whitelist["users"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
