# client.py
import json
import uuid

import requests

url = "http://localhost:4000/rpc"

# JSON-RPC リクエストの作成
payload = {
    "jsonrpc": "2.0",
    "method": "add",
    "params": {"a": 5, "b": 3},
    "id": str(uuid.uuid4()),
}

# リクエスト表示
print("Request:")
print(json.dumps(payload, indent=2))

# POSTリクエスト送信
response = requests.post(url, json=payload)

# レスポンス表示
print("Response:")
print(json.dumps(response.json(), indent=2))
