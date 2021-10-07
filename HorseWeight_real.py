import requests

data = requests.get(
    url = "https://api.hypixel.net/player",
    params = {
        "key": "647213f6-bfa4-401d-9fd9-ec562f663d06",
        "uuid": "58dfc909be4a497b871ea13f636d37f0",
        "PROFILE_ID":{
        "profile_id": "58dfc909be4a497b871ea13f636d37f0",
        "cute_name": "papaya",
        "current": True,
        "last_save": 0,
        "raw":{},
        "items":{},
        "data": {}
    }
    }
).json()

a = open ("data", "w")
a.write(str(data))
a.close()