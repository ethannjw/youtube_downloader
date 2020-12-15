from pytube import YouTube
import pytube
import requests
from bs4 import BeautifulSoup
from dict2xml import dict2xml

client = requests.session()

login_page = client.get("http://54.255.34.84:5000/Login")
login_page_soup = BeautifulSoup(login_page.text, 'html.parser')
csrf_token = login_page_soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
print(csrf_token)
payload = {
    'UserName': 'admin',
    'Password': 'P@40ssword123!',
    '__RequestVerificationToken': csrf_token,
    'RememberMe': 'false'
}

res = client.post("http://54.255.34.84:5000/Login", payload)
print(res.status_code)
print(res.text)
create_video_page = client.get("http://54.255.34.84:5000/Admin/Contents/ContentTypes/video/Create")


file = open("url.txt")
yt_list = []

for url in file:
    #store in a list
    yt_list.append(YouTube(url))

yt = yt_list[0]

contenturl = "https://www.youtube.com/watch?v=SpW31fnQKWM"
streams = yt.streams
thumbnail = yt.thumbnail_url

rating = yt.rating
created = '2020-03-09'#yt.publish_date format is 2020-03-09

length = yt.length
keywords = yt.keywords
description = "content description"#yt.description
creator = yt.author
views = yt.views
likes = 0
initdata = pytube.extract.initial_data
dislikes = 0
subscribers = 0
title = 'new video'
# print(pytube.extract.metadata(initdata("https://www.youtube.com/watch?v=0tEzvnaaqoA")))
# streams.get_highest_resolution()

# print(publish_date)
header = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryycVFZKL2n4VBei1F',
}


build_content = {
    'TitlePart.Title': ("", title),
    'video.contenturl.Text': ("", contenturl),
    'video.thumbnail.Text': ("", thumbnail),
    'video.description.Text': ("", description),
    'video.creator.Text': ("", creator),
    'video.created.Value': ("", created),
    'video.length.Value': ("", length),
    'video.views.Value': ("", views),
    'video.subscribers.Value': ("", subscribers),
    'video.likes.Value': ("", likes),
    'video.dislikes.Value': ("", dislikes),
    'returnUrl': ("", '/Admin/Contents/ContentItems'),
    '__RequestVerificationToken': ("", csrf_token)
}
print(build_content)
# post a new item
res = client.post('http://54.255.34.84:5000/Admin/Contents/ContentTypes/video/Create?returnUrl=%2FAdmin%2FContents%2FContentItems', headers=header, data=build_content)
res = client.post('http://54.255.34.84:5000/Admin/Contents/ContentTypes/video/Create?returnUrl=%2FAdmin%2FContents%2FContentItems', files=build_content)
print(res.reason)

    # try:
    #     YouTube(url).streams.get_by_itag('22').download()
    # except:
    #     pass
