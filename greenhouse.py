from ds2g import TrackingService
from time import sleep
from config import ds2g_key

import RPi.GPIO as GPIO
import Adafruit_DHT
 
tracking = TrackingService(ds2g_key)
sensor_list = {
    'GH_S1': {
        'GPIO_Pin': 23,
        'Device': Adafruit_DHT.DHT11
    }
}

DHT_GH_S1=Adafruit_DHT.DHT11
GPIO_Pin_GH_S1=23

 
while True:
    sensor_data = []
    for sensor_name, sensor_properties in sensor_list.items():
        humidity, temperature = Adafruit_DHT.read_retry(sensor_properties['Device'], sensor_properties['GPIO_Pin'])
        if humidity is not None and temperature is not None:
            data = {
                'applicationKey': 'FoundersWeek2023',
                'type': sensor_name,
                'value': '{"humidity":"' + humidity + '", "temperature": "' + temperature + '"}'
            }
            sensor_data.append(data)
            print('Success: ' + sensor_name)
        else:
            print('Fail: ' + sensor_name)
    if len(sensor_data > 0):
        tracking.send_many_tracks(sensor_data)
        print('Data sent!')
    else:
        print('No Data!')
    sleep(10)

except KeyboardInterrupt:
	GPIO.cleanup()