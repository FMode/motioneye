#from __future__ import division
#import time

# Import the PCA9685 module.
import RPi.GPIO as GPIO
import datetime

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# power-down servo controller
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 0)
#time.sleep(.5)

# Initialise the PCA9685 using the default address (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths (450 total, 25 corresponds to 10 degrees)
servo_min = 0  # Min pulse length out of 4096
servo_max = 180  # Max pulse length out of 4096

vpos=90
hpos=90

_logging=None
def get_monitor_info(camera_id):
    if int(camera_id)==1:
        return ("<-> %d || %d"%(hpos,vpos))
    return ''

def get_action_commands(camera_config,action_commands,logging):
    global _logging
    _logging=logging
    camera_id = camera_config['@id']
    #print(action_commands)
    #logging.info("get_action_commands!!!")
    if camera_id==1: 
        action_commands['left']=left
        action_commands['right']=right
        action_commands['down']=down
        action_commands['up']=up
        action_commands['preset1']=preset1
        action_commands['preset2']=preset2
        
    #logging.info(camera_id)
    #logging.info(action_commands)
    return action_commands

def preset1(IOLoop):
    hpos=90
    vpos=90
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos

def preset2(IOLoop):
    hpos=90
    vpos=90
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos


def left(IOLoop):
    global hpos
    _logging.info("left %d" %(hpos))
    if ( hpos < servo_max ):
        hpos = hpos + 10
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos
    
    #GPIO.output(18, 0)
    #io_loop = IOLoop.instance()
    #io_loop.add_timeout(datetime.timedelta(milliseconds=500), power_off,io_loop)

def right(IOLoop):
    global hpos
    _logging.info("right %d" %(hpos))    
    if ( hpos > servo_min ):
        hpos = hpos - 10
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos
    
    #GPIO.output(18, 0)
    #io_loop = IOLoop.instance()
    #io_loop.add_timeout(datetime.timedelta(milliseconds=500), power_off,io_loop)

def down(IOLoop):
    global vpos
    _logging.info("down %d" %(vpos))
    if ( vpos < servo_max ):
        vpos = vpos + 10
        _logging.info(vpos)
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos
    
    #GPIO.output(18, 0)
    #io_loop = IOLoop.instance()
    #io_loop.add_timeout(datetime.timedelta(milliseconds=500), power_off,io_loop)

def up(IOLoop):
    global vpos
    _logging.info("up %d" %(vpos))
    if ( vpos > servo_min ):
        vpos = vpos - 10
    kit.servo[1].angle=hpos
    kit.servo[0].angle=vpos
    
    #GPIO.output(18, 0)
    #io_loop = IOLoop.instance()
    #io_loop.add_timeout(datetime.timedelta(milliseconds=500), power_off,io_loop)

def power_off(io_loop):
    GPIO.output(18, 1)
