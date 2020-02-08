#!/usr/bin/env python

import asyncio
import random
import websockets

async def time(websocket, path):
    f = open("logfile.txt", "r")
    contents = f.read()
    print(contents)
    last_pos = f.tell()
    print(last_pos)
    await websocket.send(contents)
    while True:
        f = open("logfile.txt", "r")
        f.seek(last_pos)
        newText = f.readline()
        if newText!='':
            #   something new
            await websocket.send(newText)
            last_pos = f.tell()
        # last_pos = f.tell()
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()