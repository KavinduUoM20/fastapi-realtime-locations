import asyncio
import fastapi
import websockets
import random
import json

async def send_location():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        for i in range(1000):
            location_data = {
                "latitude": round(random.uniform(37.531, 37.63), 6),
                "longitude": round(random.uniform(45.043, 45.060), 6),
            }
            await websocket.send(json.dumps(location_data))
            print(f"Sent location: {location_data}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(send_location())