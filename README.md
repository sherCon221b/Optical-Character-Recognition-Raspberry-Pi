# Optical Character Recognition
Implentation using Python + OpenCV + Pytesseract
## Hardware
* Raspberry pi 3b+ (may run on later versions)
* Raspi Cam
## Software
* OS - Raspbian GNU/Linux 10 (buster)
* Python 3.7.3, Pytesseract and OpenCV 3.4.6.27

Note: _Implementation is done with the information above. Issues may occur in other versions._
# Sofware Installation

## Free up Space
Given that the Raspberry OP is freshly installed with an OS, do the following: 
### Expand File Sytem
    sudo raspi-config
Go to _Advance Options_ and then select _A1_.
### Uninstall Unnecessary Applications
    sudo apt-get remove --purge libreoffice*
    sudo apt-get purge wolfram-engine
    sudo apt-get clean
    sudo apt-get autoremove

## Update Raspi OS
    sudo apt-get update && sudo apt-get upgrade

## OpenCV
### Install Dependencies
    sudo apt-get install build-essential cmake pkg-config
    sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    sudo apt-get install libxvidcore-dev libx264-dev
    sudo apt-get install libgtk2.0-dev libgtk-3-dev
    sudo apt-get install libatlas-base-dev gfortran
Reference - [link](https://pysource.com/2018/10/31/raspberry-pi-3-and-opencv-3-installation-tutorial/).

### Install Python 3 and Pip3
    sudo apt-get install python3-dev
    sudo apt-get install python3-pip

### Install Opencv
    sudo pip3 install opencv-python==3.4.6.27
Note: _Later version of OpenCV may not be supported by python 3.7.3_

## Pytesseract

### Install Tesseract Library
    sudo apt-get install tesseract-ocr
### Install the Command Line Tesseract Tool
    sudo apt-get install libtesseract-dev
### Install Pytesseract
    sudo pip3 install pytesseract

Reference - [link](https://maker.pro/raspberry-pi/tutorial/optical-character-recognizer-using-raspberry-pi-with-opencv-and-tesseract).
