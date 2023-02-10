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

To kick-start your IoT journey using Raspberry Pi Pico we will use Raspberry Pi Pico W, for the development boards, which comes with Wi-Fi for the Internet connectivity.

But Raspberry Pi Pico W alone are not able to help you begin the IoT journey. Therefore, we introduce you a [complete kit](https://myduino.com/product/myd-055/), to help you onboarding your IoT journey with Raspberry Pi.

<p align="center"><a href="https://myduino.com/product/myd-055/"><img src="https://raw.githubusercontent.com/myinvent/Myduino-DIY-IoT-Kit-Raspberry-Pi-Pico-W/main/images/board/Image-Kit.png" width="300"></a></p>

In this repository, we share the example program for CircuitPython framework to program the RP2040 microcontroller on the Raspberry Pi Pico W, from Lab 00, which start with the understanding of the CircuitPython modules and boards until Lab 16, connecting Raspberry Pi Pico W using MQTT with secure protocol to [Favoriot](https://platform.favoriot.com) IoT platform.

Happy learning.

## Kickstart CircuitPython

[CircuitPython](https://circuitpython.org/) is a programming language designed to simplify experimenting and learning to code on low-cost microcontroller boards, developed and maintained by [Adafruit](https://www.adafruit.com/about).

Currently, CircuitPython supported more than 350 development board with ranges of microcontroller from Microchip, Espressif, Sony, etc. The firmware for each development boards can be download from [CircuitPython Download](https://circuitpython.org/downloads) page.

The latest version of CircuitPython firmware for Raspberry Pi Pico W is 8.0.0, can be download from the [CircuitPython Pico W](https://circuitpython.org/board/raspberry_pi_pico_w/) page.

Let's get started by learning from the inventor of this super awesome framework, [Adafruit - Welcome to CircuitPython!](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)

## References

- Raspberry Pi Pico W [Product Brief](https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf)
- Raspberry Pi Pico W [Datasheet](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)
- RP2040 Microcontroller [Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)