
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def Upload_File_GD(filename):
    gauth=GoogleAuth()
    gauth.LocalWebserverAuth()
    drive=GoogleDrive(gauth)

    local_file_path=" " # The path of the file in the system
    for file in os.listdir(local_file_path):
        if (file==' '): #Mention the file name to be uploaded
            f= drive.CreateFile({'title':file})
            f.SetContentString(os.path.join(local_file_path,file))
            f.Upload()
            f=None
    str= filename+' Successfully Uploaded to Google Drive'
    print(str)

    
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
#
# #used for creating a new file and then upload into my drive
# file1=drive.CreateFile({'title':'Hello.pdf'})
# file1.SetContentString('Success')
# file1.Upload()
#
# #for sending a local file to google drive
#       #path=r"C:\Users\aprab\PycharmProjects\Python_Projects"
# path=r"D:\downloads"
# for x in os.listdir(path):
#     if(x=='download.txt'):
#              f=drive.CreateFile({'title':x})
#              f.SetContentString(os.path.join(path,x))
#              f.Upload()
#              f=None
