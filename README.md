# Tutorial on building a Temperature and Humidity Sensor IoT

## Brief overview
This project makes it possible to monitor the humidity and temperature in a room. The project also has a visual warning depending on the temperature to alert the user that the temperature is outside wanted values. My name is My Lindenius (ml227kw) and this IoT device has been built as a project for the course [Introduction Applied Internet of Things](https://lnu.se/kurs/tillampad-internet-of-things-introduktion/distans-internationell-engelska-sommar/) at Linné university. This project would approximately take 10 hours to complete having the solution available. Of course the time needed will also depend on prior knowledge and if any errors appear along the way.

At the very bottom of the README is a detailed overview of the assembled board for this project, which can be used as a reference to help recreate this project.

## Objective
I decided on this project as the data collected would be interesting and something that changes throughout the day. This data is valuable for me as I have an animal with asthma, making it even more important to ensure proper humidity and temperature. This project can however also be valuable to anyone that wants to ensure that their home has a good environment. I think this project will give an insight into how to build your own device that can communicate over the network and a nice introduction to the physical parts of a device.

## Material

| Item                 | Category       | Where                                                                 | Price  |
| -------------------- | -------------- | ------------------ | ------ |
| Raspberry Pi Pico WH  | Controller| [Elektrokit](https://www.electrokit.com/en/raspberry-pi-pico-wh)     | 99 SEK |
| DHT11                | Humidity and Temperature sensor         | [Elektrokit](https://www.electrokit.com/en/temp/fuktsensor-dht11)    | 39 SEK |
| RGB LED SMD          | LED Module     | [Elektrokit](https://www.electrokit.com/en/led-modul-rgb-smd)        | 23 SEK |
| Resistor 330 Ohm     | Resistor       | [Elektrokit](https://www.electrokit.com/en/motstand-kolfilm-0.25w-330ohm-330r) | 10 SEK |
| Resistor 10k Ohm     | Resistor       | [Elektrokit](https://www.electrokit.com/en/motstand-kolfilm-0.25w-10kohm-10k) | 10 SEK |
| Wires male/male      | Cables         | [Elektrokit](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hane/hane) | 55 SEK |
| Breadboard           | Board          | [Elektrokit](https://www.electrokit.com/en/kopplingsdack-840-anslutningar) | 69 SEK |

Total: 314 SEK

You will also need a USB A male to B micro.

<img src="/image/PICO-WH-HERO.webp" width="400" alt="Raspberry Pi Pico WH" />
The Raspberry Pi Pico WH is a controller with pre-soldered pins making it easy to use out of the box. The controller also has WiFi functionalities making it perfect for IoT projects.
<img src="/image/41016231.jpg" width="400" alt="Sensor DHT11" />
The DHT11 is a humidity and temperature sensor that is pre-calibrated and can measure with an accuracy of +-5 in humidity percentage and +-2 in temperature.
<img src="/image/41015716.jpg" width="400" alt="RGB LED SMD module" />
The RGB LED SMD is a module that allows the user to control what color is displayed.

## Computer setup
I have used Visual Studio Code with the extension PyMakr for this project.
Therefore the steps relating to uploading your code to the device will be based on the VS Code IDE.

### Firmware to Raspberry Pi Pico
For a detailed guide on how to get the Raspberry Pi Pico WH working, look at this [link](https://hackmd.io/@lnu-iot/rkFw7gao_).
To get the Raspberry Pi Pico WH to work, the first step is to download the correct firmware, which can be found in the above link.
You will need to connect the Raspberry Pi Pico with a micro USB that can transfer data into a computer where you have the firmware downloaded.
Before connecting the USB A end, make sure to hold down the BOOTSEL key on the Raspberry Pi Pico.
This will result in a new drive opening on your computer which corresponds to the Raspberry Pi Pico's storage.
Now copy the downloaded firmware and paste it in the opened storage.
Wait until the Raspberry Pi Pico automatically disconnects, after that, plug out the USB A.
To start up the Raspberry Pi Pico the coming times, do NOT press the BOOTSEL key.
If you use Debian/Fedora based systems, type the following in to your terminal: sudo usermod -a -G dialout $USER

### Connect Raspberry Pi Pico to your VS Code
Now you can start programming the device. To do so, have the device connected to the computer where the code is written.
Open up the extension PyMakr, this extension should be displayed in the left side menu.
In the down left corner, there is a menu called "Devices", find your device in this list and hover it.
A lightning icon will be present named "Connect device", press that button.
Now it will also be possible to press an icon of a terminal called "Create terminal", press this icon and a terminal connected to the Raspberry Pi Pico should open up.
You can try printing something in this terminal to double check that everything works as expected. Eg: print("Hello World!)

### Project file structure and uploading code.
```
Your_project_name
|-lib
|  |-library.py
|  |-keys.py
|-boot.py
|-main.py
|-... // other configuration files and folders
```

Keys.py will contain secret keys, make sure to not share this file.
The following [link](https://hackmd.io/@lnu-iot/B1T1_KM83) contains a step guide into how to create your project and how to upload your code to the Raspberry Pi Pico.

## Platform for Data Visualization
I used the platform Ubidots as it has a free plan that covers the needs for this project (displaying temperature and humidity).
Ubidots is a platform that requires no coding to get it to work, making it quick and easy to set up.
To scale this project further, a self hosted data visualization application would be a great opportunity.
An option that I looked into but decided not to use this time was TIG Stack.
TIG Stack consists of Telegraf, InfluxDB and Grafana.
This option would also be great if you want to save the data that you collect for more than 1 month without having to pay a premium.

## Code
For the code, there are three parts that are extra interesting to understand.

### Connect to the internet
```
def connect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your WiFi Credential
        while not wlan.isconnected() and wlan.status() >= 0:
            print(f" status: {wlan.status()}")
            sleep(1)
        print(f"status: {wlan.status()}")
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip
```

The above code connects to the local WiFi and will be assigned with an IP within the local IP range.

### Sensor for humidity and temperature
```
    led.on()
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {hum}%")
        update_color(temp)
```

The above code activates the sensor (DTH11 in this case) and calls built in functions to capture what the current temperature and humidity is.
The code also prints the information to the terminal and calls a function that updates the color of the RGB LED SMD module.

### Update color on RGB LED SMD
```
def update_color(temp_c):
    if temp_c < 18:
        set_color(0, 0, 6553)
    elif temp_c < 24:
        set_color(6553, 0, 0)
    else:
        set_color(0, 6553, 0)
```
The above code is a simple function that checks what the temperature is and based on that changes the color of the RGB LED SMD to either blue, green or red.


## Transmitting the data
I decided to send the data for every 64th seconds in the current code. 
This is a good amount for the finished project as higher accuracy is not needed.
This amount will result in 1440 data requests per day per measurement.
Since I use 2 measurements in this project, it would result in 2880 data requests a day, which is within the Ubidots limit of 4000 data requests a day.
While creating this project, it could instead be good to have the data being sent more often as it would allow for quicker debugging of when changes are made in the code base.
I had a 5 second delay between data being sent while coding.

This project used WiFi to send the data with the help of API calls.
The data was sent as JSON objects.

Using Wifi has some restrictions for the device.
The biggest drawback is that it consumes a lot of energy compared to other options such as BLE and LoRa.
It also has a shorter connection range than LoRa (but further than BLE).
Since this device is designed to be used inside the home, these drawbacks are fine. 
The device will be in range of the WiFi and at the same time also have access to power.

If long range and low battery consumption is important for you, it is better to look into using LoRa , however, LoRa comes with its own drawbacks such as higher risk of high latency.



## Presenting the data

<img src="/image/iot_res.PNG" width="600" alt="Visualization of humidity and temperature on platform" />
The platform displays a simple visualization of the humidity as a percentage of between 0 and 100.
The temperature is visualized as a thermostat.
Ubidots free plan will save the data for 1 month.


## Final product
<img src="/image/product.jpg" width="400" alt="Finished IoT device" />
Above is an image of the finished IoT device.
This project has been a good learning experience and I am happy with the outcome.

Some possible future improvements for this project would be the following:
* **Self-hosted database and platform for data visualization**  
This would increase the options of what can be done, it would also let the user store their data longer.
* **Adding a buzzer**  
This would make it so that instead of only having a visual aid of when the heat is to high, the user would also get a notification in the form of a sound. This can be done with a passive or active Piezo.
* **Own application for tablet**
It would be nice to create an application that can be run on a tablet or ipad, so that the tablet could be placed beside the device and give a fuller picture of what exactly the sensors have measured, without having to login to the Ubidots website.


## Recreate this project
Disclaimer: Always look at the user guide for the sensors that you use to ensure that the correct resistance, etc, is used.

Below is a more detailed image showing how the circuit is constructed.
<img src="/image/bread.PNG" width="600" alt="Breadboard construction" />

It is important to know that the exact components used for this project are not the same as in the breadboard visualization.
The DHT11 that is used in the project only has 3 pins, and not 4 as in the visualization.
The RGB LED SMD module used in this project also has different pin layouts compared to the one in the image.
It is therefore important to read the manual of which pins is what on the piece that you have to not destroy anything.
In this project, I have used 3 resistors of 330 Ohm for the RGB LED SMD module, I have also used 10k Ohm for the DTH11 sensor.
This is slightly higher than what these components require.

