#este es el codigo de la placa que ira en el dron
import network
import espnow
from machine import Pin, PWM
import time
import ustruct

conec= Pin(2, Pin.OUT)

s1=13
s2=15
s3=12
s4=2

m1=22
m2=23
m3=32
m4=33

servo1=PWM(Pin(s1))
servo2=PWM(Pin(s2))
servo3=PWM(Pin(s3))
servo4=PWM(Pin(s4))

motor1=PWM(Pin(m1))
motor2=PWM(Pin(m2))
motor3=PWM(Pin(m3))
motor4=PWM(Pin(m4))

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
servo4.freq(50)

motor1.freq(500)
motor2.freq(500)
motor3.freq(500)
motor4.freq(500)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin, angle):
    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5) 
    duty = int(interval_mapping(pulse_width, 0, 20, 0, 1023))     
    pin.duty(duty)



servo_write(servo1, 90)
servo_write(servo2, 90)
servo_write(servo3, 90)
servo_write(servo4, 90)
    
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)



while True:
    _, msg = e.recv()
    if msg:
        
        msg1, msg2, msg3 = ustruct.unpack('iii', msg)
        
        
        msg1=(msg1*2)
        read_X=msg2
        read_Y=msg3
        
        print( "datos: ", msg1, msg2, msg3)
        
        val_servo1=(180-(msg2*180)/511)
        val_servo2=((msg2*180)/511)
        val_servo3=((msg2*180)/511)
        val_servo4=((msg3*180)/511)
        
        print(val_servo1, "/", val_servo2, "/", val_servo3, "/", val_servo4)
        
        servo_write(servo1, val_servo1)
        servo_write(servo2, val_servo2)
        servo_write(servo3, val_servo3)
        servo_write(servo4, val_servo4)
        
        motor1.duty(msg1)
        motor2.duty(msg1)
        motor3.duty(msg1)
        motor4.duty(msg1)
        
        
        time.sleep(0.3)
        
