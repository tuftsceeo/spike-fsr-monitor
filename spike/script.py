import hub,utime

hub.port.B.info()
# if info comes back with None - then you have to restart the microprocessor


while True:  
     try:
          value = hub.port.B.device.get()[0]
          hub.display.show(str(value))

          utime.sleep(0.1)

     except:
          utime.sleep(1)
