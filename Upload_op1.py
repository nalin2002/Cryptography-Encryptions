import hashlib
import base64
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os


data=open("myfile.txt","r")
data_content=data.read()
data.close()

#finding sha256 value of plain text of input file
sha_val=hashlib.sha256(data_content.encode())              # encoded value  type: <class '_hashlib.HASH'>
sha_input_file=sha_val.hexdigest()                 #a string in hexa decimal format of sha_val type: a string

#computing new file name using base64 encoding
path=r"C:\Users\aprab\PycharmProjects\Python_Projects"

with open("myfile.txt","rb") as f:
            encodedFile_bytes=base64.b64encode(f.read()) # base64 encoding the file content which converts into bytes
            encodedFile_string=encodedFile_bytes.decode()
            print(encodedFile_string)
            os.rename(r"C:\Users\aprab\PycharmProjects\Python_Projects\myfile.txt",
                      r"C:\Users\aprab\PycharmProjects\Python_Projects\ " + encodedFile_string + ".txt")


f="encodedFile_string.txt"
base=os.path.splitext(f)[0]
os.rename(f,base+".data")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


file_name= encodedFile_string+".data"
for x in os.listdir(path):
    if(x== file_name):
        f = drive.CreateFile({'title': x})
        f.SetContentString(os.path.join(path, x))
        f.Upload()
        f = None

print("Uploading Successful")
