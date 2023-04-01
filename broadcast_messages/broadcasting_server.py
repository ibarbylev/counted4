"""A more detailed look at the broadcast server using this description as an example:
https://websockets.readthedocs.io/en/stable/topics/broadcast.html#broadcasting-messages
 """

import asyncio
import websockets

CLIENTS = set()


async def handler(websocket):
    CLIENTS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)


async def broadcast(message):
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(message)
        except websockets.ConnectionClosed:
            CLIENTS.remove(websocket)


async def broadcast_messages():
    while True:
        await asyncio.sleep(1)
        message = ...  # your application logic goes here
        await broadcast(message)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await broadcast_messages()  # runs forever

if __name__ == "__main__":
    asyncio.run(main())
