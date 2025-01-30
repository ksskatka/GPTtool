import requests
import sys
import json

def ping_server():
    try:
        response = requests.get("http://127.0.0.1:5000/ping")
        if response.status_code == 200:
            return {"status": "success", "response": response.json()}
        else:
            return {"status": "error", "code": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    result = ping_server()
    print(json.dumps(result))  # Output JSON for GPTScript
