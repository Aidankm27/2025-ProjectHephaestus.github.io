# Project Hephaestus
A Crowd-Controlled E-Ink Picture Frame


# Project Description
This is a network-connected digital photo frame that allows people to remotely upload images or short messages in real-time. This project will allow people to upload photos from anywhere in the world utilizing a web interface, a small file share server, and an E-ink display with a Raspberry-Pi to handle all computing.
We decided to use an E-ink display for this project to avoid issues commonly seen in classic LED-based digital displays. This allows for efficient power management and a unique aesthetic touch using Floyd-Steinberg dithering. 
We chose to utilize Rocky Linux as our server OS because its dedicated purpose doesn't require extra applications commonly installed on other linux distributions, allowing granular control over the specific modules needed for this project without sacrificing overhead resources.
The Raspberry Pi is a lightweight computer interface that allows us to handle the communication between the display and the file server.


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
* Apache Web and File Server  -  Hosts the web interface and handles the php for uploading images to the FileServer, hosts an SMB share for the uploaded images to be transferred to the Raspberry Pi
* Raspberry PI  -  Retrieves the image from the FileServer, applies Floyd-Steinberg dithering, and directs it to the E-Ink display board.

# Usage Instructions
Users can interact with this photo frame via a webpage hosted on the internet. They will be required to login with an access password and input a username before uploading photos. The webpage will be accessible via a QR code and/or a public domain name through a browser. Users will be able to upload a chosen image to the file server for dithering/resolution correction, the images will then be rotated via the RPi every X amount of time. 

# Project Update
*Challenges:*
In the past two weeks, we've encountered some challenges regarding internet access to our webpage through the VIU Wi-Fi, which may complicate our demonstration at the project fair. To address this, we are considering a few solutions. One option is to set up a hidden Wi-Fi network, allowing fair attendees to connect locally and access our webpage for image uploads. Another solution involves requesting the opening of a port to allow network traffic on the day of the fair; we plan to discuss this in more detail next week as we prepare for the event.  

Additionally, we’ve identified a concern regarding the power requirements of the Raspberry Pi and the E-Ink display. Our current battery may not provide enough charge or voltage to power both components simultaneously. To mitigate this issue, we’ll most likely power the project via a wired connection during the fair to ensure stability.

*Achievements:*
We’ve successfully uploaded and displayed our first custom images on the E-Ink screen. Furthermore, we have tested our local Wi-Fi connection to the webpage and confirmed that the image upload functionality to the file server is working as expected.

![image](https://github.com/user-attachments/assets/a263554f-1ee1-4cb1-9036-e60bd59d89d5)


*Poster Draft*

![image](https://github.com/user-attachments/assets/ac934078-3705-46fb-83bc-ad200e5a6803)




# What's Next  
In the next two weeks, we will focus on refining the user experience, particularly by developing an admin interface that will allow us to manage and assign images to the frame. This will also enable us to exercise some control over what is displayed, which is essential for our preparation ahead of the project fair.
