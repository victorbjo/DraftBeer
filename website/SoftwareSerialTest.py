import serial
ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 57600,
        timeout=1
)
counter=0
ser.flushInput()
ser.flushOutput()
count = 0

while True:
    ser.write(serial.to_bytes([0xff,0xff,0xfd,0x00,0xa,0x4,0x0,0x5,0x4,0xfe]))
    print(ser.read())
