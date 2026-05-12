import os 
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
    if file == "mal_encrypt.py" or file == "mal_decrypt.py" or file == "thekey.key" or file == "calc.py"  or file=="LICENSE":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open("thekey.key", "rb") as key:
    secret=key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    decrypted_contents = Fernet(secret).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)