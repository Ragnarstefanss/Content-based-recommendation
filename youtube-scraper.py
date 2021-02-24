import pandas as pd
#pd.set_option('max_colwidth', None)

from bs4 import BeautifulSoup as bs
import requests

my_url = "https://www.youtube.com/user/aandawesome/videos"

r = requests.get(my_url)
page = (r.text)
soup=bs(page,'html.parser')

d = []
for match in soup.find_all('ytd-grid-video-renderer',class_="style-scope ytd-grid-renderer"):
    print(match)
    view = match.find('span',class_="style-scope ytd-grid-video-renderer")
    d.append(
        {
            'Title': match.a.text,
            'View': view.text.split("views")[0],
            'Upload date':view.text.split("views")[1]
        }
    )

pd.DataFrame(d)

print(d)
