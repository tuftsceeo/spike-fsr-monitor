import hub,utime, time

hub.port.B.info()
# if info comes back with None - then you have to restart the microprocessor

loopTime = 3
loopPosition = 0.0
max = 0
startTime = time.time()
while True:  
     try:
          loopPosition = loopPosition + time.time() - startTime
          startTime = time.time()
          value = hub.port.B.device.get()[0]
          print(value, float(loopPosition))
          if value >= max or loopPosition >= loopTime:
               max = value
               loopPosition = 0
          
          hub.display.show(str(max))
          utime.sleep(0.05)

     except:
          utime.sleep(0.5)