import socket
import time
from sense_hat import SenseHat
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()
sense = SenseHat()

sense.clear((0, 255, 0))
sense.low_light = True

GAIN = 2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#client_socket.settimeout(1.0)
addr = ("X.X.X.X", 12001)

values = [0]*4

while True:
    # start = time.time()
    # Read all the ADC channel values in a list.
    for i in range(4):
        values[i] = (adc.read_adc(i, gain=GAIN))
   
    gyro = dict.values(sense.get_gyroscope())
    accelero = dict.values(sense.get_accelerometer())
    compass = (sense.get_compass())
    # end = time.time()
    message = "%i %i %i %i %.2f %.2f %.2f %.2f %.2f %.2f %.2f" %(values[0], values[1], values[2], values[3], gyro[0], accelero[0], gyro[1], accelero[1], gyro[2], accelero[2], compass)
    client_socket.sendto(message, addr)
    
    # print(end - start)

    #time.sleep(0.5)
	
        