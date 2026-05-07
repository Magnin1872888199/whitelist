from flask import Flask, request, jsonify

app = Flask(__name__)

whitelist = {"users": []}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

@app.route("/update", methods=["POST"])
def update():
    global whitelist

    data = request.json

    # aceita string ou lista
    if isinstance(data, dict) and "users" in data:
        whitelist["users"] = data["users"]

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
