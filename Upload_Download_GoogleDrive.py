from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from time import time
import matplotlib.pyplot as plt
import hashlib

def upload(filename,drive):
    file = drive.CreateFile({'title': filename})
    file.SetContentString(open(filename,'r').read())  # this writes a string directly to a file
    file.Upload()
def download(filename,file_ID,drive):
    file = drive.CreateFile({'id': file_ID})
    file.GetContentFile(str('Downloaded_')+filename)

    return open(str('Downloaded_')+filename,'r').read()

def func(filename,client):
  name= filename.split(".")[0]
  init=time()
  original_sha_value= hashlib.sha256(open(filename,'r').read().encode())
  print("Time taken to generate a SHA hash value for "+filename+" is : ",time()-init)
  print(' ')

  init=time()
  upload(filename,client)
  t1= time()-init
  print("Time taken to upload "+filename+' is : ',time()-init)
  print(' ')

  init=time()
  query= "title contains '"+str(name)+"' and trashed=false"
  file_list = client.ListFile({'q': query}).GetList()
  file_ID = file_list[0]['id']  # get the file ID
  print("Time taken to find the ID of our required file is : ",time()-init)
  print(' ')

  init=time()
  file_content=download(filename,file_ID,client)
  t2= time()-init
  print('Time taken to download '+filename+' is : ',time()-init)
  print(' ')

  received_sha_value= hashlib.sha256(file_content.encode())

  if original_sha_value.hexdigest()==received_sha_value.hexdigest():
    print("Correct file downloaded!!!")
  else:
    print("Incorrect file!!!")
  print('------------------------------------------------------------------------------------------')
  return t1,t2

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
# gauth.LocalWebserverAuth()
# gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

t1,t2= func('2KB_file.txt',drive)
t3,t4= func('16KB_file.txt',drive)
t5,t6= func('256KB_file.txt',drive)
t7,t8= func('4MB_file.txt',drive)
t9,t10=func('64MB_file.txt',drive)


# x axis values
x = [2, 16, 256,4000,64000]
# corresponding y axis values
y = [t1,t3,t5,t7,t9]

plt.plot(x,y, color='red', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.xscale('log',basex=2)
# naming the x axis
plt.xlabel('File size (KB)')
# naming the y axis
plt.ylabel('Time in seconds')
# giving a title to my graph
plt.title('Uploading time Plot')

# function to show the plot
plt.show()

# x axis values
x = [2, 16, 256,4000,64000]
# corresponding y axis values
y = [t2,t4,t6,t8,t10]

plt.plot(x,y, color='red', linestyle='dashed', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.xscale('log',basex=2)
# naming the x axis
plt.xlabel('File size (KB)')
# naming the y axis
plt.ylabel('Time in seconds')
# giving a title to my graph
plt.title('Downloading time Plot')

# function to show the plot
plt.show()
