import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url=f"http://universities.hipolabs.com/{word}")
        data=res.json()
        print(res)
        print(data)

loop()