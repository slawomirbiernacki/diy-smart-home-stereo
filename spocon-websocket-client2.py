#!/usr/bin/env python

import asyncio
import websockets
import json
from amp_operations import *

async def consumer(message):
    print(message)
    #event = json.loads(message)["event"]
    #print('Received event: ', event)
    #if event == "contextChanged":
    #    print("Reacting to changed context")
    #    #powerOn()
    #    #time.sleep(3)
    #    sourceAUX()

    #if event == "inactiveSession":
    #    print("reacting to inactive session")
    sourceCD()

async def consumer_handler(websocket):
    async for message in websocket:
        await consumer(message)

async def hello():
    uri = "ws://192.168.0.41:24879/events"
    async with websockets.connect(uri) as websocket:
        await consumer_handler(websocket)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(hello())
