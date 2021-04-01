#pip install dropbox command to install all the libraries of dropbox in python

import dropbox #importing libraries of dropbox

dropbox_access_token="35WvAI491GgAAAAAAAAAAQdJQJXaruH9WTjDx_Ofh3Y9q06VZZZqtD5l0iZcejxA"
dropbox_path = "/home/Weather_report/test1.jpg"
computer_path = "C:\Trial1.jpg"

client = dropbox.Dropbox(dropbox_access_token)
print("Successfully linked to dropbox account")

client.files_upload(open(computer_path,"rb").read(),dropbox_path)
print("{Uplaoded} file uploaded to dropbox")
