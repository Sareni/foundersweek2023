from ds2g import TrackingService
from time import sleep
from config import ds2g_key
 
tracking = TrackingService(ds2g_key)
sensor_list = ['GH_S1']
 
while True:
    sensor_data = []
    for sensor in sensor_list:
        data = {
        'applicationKey': 'FoundersWeek2023',
        'type': sensor,
        'value': 1
        }
        sensor_data.append(data)
        print(sensor)
    tracking.send_many_tracks(sensor_data)
    print('Data sent!')
    sleep(60)