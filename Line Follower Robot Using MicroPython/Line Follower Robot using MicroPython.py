from machine import Pin, PWM
import time

# Define IR sensor pins
rightIR_Sensor = Pin(34, Pin.IN)
leftIR_Sensor = Pin(35, Pin.IN)

# Motor speed (PWM duty cycle)
MotorSpeed = 512  # PWM range in MicroPython is 0-1023[50%]

# Right motor pins
enableRightMotor = PWM(Pin(26))
rightMotorPin1 = Pin(14, Pin.OUT)
rightMotorPin2 = Pin(27, Pin.OUT)
enableRightMotor.freq(1000)

# Left motor pins
enableLeftMotor = PWM(Pin(25))
leftMotorPin1 = Pin(32, Pin.OUT)
leftMotorPin2 = Pin(33, Pin.OUT)
enableLeftMotor.freq(1000)

def move_forward():
    rightMotorPin1.value(1)
    rightMotorPin2.value(0)
    leftMotorPin1.value(1)
    leftMotorPin2.value(0)
    enableRightMotor.duty(MotorSpeed)
    enableLeftMotor.duty(MotorSpeed)

def move_left():
    rightMotorPin1.value(1)
    rightMotorPin2.value(0)
    leftMotorPin1.value(0)
    leftMotorPin2.value(0)  # Stop left motor
    enableRightMotor.duty(MotorSpeed)
    enableLeftMotor.duty(0)

def move_right():
    rightMotorPin1.value(0)
    rightMotorPin2.value(0)  # Stop right motor
    leftMotorPin1.value(1)
    leftMotorPin2.value(0)
    enableRightMotor.duty(0)
    enableLeftMotor.duty(MotorSpeed)

def stop_moving():
    rightMotorPin1.value(0)
    rightMotorPin2.value(0)
    leftMotorPin1.value(0)
    leftMotorPin2.value(0)
    enableRightMotor.duty(0)
    enableLeftMotor.duty(0)

while True:
    rightIR_SensorValue = rightIR_Sensor.value()
    leftIR_SensorValue = leftIR_Sensor.value()
    
    if rightIR_SensorValue == 0 and leftIR_SensorValue == 0:
        move_forward()
    elif rightIR_SensorValue == 0 and leftIR_SensorValue == 1:
        move_left()
    elif rightIR_SensorValue == 1 and leftIR_SensorValue == 0:
        move_right()
    else:
        stop_moving()
    
    time.sleep(0.1)  # Small delay to prevent rapid toggling
