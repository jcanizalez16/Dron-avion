#esta es la placa que ira en el control

import network
from machine import Pin, ADC
import espnow
import time
import ustruct



Pot=ADC(35)
X=ADC(33)
Y=ADC(32)


Pot.atten(ADC.ATTN_11DB)
Pot.width(ADC.WIDTH_10BIT)
X.atten(ADC.ATTN_11DB)
X.width(ADC.WIDTH_9BIT)
Y.atten(ADC.ATTN_11DB)
Y.width(ADC.WIDTH_9BIT)

sta = network.WLAN(network.STA_IF)  
sta.active(True)
sta.disconnect()

esp = espnow.ESPNow()
esp.active(True)

peer = b'\xd0\xefv\xf0\x10\xd0'
esp.add_peer(peer)

while True:
    read_Pot=Pot.read()
    read_X=X.read()
    read_Y=Y.read()
    
    msg1=read_Pot
    msg2=read_X
    msg3=read_Y
        
        
    data = ustruct.pack('iii', msg1, msg2, msg3,)
    esp.send(peer, data)
    print(msg1, msg2, msg3)
    

    time.sleep(0.3)