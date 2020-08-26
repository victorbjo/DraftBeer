from smbus import SMBus
from datetime import datetime


addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

def sendToArd(coolers, temp):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        from smbus import SMBus
        f = open("test.txt", "a")
        f.write("0x01 "+coolers+" "+temp + " "+current_time+"\n")
        bus.write_byte(addr, 0x01)
        for x in range(8):        
                bus.write_byte(addr, int(ord(coolers[x])))
        bus.write_byte(addr, int(ord("0")))
        for i in range(2):
                bus.write_byte(addr, int(ord(temp[i])))
        bus.write_byte(addr, 0x01)
        f.close()
