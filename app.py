from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE = "whitelist.json"

# garante arquivo sempre existente
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"users": []}, f)

def read_file():
    with open(FILE, "r") as f:
        return json.load(f)

def write_file(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/get", methods=["GET"])
def get():
    return jsonify(read_file())

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json(force=True)

    if not data or "users" not in data:
        return jsonify({"status": "error", "msg": "no users"}), 400

    write_file({"users": data["users"]})

    return jsonify({"status": "ok", "users": data["users"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
