import dropbox

dropbox_access_token = "35WvAI491GgAAAAAAAAAAQdJQJXaruH9WTjDx_Ofh3Y9q06VZZZqtD5l0iZcejxA"

client = dropbox.Dropbox(dropbox_access_token)
print("Successfully linked to dropbox account")

with open("trial1.jpg", "wb") as f:
    metadata, res = client.files_download(path="/Weather_report/test1.jpg")
    f.write(res.content)

print("{downloaded} file successfully downloaded")
