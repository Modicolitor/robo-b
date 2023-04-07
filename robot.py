from Raspi_MotorHAT import Raspi_MotorHAT

import atexit
from time import sleep

class Robot:
    def __init__(self, motorhat_addr=0x60):
        #setup the motorhat with the passed in adress
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        
        
        #get local variable for each motor
        self.left_motor = self._mh.getMotor(1)
        self.right_motor = self._mh.getMotor(2)
        
                
        #ensure the motors get stopped when the code exits 
        atexit.register(self.stop_motors)
    
    def convert_speed(self, speed):
        #choose the running mode
        mode = Raspi_MotorHAT.RELEASE 
        if speed>0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
            
        #Scale the speed
        output_speed = (abs(speed)* 255) // 100
        return mode, int(output_speed) 
    
    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)
    
    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)
        
    def straight(self, sec):
        self.set_left(80)
        self.set_right(80)
        sleep(sec)
        
    def turn_left(self, sec):
        self.set_left(20)
        self.set_right(80)
        sleep(sec)
    
    def turn_right(self, sec):
        self.set_left(80)
        self.set_right(20)
        sleep(sec)
        
    def spin_left(self, sec):
        self.set_left(-80)
        self.set_right(80)
        sleep(sec)
        
    def spin_right(self, sec):
        self.set_left(80)
        self.set_right(-80)
        sleep(sec)
    
    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)