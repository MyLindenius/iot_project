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
VARIABLE_LABEL_TEMP = keys.VARIABLE_LABEL_TEMP  # variable label to send
VARIABLE_LABEL_HUM = keys.VARIABLE_LABEL_HUM
DELAY = 64  # Delay in seconds

# Set PINs
led = Pin("LED", Pin.OUT) # Set the OUTPUT pin to on-board LED
sensor = dht.DHT11(Pin(16)) # Pin where temp and hum data 
red = PWM(Pin(11))
green = PWM(Pin(14))
blue = PWM(Pin(15))

red.freq(1000)
green.freq(1000)
blue.freq(1000)



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

# These are set to around 10% of max strenght
def update_color(temp_c):
    if temp_c < 18:
        set_color(0, 0, 6553)      # Blue
    elif temp_c < 24:
        set_color(6553, 0, 0)      # Green
    else:
        set_color(0, 6553, 0)      # Red


while True:
    led.on()  # turn LED on to signal success
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
        update_color(temp)
        led.off()
    except OSError as e:
        print("Failed to read from DHT11: ", e)
        led.off()  # turn LED off to signal failure

    returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL_TEMP, temp)
    returnValue = sendData(DEVICE_LABEL, VARIABLE_LABEL_HUM, hum)
    sleep(DELAY)


