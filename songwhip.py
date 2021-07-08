import sys

from lxml import html
from requests import request

url = "https://songwhip.com/"

payload = sys.argv[1]

response = request("POST", url, data=payload)
links_page = request("GET", response.json()['url'])
doc = html.fromstring(links_page.content)

elements = doc.xpath("//div/a[contains(@href,'http')][not(contains(@href,'songwhip'))]")
service_link_dict = {el.xpath("div[contains(@class,'regular')]")[0].text: el.get('href') for el in elements}

# to remove service from output - comment or remove it from output_services list
output_services = [
    'Amazon Music',
    'Apple Music',
    'Deezer',
    'Napster',
    'Spotify',
    'Tidal',
    'Yandex',
    'YouTube',
    'YouTube Music',
]

for service, link in service_link_dict.items():
    if any(map(service.__eq__, output_services)):
        print("[{}]({})".format(service, link))
