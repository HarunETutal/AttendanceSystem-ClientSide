# -*- author: Harun Emre Tutal -*-

from config import ROUTES
from controls.classes import Client, VCBridge

client = Client()
vcbridge = VCBridge()

def user_login(username, password, usertype):
    response = client.send(ROUTES["user_login"],
                           {"username":username,
                            "password":password,
                            "usertype":usertype},
                            "POST")
    
    print(response.json())
    print(response.status_code)
    

