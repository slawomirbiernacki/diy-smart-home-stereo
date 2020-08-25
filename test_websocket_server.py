#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import time

async def hello(websocket, path):
    print("awaiting...")
    #name = await websocket.recv()
    #print(f"< {name}")

    greeting = '{"event":"contextChanged","username":"21wfzx6hm3lkm3fhplu5ff67i"}'
    #time.sleep(5)
    print("Sending")
    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "192.168.0.41", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
