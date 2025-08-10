import time
import requests

URL = "https://parink.xyz"

while True:
    try:
        response = requests.get(URL)
        print(f"Pinged {URL} - Status: {response.status_code}")
    except Exception as e:
        print(f"Error pinging site: {e}")
    
    time.sleep(5 * 60)
