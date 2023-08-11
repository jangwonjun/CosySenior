import serial
import time
from env import ARDUINO

'''
class measure_arduino():
    def __init__():
        
            try:
                serial_port = ARDUINO.SER
                ser = serial.Serial(serial_port, 9600, timeout=1)
                print("Arduino Start")
                while True:
                    ser.write(b'r')  
                    value = ser.readline().decode().strip()  
                    if value.isdigit():  
                        sensorValue = int(value)
                        #print("화재 감지 이상 여부:", sensorValue)
                    else:
                        print("System:", value)
                    
                    time.sleep(1) 

            except KeyboardInterrupt:
                pass

            ser.close()
'''
