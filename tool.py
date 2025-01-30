import os
import requests

print(requests.get(os.getenv("url")).text)