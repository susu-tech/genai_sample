import asyncio
import datetime

import websockets

connected_clients = set()


async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            reply = f"Echo: {message}"
            await websocket.send(reply)
    finally:
        connected_clients.remove(websocket)


async def broadcast_announcement():
    while True:
        await asyncio.sleep(10)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        announcement = f"[Server] Announcement at {now}"
        if connected_clients:
            await asyncio.wait(
                [client.send(announcement) for client in connected_clients]
            )


async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    await asyncio.gather(server.wait_closed(), broadcast_announcement())


asyncio.run(main())
