#!/usr/bin/env python
import os
import asyncio
import random
import websockets
from pathlib import Path

async def talk(websocket, path):
    two_up = Path(__file__).resolve().parents[2]
    f = open(os.path.join(two_up,"logfile.txt"), "rb")
    tail_contents = tail(f,5)
    print(tail_contents)
    for i in range(0,len(tail_contents)):
        await websocket.send(str(tail_contents[i]))

    f.seek(0, os.SEEK_END)
    last_pos = f.tell()

    while True:
        f = open(os.path.join(two_up,"logfile.txt"), "r")
        f.seek(last_pos)
        newText = f.readline()
        if newText:
            #   something new
            await websocket.send(newText)
            last_pos = f.tell()
        await asyncio.sleep(random.random() * 3)

def tail(f, window=20):
    """Returns the last `window` lines of file `f` as a list.
    """
    if window == 0:
        return []

    BUFSIZ = 1024
    f.seek(0, 2)
    remaining_bytes = f.tell()
    size = window + 1
    block = -1
    data = []

    while size > 0 and remaining_bytes > 0:
        if remaining_bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            f.seek(block * BUFSIZ, 2)
            # read BUFFER
            bunch = f.read(BUFSIZ)
        else:
            # file too small, start from beginning
            f.seek(0, 0)
            # only read what was not read
            bunch = f.read(remaining_bytes)

        bunch = bunch.decode('utf-8')
        data.insert(0, bunch)
        size -= bunch.count('\n')
        remaining_bytes -= BUFSIZ
        block -= 1

    return ''.join(data).splitlines()[-window:]

start_server = websockets.serve(talk, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()