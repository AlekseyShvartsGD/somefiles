from flask import Flask, request, Response

app = Flask(__name__)

DATA = {
    "date": "2026-09-07",
    "numbers": "01101100",
}


@app.route("/")
def index():
    return Response("Roblox Build Logic Server\nEndpoints: /Return_Date, /Return_Numbers", content_type="text/plain")


@app.route("/Return_Date", methods=["GET", "POST"])
def return_date():
    return Response(DATA["date"], content_type="text/plain")


@app.route("/Return_Numbers", methods=["GET", "POST"])
def return_numbers():
    return Response(DATA["numbers"], content_type="text/plain")


@app.route("/Post_Data", methods=["GET", "POST"])
def post_data():
    if request.method == "POST":
        return Response("Received: " + request.data.decode(), content_type="text/plain")
    return Response("Ready", content_type="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
