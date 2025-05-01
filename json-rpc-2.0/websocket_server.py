# server.py
import asyncio
import json

import websockets


async def handle_rpc(websocket):
    async for message in websocket:
        request = json.loads(message)
        print("Received:", request)

        if request.get("method") == "echo":
            response = {
                "jsonrpc": "2.0",
                "result": request["params"],
                "id": request["id"],
            }
        else:
            response = {
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": "Method not found"},
                "id": request["id"],
            }

        await websocket.send(json.dumps(response))


async def main():
    async with websockets.serve(handle_rpc, "localhost", 8765):
        print("WebSocket RPC Server started on ws://localhost:8765")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
