#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import binascii
import array

SDI   = 16 # Yellow
RCLK  = 22 # Purple
SRCLK = 18 # Orange


segCode = [0x6f,0x7f,0x07,0x7d,0x6d,0x66,0x4f,0x5b,0x06,0x3f,0x00]



def print_msg():
    print 'Program is running...'
    print 'Please press Ctrl+C to end the program...'
 
def setup():
    GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)
 
def hc595_shift(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RCLK, GPIO.LOW)
 
def loop():
    #ee = 9 
   # while True :
        for i in range(0, len(segCode)):
            hc595_shift(segCode[i])
     #       print ee
            time.sleep(1)
      #      ee = ee -1 


def destroy():   #When program ending, the function is executed.
    GPIO.cleanup()
 
if __name__ == '__main__': #Program starting from here
    print_msg()
    setup()
    try:
        loop() 
    except KeyboardInterrupt: 
        destroy()
