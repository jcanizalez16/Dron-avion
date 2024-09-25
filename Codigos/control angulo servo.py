from machine import Pin, ADC, PWM
import time

X = ADC(33)
Y = ADC(32)


servo1 = PWM(Pin(22))
servo1.freq(50)

servo2 = PWM(Pin(23))
servo2.freq(50)

X.atten(ADC.ATTN_11DB)
X.width(ADC.WIDTH_9BIT)
Y.atten(ADC.ATTN_11DB)
Y.width(ADC.WIDTH_9BIT)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin, angle):
    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5) 
    duty = int(interval_mapping(pulse_width, 0, 20, 0, 1023))     
    pin.duty(duty)

while True:
    val_X=X.read()
    val_Y=Y.read()
    
    vol_X=X.read_uv()
    
    
    
    val_servo1=(180-(val_X*180)/511)
    val_servo2=((val_X*180)/511)
    
    servo_write(servo1, val_servo1)
    servo_write(servo2, val_servo1)
    
    
    print(val_X, ",", val_Y, ",", val_servo1, ",", val_servo2, vol_X)
    time.sleep(0.3)