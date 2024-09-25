import network
from machine import Pin
import espnow
import time


# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Define the MAC address of the receiving ESP32 (ESP32 B)
peer = b'\xecd\xc9\x90\xf0|'
esp.add_peer(peer)

# Create a function to send data when a button is pressed (optional)
button_pin = Pin(16, Pin.IN)


while True:
    if button_pin.value() == 1:
        message = "ledOn"
        print(f"Sending command : {message}")
        esp.send(peer, message)
    else:
        message = "ledOff"
        print(f"Sending command : {message}")
        esp.send(peer, message)
        
    time.sleep(0.3)