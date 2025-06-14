from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Serve the current directory including Map.html
app.mount("/static", StaticFiles(directory="."), name="static")

active_connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()  # movement Device IOT
            location = json.loads(data)

            for connection in active_connections:
                await connection.send_json(location)  # dic
    except:
        pass
    finally:
        active_connections.remove(websocket)
