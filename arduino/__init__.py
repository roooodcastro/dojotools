import serial
import glob
import time

def find_arduino_usb():
    arduino_usb = glob.glob('/dev/ttyUSB*')
    if len(arduino_usb) == 0:
        arduino_usb = glob.glob('/dev/ttyACM*')[0]
    else:
        arduino_usb = arduino_usb[0]
    return arduino_usb

def send_message(test_fails, last=False):
    '''
    Sends a message to Arduino via serial
    '''
    color = {
        True: 'R',
        False: 'G',
    }
    
    arduino_usb = find_arduino_usb()
    serial.Serial.color = lambda self, tf: self.write(color[tf])


    arduino = serial.Serial(arduino_usb, 9600)
    #time.sleep(1)
    arduino.color(test_fails)
    
def send_time_up_message():
    arduino_usb = find_arduino_usb()
    arduino = serial.Serial(arduino_usb, 9600)
    arduino.write('T')
