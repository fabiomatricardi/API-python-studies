import io
from PIL import Image
import requests
import os
from io import BytesIO
import time
import ssl
import urllib.request
import cv2
import sys


ssl._create_default_https_context = ssl._create_unverified_context

# serie kaminaki-sekai-no-kamisama-katsudou

file_url = "https://tc-036.agucdn.com/1ab5d45273a9183bebb58eb74d5722d8ea6384f350caf008f08cf018f1f0566d0cb82a2a799830d1af97cd3f4b6a9a81ef3aed2fb783292b1abcf1b8560a1d1aa308008b88420298522a9f761e5aa1024fbe74e5aa853cfc933cd1219327d1232e91847a185021b184c027f97ae732b3708ee6beb80ba5db6628ced43f1196fe/545126644886463d5c462b394d5fa893/ep.1.1677827924.360.m3u8"
image_url = "https://gogocdn.net/cover/celia-sensei-no-wakuwaku-magical-kyoushitsu.png"
response = requests.get(image_url)
img_data = response.content
"""
# Display using PILLOW - will open default image viewer app
orig_img = Image.open(BytesIO(img_data))
imready = orig_img.resize((165, 200))
imready.show()

"""
"""
# Open an image from local directory
img = cv2.imread("yourlocalImage.file", cv2.IMREAD_ANYCOLOR)
while True:
    cv2.imshow("Sheep", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes

cv2.destroyAllWindows() # destroy all windows

"""
images = ["https://gogocdn.net/cover/jarinko-chie-tv.png",
          "https://gogocdn.net/cover/kaminaki-sekai-no-kamisama-katsudou-1679555300.png",
          "https://gogocdn.net/cover/zetsubou-no-kaibutsu.png",
          "https://gogocdn.net/cover/kono-subarashii-sekai-ni-bakuen-wo.png"]
key_typed = ""

def show_my_image(image_ur):
    cap = cv2.VideoCapture(image_ur)  # Open the URL as video
    success, image = cap.read()  # Read the image as a video frame
    if success:
        cv2.imshow('image ', image)  # Display the image for testing
        cv2.waitKey()
    cap.release()
    

while key_typed.lower() != "q":
    i = 1
    for image in images:
        print(f"{i} - image numner {i}")
        i += 1
    key_typed = input(f"Select number of the image you want to display [1 to {i-1}]")
    show_my_image(images[int(key_typed)-1])



# Before exiting the app destroy all windows
cap.release()
cv2.destroyAllWindows()

