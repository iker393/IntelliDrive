import asyncio
import websockets
import random
import time


# creating a handler for each connection
async def handler(websocket, path):
    while True:
        message = str(random.randint(1, 100))
        await websocket.send(message)


start_server = websockets.serve(handler, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
