import hashlib
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


data=open("myfile.txt","r")
data_content=data.read()
data.close()

#finding sha256 value of plain text of input file
sha_val=hashlib.sha256(data_content.encode())              # encoded value  type: <class '_hashlib.HASH'>
sha_input_file=sha_val.hexdigest()                 #a string in hexa decimal format of sha_val type: a string

gauth=GoogleAuth()
gauth.LocalWebserverAuth()
drive=GoogleDrive(gauth)

file_id="1HTJRbJrZBMf4UeOb0_SASktEjcg-tCQR"
file=drive.CreateFile({'id':file_id})
file.GetContentFile('Download.data')
print("Successfully Downloaded")

file_name='Download.data'
base=os.path.splitext(file_name)[0]
os.rename(file_name,base+".txt")

data1=open("Download.txt","r")
output=data1.read()
data1.close()
sha_val1=hashlib.sha256(output.encode())
sha_output_file=sha_val1.hexdigest()

if(sha_input_file==sha_output_file):
    print("Files Matched")
else:
    print("files not matched")





