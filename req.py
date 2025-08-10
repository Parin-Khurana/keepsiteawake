import time
import requests
from flask import Flask

URL = "https://parink.xyz"

app = Flask(__name__)

@app.route("/")
def home():
    return "I'm alive!", 200

def keep_awake():
    while True:
        try:
            r = requests.get(URL)
            print(f"Pinged {URL} - Status {r.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5 * 60)

if __name__ == "__main__":
    import threading
    threading.Thread(target=keep_awake, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
