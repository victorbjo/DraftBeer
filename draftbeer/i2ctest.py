from smbus import SMBus
 
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
numb = 1
 
print ("Enter 1 for ON or 0 for OFF")
while numb == 1:
 
        ledstate = input(">>>>   ")
        bus.write_byte(addr, 0x02)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x31)
        bus.write_byte(addr, 0x30)
        bus.write_byte(addr, 0x34)
        bus.write_byte(addr, 0x32)
        bus.write_byte(addr, 0x04)
