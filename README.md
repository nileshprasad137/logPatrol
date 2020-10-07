 # LogPatrol

Monitor logs from file to browser in realTime. Tail -f implementation in Python. (Without SubProcess). Solution is optimized for large files. In order to perform `tail -xf` operation on large files, I read the file in chunks of 1KB from bottom, until i find x lines.  

#### Concept

WebSockets

#### Requirements
Python 3.7+ 

#### Instructions to run:
Run `logwatch.py`  and open  `websocket_client.html` in browser. Add logs in `logfile.txt` and see the changes in browser.

#### LICENSE ##
[MIT](LICENSE)
