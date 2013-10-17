from RPIO import PWM
import sys
import time

lastangle=-1

def normalize_angle(angle):
   if( angle >= 180):
      return 180
   elif( angle <= 0 ):
      return 0
   else:
      return angle

def angle2time(angle):
    if( angle >= 180):
      return 2360
    elif( angle <= 0 ):
      return 490
    else:
      return ((2360-490)/180*angle+490)
def diff(angle):
   if( lastangle == -1 ):
     return angle
   if( angle > lastangle ):
     return angle-lastangle
   elif( angle < lastangle):
     return lastangle-angle
   else:
     return 0

def set_angle(angle):
  servos = PWM.Servo()
  diff_angle=diff(angle)
  if( diff_angle <> 0 ):
    servos.set_servo(18,angle2time(angle))
    global lastangle
    lastangle=angle
    sleeptime=float((0.5/180)*diff_angle)
    if( sleeptime < 0.01):
      sleeptime=0.01
    print "sleeptime is "+str(sleeptime)
    print "diff_angle is "+str(diff_angle)
    time.sleep(0.5)
    servos.stop_servo(18)

set_angle(90)
paramcount = len(sys.argv)
for i in range(1,paramcount):
   print "Param"+str(i)+" is "+sys.argv[i]
   angle=normalize_angle(int(sys.argv[i]))
   set_angle(angle)
