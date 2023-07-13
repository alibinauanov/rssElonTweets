import requests
import xml.etree.ElementTree as ET

rssURL = 'https://rsshub.app/twitter/user/elonmusk'

response = requests.get(rssURL)
xml_content = response.content

root = ET.fromstring(xml_content)

for item in root.findall('.//item'):
    title = item.find('title').text
    print(title)
