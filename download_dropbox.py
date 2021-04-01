import dropbox
import hashlib
import os
import base64

in_file=open("myfile1.txt","r").read()
sha256_encode=hashlib.sha256(in_file.encode())


dropbox_access_token="35WvAI491GgAAAAAAAAAAQdJQJXaruH9WTjDx_Ofh3Y9q06VZZZqtD5l0iZcejxA"

client=dropbox.Dropbox(dropbox_access_token)
print("Successfully linked with your account")

with open("trial1.data", "wb") as f:
    metadata, res = client.files_download(path=r"/home/Weather_report/bXlmaWxlMQ==.data")
    f.write(res.content)

os.rename(r'C:\Users\aprab\PycharmProjects\Python_Projects\trial1.data',r'C:\Users\aprab\PycharmProjects\Python_Projects'+"\\"+"check.txt")

content=open("check.txt","r").read()
sha256_encode1=hashlib.sha256(content.encode())


if(sha256_encode.hexdigest() == sha256_encode1.hexdigest()):
    print("files are same")
else:
    print("files are not same")
