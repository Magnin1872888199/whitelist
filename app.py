from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE = "whitelist.json"

# cria arquivo se não existir
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"users": []}, f)

def load():
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/get", methods=["GET"])
def get():
    return jsonify(load())

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json(force=True)

    if "users" in data:
        save({"users": data["users"]})

    return jsonify({"status": "ok", "users": data.get("users", [])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
