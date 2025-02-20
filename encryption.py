import cv2
import os
import string
import json
import base64

# Save the image in .png format for better output.
name = input("Enter the full filename (including extension, e.g., image.png or image.jpg) of the image you want to encrypt: ")
img = cv2.imread(name) # Replace with the correct image path

if img is None:
    print("Error: Image not found.")
    exit()

msg = input("Enter secret message: ")
# Since password cannot be read by others so i converted to bytes and save in json file in base64 string.
password = input("Enter a passcode: ")
key = password.encode('utf-8') # converting string to bytes


d = {chr(i):i for i in range(256)}
c = {i:chr(i) for i in range(256)}

height, width, colour_channels = img.shape 

m,n,z = 0,0,0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    z = (z + 1) % 3
    if z==0:
        m+=1
        if m==width:
            m=0
            n+=1
            if n==height:
                print("Error: Message is too long for this image.")
                exit()

encrypted_name = input("Enter a filename (with extension, e.g., output.png) to save the encrypted image: ")
cv2.imwrite(encrypted_name, img)
os.system(f"start {encrypted_name}")  # Use 'start' to open the image on Windows


with open('data.json','w') as f:
    json.dump({
        'c':{str(k):v for k,v in c.items()},
        'len': len(msg),
        'password':base64.b64encode(key).decode('utf-8')
    }, f)