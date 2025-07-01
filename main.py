# Import from libraries
import time
from machine import Pin
import socket
import network
import dht

# Set the OUTPUT pin to on-board LED
led = Pin("LED", Pin.OUT)


sensor = dht.DHT11(Pin(16))

time.sleep(2)

try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature:", temp, "°C")
    print("Humidity:", hum, "%")
    led.on()  # turn LED on to signal success
except OSError as e:
    print("Failed to read from DHT11: ", e)
    led.off()  # turn LED off to signal failure

# Runs forever
while True:
    led.on()              # Turn on LED
    time.sleep(0.2)       # Delay for 0.2 seconds
    led.off()             # Turn off LED
    time.sleep(1.0)       # Delay for 1.0 seconds
