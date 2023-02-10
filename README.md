```
   __  ___     _                   __    ______        __             __          _       
  /  |/  /_ __(_)__ _  _____ ___  / /_  /_  __/__ ____/ /  ___  ___  / /__  ___ _(_)__ ___
 / /|_/ / // / / _ \ |/ / -_) _ \/ __/   / / / -_) __/ _ \/ _ \/ _ \/ / _ \/ _ `/ / -_|_-<
/_/  /_/\_, /_/_//_/___/\__/_//_/\__/   /_/  \__/\__/_//_/_//_/\___/_/\___/\_, /_/\__/___/
       /___/                                                              /___/           
iot.embedded.ai.connectivity.training.solutions ==========================================

https://myduino.com
ariffin@myduino.com
```

# Myduino DIY IoT Kit Raspberry Pi Pico W

> Let's learn Internet of Things (IoT) using [CircuitPython](https://circuitpython.org/) with Raspberry Pi Pico W 😉

Hi there, thank you for purchasing [Basic IoT Kit Raspberry Pi Pico W](https://myduino.com/product/myd-055/). You are one step to the journey of Internet of Things 👍

# Introduction

Raspberry Pi Pico is a family of super affordable development board from [Raspberry Pi Foundation](https://www.raspberrypi.org/).

<p align="center"><img src="https://staging-assets.raspberrypi.com/static/hero-desktop-0be741ca0b96c13025520975475b902c.png" width="600"></p>

Currently, the family have two development boards, one without Wi-Fi connectivity known as Raspberry Pi Pico (1st) and the other with Wi-Fi connectivity, known as Raspberry Pi Pico W (3rd).

<p align="center"><a href="https://myduino.com/product/myd-055/"><img src="https://raw.githubusercontent.com/myinvent/Myduino-DIY-IoT-Kit-Raspberry-Pi-Pico-W/main/images/board/Pico-family.png" width="400"></a></p>

Both of the development boards also comes with pin header and without header. The one without Wi-Fi connectivity and header, known as Raspberry Pico WH (2nd). While, the one with Wi-Fi connectivity and header, known as Raspberry Pi Pico WH (4th).

The heart of the Raspberry Pi Pico is a microcontroller [RP2040](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html), the first ever microcontroller designed and developed by [Raspberry Pi Foundation](https://www.raspberrypi.org/).

<p align="center"><a href="https://myduino.com/product/myd-055/"><img src="https://www.raspberrypi.com/documentation/microcontrollers/images/rp2040.jpg" width="300"></a></p>

The microcontroller support range of programming language, such as [C, C++](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html) and Python using [MicroPython](https://micropython.org/download/) or [CircuitPython](https://circuitpython.org/downloads?q=pico) framework.

The features of Raspberry Pi Pico and Pico H include:
- RP2040 microcontroller chip.
- Dual-core Arm Cortex M0+ processor, flexible clock running up to 133 MHz.
- 264kB of SRAM, and 2MB of on-board flash memory.
- USB 1.1 with device and host support.
- Low-power sleep and dormant modes.
- Drag-and-drop programming using mass storage over USB.
- 26 × multi-function GPIO pins.
- 2 × SPI, 2 × I2C, 2 × UART, 3 × 12-bit ADC, 16 × controllable PWM channels.
- Accurate clock and timer on-chip.
- Temperature sensor.
- Accelerated floating-point libraries on-chip.
- 8 × Programmable I/O (PIO) state machines for custom peripheral support.

While Raspberry Pi Pico W and Pico WH with additional features of:
- Single-band 2.4GHz wireless interfaces (802.11n) using the Infineon CYW43439 on-board antenna.
- WPA3.
- Soft AP (access point) supporting up to four clients.

## Basic IoT Kit Raspberry Pi Pico W

To kickstart your IoT journey using Raspberry Pi Pico we will use Raspberry Pi Pico W, for the development boards, which comes with Wi-Fi for the Internet connectivity.

But Raspberry Pi Pico W alone are not able to help you begin the IoT journey. Therefore, we introduce you a [complete kit](https://myduino.com/product/myd-055/), to help you onboarding your IoT journey with Raspberry Pi.

<p align="center"><a href="https://myduino.com/product/myd-055/"><img src="https://raw.githubusercontent.com/myinvent/Myduino-DIY-IoT-Kit-Raspberry-Pi-Pico-W/main/images/board/Image-Kit.png" width="400"></a></p>

In this repository, we share CircuitPython example program to program the RP2040 microcontroller on the Raspberry Pi Pico W. The hands-on perform by lab exercises, from Lab 00 until Lab 16 with other 3 extra lab exercises interfacing with OLED display.

The learning curve of the lab, starts from the understanding of the CircuitPython modules and boards, control the output signal from the microcontroller, read the input from the sensors, lastly for the IoT exercises by experimenting data provisioning from Raspberry Pi Pico W using HTTP and MQTT with secure protocol to [Favoriot](https://platform.favoriot.com) IoT platform.

1. Lab 00 CircuitPython Pins and Modules
2. Lab 01 Digital Output Blink On-Board LED
3. Lab 02 Digital Output Blink An LED
4. Lab 03 Digital Output Traffic Light
5. Lab 04 Digital Output DC Motor
6. Lab 05 PWM Output LED Brightness
7. Lab 06 Digital Input Pushbutton
8. Lab 07 Analog Input Potentiometer
9. Lab 08 Analog Input LDR
10. Lab 09 DHT11 Sensor
11. Lab 10 Wi-Fi Connectivity
12. Lab 11 Favoriot HTTP
13. Lab 12 Favoriot HTTPS
14. Lab 13 Favoriot MQTT Publish
15. Lab 14 Favoriot MQTTS Publish
16. Lab 15 Favoriot MQTTS Subscribe RPC
17. Lab 16 Favoriot MQTT Publish Node-RED Subscribe
18. Lab Extra OLED Display SSD1306
19. Lab Extra OLED Display SSD1306 DHT11
20. Lab Extra OLED Display SSD1306 DHT11 Favoriot

Happy learning.

## Kickstart CircuitPython

[CircuitPython](https://circuitpython.org/) is a programming language designed to simplify experimenting and learning to code on low-cost microcontroller boards, developed and maintained by [Adafruit](https://www.adafruit.com/about).

Currently, CircuitPython supported more than 350 development board with ranges of microcontroller from Microchip, Espressif, Sony, etc. The firmware for each development boards can be download from [CircuitPython Download](https://circuitpython.org/downloads) page.

The latest version of CircuitPython firmware for Raspberry Pi Pico W is 8.0.0, can be download from the [CircuitPython Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) page.

Let's get started by learning from the inventor of this super awesome framework, [Adafruit - Welcome to CircuitPython!](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)

## Raspberry Pi Pico W Pinout

<p align="center"><img src="https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg" width="800"></p>

## References

- Raspberry Pi Pico W [Product Brief](https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf)
- Raspberry Pi Pico W [Datasheet](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)
- RP2040 Microcontroller [Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)