"""from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

fernet = Fernet(os.getenv("ENCRYPTION_KEY").encode("utf-8"))
enc = fernet.encrypt(os.getenv("OPENAI_API_KEY").encode("utf-8"))
print(enc.decode("utf-8"))
dec = fernet.decrypt(enc)

"""

# print("\n\n{dec}".format(dec=dec.decode("utf-8")))
# load_dotenv(dotenv_path=r"C:\Projects\ragas_eval\folder\.env")
from fastapi import WebSocket, WebSocketDisconnect, WebSocketException, FastAPI

app = FastAPI()


@app.websocket("/chat")
async def chat(web: WebSocket):
    await web.accept()
    try:
        while True:
            message = await web.receive_json()
            if "message" in message:
                k = 0
                for i in range(1, 1000):
                    k += 1
                    await web.send_json({"message": message["message"], "num": k})
            await web.send_json({"message": "Done"})
    except WebSocketDisconnect:
        print("client disconnected")
    except Exception as e:
        raise WebSocketException(code=1011, reason=str(e))
