from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

DATA = {
    "numbers": [0, 1, 1, 0, 1, 1, 0, 0],
    "date": "2026-09-07",
    "status": "active",
}


@app.route("/")
def index():
    return jsonify({"message": "Roblox Build Logic Server", "endpoints": ["/Return_Date", "/Return_Numbers", "/Post_Data"]})


@app.route("/Return_Date", methods=["GET", "POST"])
def return_date():
    if request.method == "POST":
        received = urllib.parse.unquote(request.data.decode())
        return jsonify({"received": received, "date": DATA["date"]})
    return jsonify({"date": DATA["date"]})


@app.route("/Return_Numbers", methods=["GET", "POST"])
def return_numbers():
    if request.method == "POST":
        received = urllib.parse.unquote(request.data.decode())
        return jsonify({"received": received, "numbers": DATA["numbers"]})
    return jsonify({"numbers": DATA["numbers"]})


@app.route("/Post_Data", methods=["GET", "POST"])
def post_data():
    if request.method == "POST":
        received = urllib.parse.unquote(request.data.decode())
        parsed = dict(urllib.parse.parse_qsl(received))
        return jsonify({"received": parsed, "response": "Data received"})
    return jsonify({"status": "ready"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
