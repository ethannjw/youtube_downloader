from pytube import YouTube
import pytube
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login_orchardcms():
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
    return driver

def process_file(filename):
    file = open(filename)
    content_array = []
    count = 0

    type_idx = 0
    item = dict({
        'module_name': '',
        'title': '',
        'url': '',
        'keywords': '',
    })
    for line in file:
        if type_idx == 0 and line.startswith('Module:'):
            module_line = line.split(':')
            item['module_name'] = module_line[1].rstrip()
            type_idx = type_idx + 1

        elif type_idx == 1:
            item['title'] = line.rstrip()
            type_idx = type_idx + 1

        elif type_idx == 2 and line.startswith('http'):
            item['url'] = line.rstrip()
            type_idx = type_idx + 1

        elif type_idx == 3:
            item['keywords'] = line.rstrip()
            content_array.append(item)
            item = dict({
                'module_name': '',
                'title': '',
                'url': '',
                'keywords': '',
            })
            type_idx = 0    # set back to zero
        elif line == '\n': # empty line
            pass
        else:
            pass

    return content_array


def format_date(date):
    return (str(date.day) + '/' + str(date.month) + '/' + str(date.year))

stream_list = []

def upload_content(filename):
    driver = login_orchardcms()
    content_array = process_file(filename)
    for content in content_array:
        driver.get("http://54.255.34.84:5000/Admin/Contents/ContentTypes/video/Create?returnUrl=%2FAdmin%2FContents%2FContentItems&admin=1009810766")
        contenturl = content['url']
        yt = (YouTube(contenturl))
        streams = yt.streams
        thumbnail = yt.thumbnail_url.rstrip()
        rating = yt.rating
        created = format_date(yt.publish_date) # format is dd/mm/yyyy
        length = yt.length
        keywords = yt.keywords
        description = yt.description.rstrip()
        creator = yt.author.rstrip()
        views = yt.views
        likes = random.randint(int(views/2),views) # retunr randonm numbe rbetween views/2 and views
        dislikes = random.randint(int(likes/5),int(likes/2))
        subscribers = random.randint(int(views/10),views)
        title = yt.title.strip()
        driver.find_element_by_id('TitlePart_Title').send_keys(content['title'])
        driver.find_element_by_id('video_thumbnail_Text').send_keys(thumbnail)
        driver.find_element_by_id('video_module_Text').send_keys(content['module_name'])
        driver.find_element_by_id('video_keywords_Text').send_keys(content['keywords'])
        driver.find_element_by_id('video_creator_Text').send_keys(creator)
        driver.find_element_by_id('video_created_Value').send_keys(created)
        driver.find_element_by_id('video_length_Value').send_keys(length)
        driver.find_element_by_id('video_views_Value').send_keys(views)
        driver.find_element_by_id('video_subscribers_Value').send_keys(subscribers)
        driver.find_element_by_id('video_likes_Value').send_keys(likes)
        driver.find_element_by_id('video_dislikes_Value').send_keys(dislikes)
        driver.find_element_by_id('video_contenturl_Text').send_keys(contenturl)
        try:
            driver.find_element_by_name('video.description.Text').send_keys(description)
        except Exception as e:
            pass
        try:
            driver.find_element_by_name('video.description.Text').send_keys(Keys.RETURN)
        except Exception as e:
            pass
        stream_list.append(streams.get_highest_resolution())

#upload_content("10videos.txt")

def download_content(filename):
    content_array = process_file(filename)
    for content in content_array:
        contenturl = content['url']
        yt = (YouTube(contenturl))
        streams = yt.streams
        stream_list.append(streams.get_highest_resolution())

download_content("missed.txt")
print(stream_list)
for stream in stream_list:
    try:
        stream.download('./videos')
    except Exception:
        pass
YouTube('https://www.youtube.com/watch?v=rGtTeq03_aM').streams
.get_highest_resolution().download()
