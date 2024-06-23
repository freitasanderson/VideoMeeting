import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            tasks = [client.send(message) for client in clients if client != websocket]
            if tasks:
                await asyncio.wait(tasks)
    except ConnectionClosed:
        print("Conexão fechada.")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "192.168.15.18", 8000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
