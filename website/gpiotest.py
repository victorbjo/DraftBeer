import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.OUT) # Set pin 10 to be an input
while True: # Run forever
    GPIO.output(10, GPIO.LOW)
    print("ok")
