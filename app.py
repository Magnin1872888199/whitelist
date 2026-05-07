from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE = "whitelist.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({"users": []}, f)

def read():
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

@app.route("/get", methods=["GET"])
def get():
    return jsonify(read())

@app.route("/update", methods=["POST"])
def update():
    data = request.get_data(as_text=True).strip()

    if not data:
        return {"status": "error", "msg": "empty"}, 400

    db = read()

    if data not in db["users"]:
        db["users"].append(data)

    save(db)

    return {"status": "ok", "users": db["users"]}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
