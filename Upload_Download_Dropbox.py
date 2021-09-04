import dropbox #importing libraries of dropbox
import hashlib
from time import time

def upload(filename,client):
  dropbox_path= '/Weather_report/'+str(filename)
  # client = dropbox.Dropbox(dropbox_access_token)
  # print("Successfully linked to dropbox account!!!")
  print("Now Uploading the file.... \n ")
  with open(filename,'rb') as f:
    client.files_upload(f.read(),dropbox_path)
  
  print(filename+' successfully uploaded to dropbox')

def download(filename,client):
    print("Downloading the file.... \n")
    f=open(filename, "wb")
    metadata, res = client.files_download(path="/Weather_report/"+filename)
    f.write(res.content)
  
    print(filename+' successfully downloaded!!')
    return res.content
  

def func(filename,client):
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
  file_content=download(filename,client)
  t2= time()-init
  print('Time taken to download '+filename+' is : ',time()-init)
  print(' ')

  received_sha_value= hashlib.sha256(file_content)

  if original_sha_value.hexdigest()==received_sha_value.hexdigest():
    print("Correct file downloaded!!!")
  else:
    print("Incorrect file!!!")
  print('------------------------------------------------------------------------------------------')
  return t1,t2

dropbox_access_token="35WvAI491GgAAAAAAAAAAQdJQJXaruH9WTjDx_Ofh3Y9q06VZZZqtD5l0iZcejxA"
client = dropbox.Dropbox(dropbox_access_token)
print("Successfully linked to your dropbox account!!")

t1,t2= func('2KB_file.txt',client)
t3,t4= func('16KB_file.txt',client)
t5,t6= func('256KB_file.txt',client)
t7,t8= func('4MB_file.txt',client)
t9,t10=func('64MB_file.txt',client)

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
