import json
import sys
from colorsys import rgb_to_hsv
from websockets.sync.client import connect

CIRCLE_ID = 3802
CIRCLE_TYPE = [32, 5]
DRAW_SCALE = 1

def hsvify(r, g, b):
    h, s, v = rgb_to_hsv(r / 255, g / 255, b / 255)
    hsv_string = f'{h * 360:.2f}a{s:.2f}a{v:.2f}a0a0'
    return hsv_string

def gddata(dict: dict):
    lis = []
    for key, val in dict.items():
        lis.append(f"{key},{val}")
    return ','.join(lis)

if len(sys.argv) <= 1:
    print(f"usage: main.py <json file>")
    exit(1)

with open(sys.argv[1], "r") as f:
    geo = json.load(f)
    if geo.get("shapes"):
        geo = geo["shapes"]

send = {
    "action": "ADD"
}
objects = []
width = geo[0]["data"][0]
height = geo[0]["data"][1]
for index, item in enumerate(geo):
    x = item["data"][0]
    y = item["data"][1]
    color = item["color"]
    if item["type"] not in CIRCLE_TYPE:
        print("not a circle, skipping...")
        continue
    (r, g, b, *_) = color
    hsv = hsvify(r, g, b)
    
    gd_data = gddata({
        "1": CIRCLE_ID, # object
        "2": x / DRAW_SCALE, # x
        "3": height - (y / DRAW_SCALE) - 1, # y
        "25": index, # z order
        "32": item["data"][2] / DRAW_SCALE / 8, # scale
        "21": 10, # color channel
        "22": 10, # color channel
        "41": 1, # color checked
        "42": 1,
        "43": hsv, # color
        "44": hsv,
    })
    
    objects.append(gd_data)
    print(gd_data)
    

send["objects"] = ";".join(objects)

send["objects"] += ";"

#print(send["objects"])

with connect("ws://localhost:1313") as websocket:
    websocket.send(json.dumps(send))
    message = websocket.recv()
    print(f"Received: {message}")