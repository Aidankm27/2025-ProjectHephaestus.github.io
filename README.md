# Project Hephaestus
A Crowd-Controlled E-Ink Picture Frame


# Project Description
This is a network-connected digital photo frame that allows people to remotely upload images or short messages in real-time. This project will allow people to upload photos from anywhere in the world utilizing a web interface, a small file share server, and an E-ink display with a Raspberry-Pi to handle all computing.
We decided to use an E-ink display for this project to avoid issues commonly seen in classic LED based digital displays. This allows for efficient power management and a unique aesthetic touch using floyd-steinberg dithering. 
We chose to utilize rocky linux as our server OS because its dedicated purpose doesnt require extra applications commonly installed on other linux distributions, allowing granular control over the specific modules needed for this project without sacrificing overhead resources.
The Raspberry Pi is a lighweight computer interface that allows us to handle the communication between the display and the file server.
![image](https://github.com/user-attachments/assets/167b96ef-71ba-4850-adc7-b4d46564c4d7)


# Group:
* Mikaela Knutson
* Joey Bueckert
* Aidan Maude

# Supplies
* E-Ink Display Board
* Raspberry Pi
* Battery
* Voltage Adapter
* Frame

# System Architecture
* Apache WebServer  -  Hosts the web interface and handles the php for uploading images to the FileServer.
* Apache FileServer  -  Hosts the FileServer that accepts images from the WebServer, processes them with dithering, formats the resolution to fit the frame, then sends the image to the RPi.
* Raspberry PI  -  Retrieves the image from the FileServer and directs it to the E-Ink display board.

# Usage Instructions
Users can interact with this photo frame via a webpage hosted on the internet. They will be required to login with an access password and input a username before uploading photos. The webpage will be accessible via a QR code and/or a public domain name through a browser. Users will be able to upload a chosen image to the file server for dithering/resolution correction, the images will then be rotated via the RPi every X amount of time. 
