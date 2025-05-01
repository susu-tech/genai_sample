import json
import uuid

import requests

url = "http://localhost:4000/rpc"

batch_payload = [
    {
        "jsonrpc": "2.0",
        "method": "add",
        "params": {"a": 10, "b": 20},
        "id": str(uuid.uuid4()),
    },
    {
        "jsonrpc": "2.0",
        "method": "add",
        "params": {"a": 5, "b": 7},
        "id": str(uuid.uuid4()),
    },
]

# リクエスト表示
print("Batch Request:")
print(json.dumps(batch_payload, indent=2))

response = requests.post(url, json=batch_payload)

# レスポンス表示
print("Batch Response:")
print(json.dumps(response.json(), indent=2))


# print(json.dumps(response.json(), indent=2))
