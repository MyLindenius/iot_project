# Import from libraries
import time
from machine import Pin, PWM
import socket
import network
import dht
import keys
from time import sleep
import urequests as requests


TOKEN = keys.TOKEN_UBIDDOTS # Ubidots token
DEVICE_LABEL = keys.DEVICE_LABEL # device label to send
VARIABLE_LABEL = keys.VARIABLE_LABEL  # variable label to send
DELAY = 5  # Delay in seconds

print("Test")

# Set PINs
led = Pin("LED", Pin.OUT) # Set the OUTPUT pin to on-board LED
sensor = dht.DHT11(Pin(16)) # Pin where temp and hum data 
red = PWM(Pin(11))
green = PWM(Pin(14))
blue = PWM(Pin(15))



# Builds the json to send the request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None
    

def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass


def set_color(r, g, b):
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)

# Example: change color based on temp
def update_color(temp_c):
    if temp_c < 18:
        # Cold - Blue
        set_color(0, 0, 1023)
    elif temp_c < 25:
        # Comfortable - Green
        set_color(1023, 0, 0)
    else:
        # Hot - Red
        set_color(0, 1023, 0)


while True:
    led.on()  # turn LED on to signal success
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
        update_color(temp)
        led.off()  # turn LED on to signal success
    except OSError as e:
        print("Failed to read from DHT11: ", e)
        led.off()  # turn LED off to signal failure

    #returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL, temp)
    sleep(DELAY)


