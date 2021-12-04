import asyncio
import websockets
import time
async def hello():
    async with websockets.connect("ws://localhost:8000/ws/test/",open_timeout=10,close_timeout=10) as websocket:
        try:
            await websocket.send(str(400))
            print("sent",400)
            while True:
                print()
                respons = await websocket.recv()
            
                print("received",respons)
                time.sleep(5)
                await websocket.send(str(int(respons)+1))
                print("Sent",int(respons)+1)
        except websockets.exceptions.ConnectionClosedError:
            print("Connection Closed")
            return	
asyncio.run(hello())