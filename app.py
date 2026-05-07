from flask import Flask, request, jsonify

app = Flask(__name__)

whitelist = {"users": ["joao", "maria"]}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(whitelist)

@app.route("/update", methods=["POST"])
def update():
    global whitelist
    whitelist = request.json
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
