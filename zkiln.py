!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")







Kc      #process constant
Kp      #proportional constant
Ki      #integral constant
Kd      #derivative constant
Iterm   #Integral term
Cex     #TempC external
Cpv     #TempC kiln
Csp     #TempC setpoint
er=list(0,0) #n-1,n-2 error values
win     #window length in seconds
omax    #output max value
omin    #output min value
imax    #Iterm max value
imin    #Iterm min value


pid(Csp,Cpv,Cex) returns seconds to fire
#steady state heat loss is proportional to insideC-outsideC
Cterm = Kc*(Cpv-Cex)/100.0    # /100 allows integer Kc, (100C=6 & 1000C=60)
Pterm = Kp*(er[0])*win/60.0   # /Kp * delta C/min
Iterm += Ki*(er[1])*win/60.0  # summation previous error * Ki
if Iterm < imin:              # Iterm limits: imin =? -imax
  Iterm = imin
elif Iterm > imax:
  Iterm = imax
Dterm = Kd*(er[1]-er[2])*win/60.0

output = (Cterm + Pterm + Iterm + Dterm)/100.0
if output > 1:
  output = 1
elif output < 0:
  output = 0

cycle_sec = output * win
return cycle_sec

#records and display
Kc,Kp,Ki,Kd
win
imax,imin
Iterm

#parent - records & display
Csp
Cpv
Cex
dt
RunId
segment
  id#
  target
  CperHr
  hold_sec
  time_remaining_(): return (target-Cpv)/CperHr
cycle_sec

class Kiln():

    #3 modes
        #Idle (armed?)
        #Run  (manual, auto)
        #Test (armed?, current?, thermocouple?)
    #Run 
        #heat
        #hold
        #cool


