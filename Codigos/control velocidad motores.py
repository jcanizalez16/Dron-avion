from machine import Pin, PWM, ADC
import time
CM1=PWM(Pin(32, Pin.OUT))
CM1.freq(500)

CM2=PWM(Pin(33, Pin.OUT))
CM2.freq(500)

Pot= ADC(26)

Pot.atten(ADC.ATTN_11DB)
Pot.width(ADC.WIDTH_10BIT)

while True:
        read_Pot=Pot.read()
        CM1.duty(read_Pot)
        CM2.duty(read_Pot)
        print(read_Pot)
        time.sleep(0.3)