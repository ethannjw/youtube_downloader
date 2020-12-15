from pytube import YouTube
import pytube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(
    executable_path="chromedriver.exe")

payload = {
    'UserName': 'admin',
    'Password': 'P@40ssword123!',
}
driver.get('http://54.255.34.84:5000/Login')
# login
driver.find_element_by_id('UserName').send_keys(payload["UserName"])
driver.find_element_by_id('Password').send_keys(payload["Password"])
driver.find_element_by_id('Password').send_keys(Keys.RETURN)

# go to content create
driver.get("http://54.255.34.84:5000/Admin/Contents/ContentTypes/video/Create?returnUrl=%2FAdmin%2FContents%2FContentItems&admin=1009810766")

file = open("url.txt")
yt_list = []

for url in file:
    #store in a list
    yt = (YouTube(url))

    contenturl = url
    streams = yt.streams
    thumbnail = yt.thumbnail_url
    rating = yt.rating
    created = '09/03/2020' #yt.publish_date format is 2020-03-09
    length = yt.length
    keywords = yt.keywords
    description = "content description"#yt.description
    creator = yt.author
    views = yt.views
    likes = 0
    dislikes = 0
    subscribers = 0
    title = yt.title
    driver.find_element_by_id('TitlePart_Title').send_keys(title)
    driver.find_element_by_id('video_thumbnail_Text').send_keys(thumbnail)
    driver.find_element_by_name('video.description.Text').send_keys(description)
    driver.find_element_by_id('video_creator_Text').send_keys(creator)
    driver.find_element_by_id('video_created_Value').send_keys(created)
    driver.find_element_by_id('video_length_Value').send_keys(length)
    driver.find_element_by_id('video_views_Value').send_keys(views)
    driver.find_element_by_id('video_subscribers_Value').send_keys(subscribers)
    driver.find_element_by_id('video_likes_Value').send_keys(likes)
    driver.find_element_by_id('video_dislikes_Value').send_keys(dislikes)
    driver.find_element_by_id('video_contenturl_Text').send_keys(contenturl)
    streams.get_highest_resolution()
    print(initdata)
    metadata = yt.metadata
    print(title)
    pytube.extract.metadata(metadata)
    initdata()

# streams.get_highest_resolution()

    # try:
    #     YouTube(url).streams.get_by_itag('22').download()
    # except:
    #     pass
