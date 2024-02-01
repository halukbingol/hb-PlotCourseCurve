from datetime import datetime


def get_time_stamp():
    now = datetime.now()
    # print("now =", now)
    return now.strftime("%Y-%m-%dT%H:%M")


a = get_time_stamp()
print(a)
