import requests,json,time

server='http://10.22.20.59:8080'



def check_wall():
    cm = '/remote/sonar'
    return json.loads(requests.get(server+cm).text)

def run():
    cm = '/remote/play'
    return json.loads(requests.get(server+cm).text)

def stop():
    cm = '/remote/pause'
    return json.loads(requests.get(server + cm).text)

def turn_left():
    pass

def turn_right():
    pass

def back():
    cm='/remote/back'
    return json.loads(requests.get(server + cm).text)

def round_left():
    cm='/remote/left'
    return json.loads(requests.get(server + cm).text)

def round_right():
    cm='/remote/right'
    return json.loads(requests.get(server + cm).text)

def get_color():
    cm='/remote/color'
    return json.loads(requests.get(server + cm).text)

def compass():
    cm='/remote/compass'
    return json.loads(requests.get(server + cm).text)

def reset_compass():
    cm='/remote/reset_compass'
    return json.loads(requests.get(server + cm).text)

def change_speed(speed):
    cm='/remote/change_spd'
    return json.loads(requests.post(server + cm,json.dumps({"speed":speed})).text)

def chang_speed_left(speed):
    cm='/remote/change_spd_left'
    return json.loads(requests.post(server + cm,json.dumps({"speed":speed})).text)

def chang_speed_right(speed):
    cm='/remote/change_spd_right'
    return json.loads(requests.post(server + cm,json.dumps({"speed":speed})).text)