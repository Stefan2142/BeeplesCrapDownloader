import requests, shutil, re
import ctypes, json, time, datetime
from bs4 import BeautifulSoup

# Create a request to his instagram profile
headers = {'User-Agent': 
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get('https://www.instagram.com/beeple_crap/?hl=en', headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
scriptTag = soup.findAll("script")
strDict = scriptTag[1].text.split('window._sharedData = ')[1][:-1] # Normalize string to look like a json

s = strDict
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string) # Create dict from normalized j
latestPostURL = d['entry_data']['ProfilePage'][0]['user']['media']['nodes'][0]['display_src']

fileName = datetime.date.today().strftime('%Y-%m-%d')
response = requests.get(latestPostURL, stream=True)
with open(fileName+'.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

# Make sure file is written
time.sleep(3)

# Set new wallpaper
SPI_SETDESKWALLPAPER = 20
imagePath = 'C:\\Users\\stefa\\Desktop\\'+fileName+'.jpg'
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath, 3)

del response