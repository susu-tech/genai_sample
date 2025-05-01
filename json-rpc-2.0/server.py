# server.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/rpc", methods=["POST"])
def rpc():
    req = request.get_json()
    method = req.get("method")
    params = req.get("params", {})
    id = req.get("id")

    # メソッド処理（ここでは add メソッドのみ）
    if method == "add":
        result = params["a"] + params["b"]
        response = {
            "jsonrpc": "2.0",
            "result": result,
            "id": id,
        }
    else:
        response = {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
            "id": id,
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(port=4000)
