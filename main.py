import serial
import time
import datetime as dt

ser = serial.Serial('/dev/ttyACM2')
ser.flushInput()

while True:
    try:
        data = []
        for i in range(0,2):
            ser_bytes = ser.readline()
            decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            data.append(decoded_bytes+" "+dt.datetime.now().strftime('%H:%M:%S'))

        with open("output.txt","a") as f:
            f.write(str(data)+'\n')
        time.sleep(120)
    except:
        print("Keyboard Interrupt")
        break
