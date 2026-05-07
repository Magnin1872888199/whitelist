from flask import Flask, request, jsonify
import os

app = Flask(__name__)

whitelist = {"users": []}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

@app.route("/update", methods=["POST"])
def update():
    global whitelist

    data = request.form.get("users")

    if data:
        whitelist["users"] = data.split(",")

    return {"status": "ok", "users": whitelist["users"]}
    global whitelist

    data = request.get_json(force=True)

    if "users" in data:
        whitelist["users"] = data["users"]

    return jsonify({"status": "ok", "users": whitelist["users"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
