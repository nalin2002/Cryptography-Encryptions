import dropbox
import hashlib
import base64
import os

in_file= open("myfile1.txt","w+")
for i in range(100):
    in_file.write("The line number is %d \n" % (i+1))
in_file.close()

contents= open("myfile1.txt","r").read()  # file content in string format

sha_encode= hashlib.sha256(contents.encode()) # sha256 hash value of file content

file_name="myfile1"
b64_encode=base64.b64encode(file_name.encode())
new_file_name=b64_encode.decode()

os.rename(r'C:\Users\aprab\PycharmProjects\Python_Projects\myfile1.txt',r'C:\Users\aprab\PycharmProjects\Python_Projects'+"\\"+new_file_name+".data")

print("Successfully renamed with base64 name")

dropbox_access_token="35WvAI491GgAAAAAAAAAAQdJQJXaruH9WTjDx_Ofh3Y9q06VZZZqtD5l0iZcejxA"
dropbox_path=r"/home/Weather_report/bXlmaWxlMQ==.data"
computer_path=r"C:\Users\aprab\PycharmProjects\Python_Projects\bXlmaWxlMQ==.data"

client=dropbox.Dropbox(dropbox_access_token)
print("Successfully linked to dropbox account")


with open(computer_path,"rb") as f:
 client.files_upload(f.read(),dropbox_path)
 print("Successfully Uploaded")


