# server.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/rpc", methods=["POST"])
def rpc():
    req = request.get_json()

    if isinstance(req, list):
        # バッチリクエストの場合
        responses = [handle_single_request(single_req) for single_req in req]
        return jsonify(responses)
    else:
        # 単一リクエストの場合
        response = handle_single_request(req)
        return jsonify(response)


def handle_single_request(req):
    method = req.get("method")
    params = req.get("params", {})
    id = req.get("id")

    # メソッド処理（ここでは add メソッドのみ）
    if method == "add":
        result = params["a"] + params["b"]
        return {
            "jsonrpc": "2.0",
            "result": result,
            "id": id,
        }
    else:
        return {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
            "id": id,
        }


if __name__ == "__main__":
    app.run(port=4000, debug=True)
