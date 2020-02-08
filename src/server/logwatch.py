#!/usr/bin/env python
import os
import asyncio
import random
import websockets
from pathlib import Path

async def time(websocket, path):
    two_up = Path(__file__).resolve().parents[2]
    f = open(os.path.join(two_up,"logfile.txt"), "r")
    f.seek(0, os.SEEK_END)
    # contents = f.read()
    last_pos = f.tell()
    # await websocket.send(contents)
    while True:
        f = open(os.path.join(two_up,"logfile.txt"), "r")
        f.seek(last_pos)
        newText = f.readline()
        if newText!='':
            #   something new
            await websocket.send(newText)
            last_pos = f.tell()
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()