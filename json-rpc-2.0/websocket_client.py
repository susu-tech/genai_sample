# client.py
import asyncio
import json

import websockets


async def call_rpc():
    async with websockets.connect("ws://localhost:8765") as websocket:
        request = {
            "jsonrpc": "2.0",
            "method": "echo",
            "params": "Hello WebSocket JSON-RPC!",
            "id": 1,
        }
        await websocket.send(json.dumps(request))
        print("Request sent.")

        response = await websocket.recv()
        print("Response received:", json.loads(response))


if __name__ == "__main__":
    asyncio.run(call_rpc())
