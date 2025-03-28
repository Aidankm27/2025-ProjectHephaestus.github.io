#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
import time
from PIL import Image, ImageOps

# Add Waveshare e-Paper library path
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in3e  # Ensure this is the correct model for 6-color display

logging.basicConfig(level=logging.INFO)

def process_image(image_path, epd):
    """ Resize image correctly and convert to the 6-color palette """
    logging.info(f"Opening image: {image_path}")
    image = Image.open(image_path).convert("RGB")

    # Resize image to fit within 800x480 without cropping
    resized = ImageOps.contain(image, (epd.width, epd.height), method=Image.LANCZOS)

    # Create a white 800x480 canvas and paste the resized image centered
    final_image = Image.new("RGB", (epd.width, epd.height), (255, 255, 255))
    offset = ((epd.width - resized.width) // 2, (epd.height - resized.height) // 2)
    final_image.paste(resized, offset)

    # Define the 6-color palette
    palette = [
         0,   0,   0,    # Black
       255, 255, 255,    # White
       255,   0,   0,    # Red
         0, 128,   0,    # Green
         0,   0, 255,    # Blue
       255, 255,   0     # Yellow
    ]

    # Pad the palette to 768 values (256 * 3) with zeros
    palette += [0] * (768 - len(palette))

    # Create a 1x1 palette image and assign the custom palette
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette(palette)

    # Convert image to 6-color mode using Floyd-Steinberg dithering
    quantized = final_image.quantize(palette=pal_img, dither=Image.FLOYDSTEINBERG)

    return quantized

def main(image_path):
    try:
        logging.info("Initializing e-Paper Display")
        epd = epd7in3e.EPD()
        epd.init()
        epd.Clear()

        logging.info(f"Processing image: {image_path}")
        image = process_image(image_path, epd)

        # Ensure the image is in the correct format for the e-Paper buffer
        image = image.convert("RGB")

        logging.info("Displaying image...")
        epd.display(epd.getbuffer(image))
        time.sleep(60)  # How long to display the image for

        logging.info("Clearing display and going to sleep...")
        epd.Clear()
        epd.sleep()

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.info("Exiting...")
        epd.sleep()
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 display_image.py <image_path>")
        sys.exit(1)

    main(sys.argv[1])