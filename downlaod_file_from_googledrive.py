from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def Download_File_GD(filename,file_ID): # File Id for the text file i.e .txt file
     gauth=GoogleAuth()
     gauth.LocalWebserverAuth()
     drive=GoogleDrive(gauth)

     file=drive.CreateFile({'id':file_ID})
     file.GetContentFile(filename)
     str= filename+' Successfully Downloaded from Google Drive'
     print(str)

# gauth=GoogleAuth()
# gauth.LocalWebserverAuth()
# drive=GoogleDrive(gauth)
#
# #this code works for downloading a txt file but not a google doc and different files
# file_id="1hat3w8-pOGI93BSwIdA4bRzWALs3KxD3"
# file=drive.CreateFile({'id':file_id})
# file.GetContentFile('download.txt')
# print("successfully downloaded")
#
# #code for downloading different files into my current working directory from google drive
# file_id="1oXzAwLidbIWhSk-FEZoYuXiyfbK6Q-4k"
# file3=drive.CreateFile({'id':file_id})
# print('downloading file %s form google drive' %file3['title'])
# file3.GetContentFile('downloaded_resume.pdf',mimetype='text/html')