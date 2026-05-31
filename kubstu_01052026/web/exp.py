import requests
import time

s = requests.Session() 
s.cookies['session'] = "eyJ1c2VyX2lkIjoxMDIsInVzZXJuYW1lIjoiYSJ9.afRjHw.UUmdfrufo5EgtweblLdYx5mxSMo"
s.cookies['web_session'] = "ab59b291cc3af8ac"

def get_likes():
    return s.get('http://155.XXX.XXX.XXX/api/likes')

def get_time():
    return s.get('http://155.XXX.XXX.XXX/api/timer')

def set_val(n):
    payload = {"bet":n}
    return s.post("http://155.XXX.XXX.XXX/api/bet", json=payload)



print(get_likes().status_code)
print(get_likes().json())
print(get_time().json())

get_time().json()

while (get_time().json()['remaining'] > 10.0):
    time.sleep(3)
    print(get_time().json())
    print(get_likes().json()['count'])

while (get_time().json()['remaining'] < 10.0):
    #follow the obvious actions by means of get_likes() and set_val()



