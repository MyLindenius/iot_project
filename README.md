# Tutorial on building a Temperature and Humidity Sensor IoT

## Brief overview
This project makes it possible to monitor the humidity and temperature in a room. The project also have a visual warning depending on the temperature to alert the user that the temperature is outside wanted values. My name is My Lindenius (ml227kw) and this IoT device has been built as a project for the course [Introduction Applied Internet of Things](https://lnu.se/kurs/tillampad-internet-of-things-introduktion/distans-internationell-engelska-sommar/) at Linné university. This project would approximetly take 10 hours to complete having the solution available. Of course the time needed will also depend on prior knowledge and if any errors appear a long the way.

## Objective
I decided on this project as the data collected would be interesting and something that changes through out the day. This data is valuable for me as I have an animal with asthma, making it even more important to ensure proper humidity and temperature. This project can however also be valuable to anyone that want to ensure that their home has a good environment. I think this project will give an insight into how to build your own device that can communicate over the network and a nice introduction to the physical parts of a device.

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

The Raspberry Pi Pico WH is a controller with pre-soldered pins making it easy to use out of the box. The controlle also have WiFi functionalities making it perfect for IoT projects.
The DHT11 is a humidity and temperature sensor that is pre-calibrated and can measure with a accuracy of +-5 in humidity precentage and +-2 in temperature.
The RGB LED SMD is a module that allows the user to control what color is displayed.

## Computer setup
I have used Visual Studio Code with the extension PyMakr for this project.
Therefore the steps relating to uploading your code to the device will be based on the VS Code IDE.

### Firmware to Raspberry Pi Pico
For a detailed guide on how to get the Raspberry Pi Pico WH working, look at this [link](https://hackmd.io/@lnu-iot/rkFw7gao_).
To get the Raspberry Pi Pico WH to work, the first step is to download the correct firmware, can be found in the above link.
You will need to connect the Raspberry Pi Pico with a micro USB that can transfare data into a computer where you have the firmware downloaded.
Before connecting the USB A end, make sure to hold down the BOOTSEL key on the Raspberry Pi Pico.
This will result in a new drive opening on your computer which corresponds to the Raspberry Pi Pico's storage.
Now copy the downloaded firmware and paste it in the opened storage.
Wait until the Raspberry Pi Pico automatically disconnects, after that, plug out the USB A.
To start up the Raspberry Pi Pico the coming times, do NOT press the BOOTSEL key.
If you use Debian/Fedora based systems, type the following in to your terminal: sudo usermod -a -G dialout $USER

### Connect Raspberry Pi Pico to your VS Code
Now you can start programming the device. To do so, have the device connected to the computer where the code is written.
Open up the extension PyMakr, this extension should be displayed in the left side menu.
In the down left corner, there is a menu called "Devices", find your device in this list and hower it.
A lightning icon will be present named "Connect device", press that botton.
Now it will also be possible to press a icon of a terminal called "Create terminal", press this icon and a terminal connected to the Raspberry Pi Pico should open up.
You can try printing something in this terminal to double check that everything work as expected. Eg: print("Hello World!)

### Project file structure and uploading code.
Your_project_name
|-lib
| |-library.py
| |-keys.py
|-boot.py
|-main.py
|-... // other configuration files and folders

Keys.py will contain secret keys, make sure to not share this file.
The following [link](https://hackmd.io/@lnu-iot/B1T1_KM83) contains a step guide into how to create your project and how to upload your code to the Raspberry Pi Pico.


