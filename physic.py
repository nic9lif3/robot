import requests, json, time


server = 'http://10.22.20.59:8080'

def check_wall():
    cm = '/remote/sonar'
    return json.loads(requests.get(server + cm).text)

def hieuchinh(d):
    reset_compass()
    degree=compass()
    degree=degree['degree'] + degree['minute'] / 60
    if degree>d:
        turn_right_degree(degree-d)
    elif degree<d:
        turn_left_degree(d-degree)

def go(d):
    run()
    degree = compass()
    t=time.clock()
    while(time.clock()-t<=1.2 and check_wall()['distance']>12):
        pass
    stop()
    degree=degree['degree'] + degree['minute'] / 60
    if d  > degree > d :
        hieuchinh(d)


def check_color():
    cm = '/remote/color'
    return json.loads(requests.get(server + cm).text)


def run():
    cm = '/remote/play'
    return json.loads(requests.get(server + cm).text)


def stop():
    cm = '/remote/pause'
    return json.loads(requests.get(server + cm).text)


def turn_left():
    pass


def turn_left_degree(d):
    change_speed_left(30)
    change_speed_right(30)
    reset_compass()
    degree = compass()
    rotate = 0
    previous_degree = degree['degree'] + degree['minute'] / 60
    current_degree = previous_degree

    while (rotate <= d):
        round_left()
        time.sleep(0.01)
        stop()
        print(rotate, current_degree)
        degree = compass()
        current_degree = degree['degree'] + degree['minute'] / 60
        if current_degree < previous_degree - 200:
            rotate += 360
        rotate += current_degree - previous_degree
        previous_degree = current_degree

    print(rotate, current_degree)
    change_speed_left(30)
    change_speed_right(30)

def turn_right_degree(d):
    change_speed_left(30)
    change_speed_right(30)
    reset_compass()
    degree = compass()
    rotate = 0
    previous_degree = degree['degree'] + degree['minute'] / 60
    current_degree = previous_degree

    while (rotate >= -d):
        round_right()
        time.sleep(0.01)
        stop()
        print(rotate, current_degree)
        degree = compass()
        current_degree = degree['degree'] + degree['minute'] / 60
        if current_degree > previous_degree + 200:
            rotate -= 360
        rotate += current_degree - previous_degree
        previous_degree = current_degree

    print(rotate, current_degree)
    change_speed_left(30)
    change_speed_right(30)


def back():
    cm = '/remote/back'
    return json.loads(requests.get(server + cm).text)


def round_left():
    cm = '/remote/left'
    return json.loads(requests.get(server + cm).text)


def round_right():
    cm = '/remote/right'
    return json.loads(requests.get(server + cm).text)


def get_color():
    cm = '/remote/color'
    return json.loads(requests.get(server + cm).text)


def compass():
    cm = '/remote/compass'
    return json.loads(requests.get(server + cm).text)


def reset_compass():
    cm = '/remote/reset_compass'
    return json.loads(requests.get(server + cm).text)


def change_speed(speed):
    cm = '/remote/change_spd'
    return json.loads(
        requests.post(server + cm, json.dumps({"speed": speed}), headers={'Content-type': 'application/json'}).text)


def change_speed_left(speed):
    cm = '/remote/change_spd_left'
    requests.post(server + cm, json.dumps({"speed": speed})).text
    return json.loads(
        requests.post(server + cm, json.dumps({"speed": speed}), headers={'Content-type': 'application/json'}).text)


def change_speed_right(speed):
    cm = '/remote/change_spd_right'
    return json.loads(
        requests.post(server + cm, json.dumps({"speed": speed}), headers={'Content-type': 'application/json'}).text)
