#demo program to learn how otp works
import random
import requests
import json

def otp():
    list1=''
    for i in range(6):
        val=str(random.randint(0,9))
        list1+=val
    return list1   
new_otp=otp()  

def send_otp(new_otp):
    tokens = {
        'Authorization': 'Bearer ed529e9487b2498194880e9b5e68e304',
        'Content-Type': 'application/json'
    }

    data = {
        "from": "447520651219",
        "to": ["919546610073"],
        "body": f"your otp is {new_otp}"
    }

    id='b835c687edb642198f1595d160482245'
    url = f'https://sms.api.sinch.com/xms/v1/{id}/batches'

    requests.post(url, headers=tokens, data=json.dumps(data))


check_otp=input('enter the otp send on the your phone')
send_otp(new_otp)
if check_otp==otp():
    print('Authenticated')
else:
    print('error')
