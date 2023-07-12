import requests
from django.conf import settings

def uploadtoS3():
    url = "http://127.0.0.1:8001/backupdata"
    # url = "https://portal.virtualtriage.ca/backupdata"

    payload={}
    files=[
    ('file',('db.json',open(str(settings.BASE_DIR) +'/db.json','rb'),'application/json'))
    ]
    headers = {}
    print("files==========",files)
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # print(response.json())
    print(response)
    print("Backup Successfully")