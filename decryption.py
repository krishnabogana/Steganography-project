import json
import cv2
import os
import string
import base64

name = input("Enter the name of the image for decryption. ")
img = cv2.imread(name) # Replace with the correct image path

if img is None:
    print("Error: Encrypted image is not found.")
    exit()


with open('data.json','r') as f:
    data = json.load(f)

length = data['len']
enc_password = data['password']
password = base64.b64decode(enc_password.encode('utf-8'))
c = {int(k):v for k,v in data['c'].items()}


message = ""
m,n,z = 0,0,0

pas = input("Enter passcode for Decryption: ")

if  password.decode('utf-8')== pas:
    for i in range(length):
        message = message + c[int(img[n, m, z])]
        z = (z + 1) % 3
        if z==0:
            m+=1
            if m == img.shape[1]:
                m=0
                n+=1
    print("Decryption message:", message)
else:
    print("You are not authorised to access this file.")