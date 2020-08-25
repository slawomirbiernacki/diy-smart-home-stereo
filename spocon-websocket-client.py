import websocket
import json
from amp_operations import *

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)
    event = json.loads(message)["event"]
    print('Received event: ', event)
    if event == "contextChanged":
        print("Reacting to changed context")
        powerOn()
        powerOn()
        powerOn()
        #time.sleep(3)
        sourceAUX() 
        sourceAUX() 
        sourceAUX() 

    if event == "inactiveSession":
        print("reacting to inactive session")
        sourceCD()
        sourceCD()
        sourceCD()

def on_message_threaded(ws, message):
    thread.start_new_thread(on_message, (ws, message))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    #thread.start_new_thread(run, ())
    print("Listening...")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.0.41:24879/events",
    #ws = websocket.WebSocketApp("ws://192.168.0.41:8765",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
