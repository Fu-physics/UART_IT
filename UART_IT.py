# run python code firstly, because python read the data from STM32 firstly.

import serial
import time
import random

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM11"

ser.open()

led = 0

while True:
    # ser.write(b'hello fu \n')
    for i in range(random.randint(1, 5)):
        readData = ser.readline()
        print(readData)
        time.sleep(0.2)
    print("---------")
    led += 1
    state = led % 2
    print(str(state).encode())
    ser.write(str(state).encode())
    print("--------------------------------------")
    time.sleep(1)


