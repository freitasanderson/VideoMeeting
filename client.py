import asyncio
import websockets
import cv2
import numpy as np
import base64

async def video_sender(uri):
    cap = cv2.VideoCapture(0)
    
    async with websockets.connect(uri) as websocket:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            frame_data = base64.b64encode(buffer).decode('utf-8')
            await websocket.send(frame_data)

            try:
                frame_data = await websocket.recv()
                img_bytes = base64.b64decode(frame_data)
                nparr = np.frombuffer(img_bytes, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                cv2.imshow('Video Recebido', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except websockets.ConnectionClosed:
                print("Conexão encerrada.")
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    server_ip = "192.168.15.18"  #IP da máquina do servidor
    uri = f"ws://{server_ip}:8000"
    asyncio.run(video_sender(uri))
