import gc,utime

import pyb, micropython,LPF2Class

adc = pyb.ADC('X6') # set up analog pin

micropython.alloc_emergency_exception_buf(200)  # shows errors


red_led=pyb.LED(1)
red_led.on()


lpf2 = LPF2Class.LPF2(3, 'Y9', 'Y10', timer = 4, freq = 5)     # OpenMV UART #, Tx, Rx, callback timer, and timer frequency
lpf2.initialize()

# Loop
while True:

     if not lpf2.connected:
          lpf2.sendTimer.callback(None)   # clear any earlier 
          red_led.on()                    # tell user connecting
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()                   # signal connected
          lpf2.load_payload( int(adc.read()/500) ) # range of FSR should be 0-5000 mV, so divde by 500 to fit in the 0-9 digit range for SPIKE
          data = lpf2.readIt()

          utime.sleep_ms(200)