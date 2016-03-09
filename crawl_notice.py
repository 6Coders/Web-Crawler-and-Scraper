# International Islamic University, Chittagong, CSE Dept. Website's Notice Crawler/Grabber

import requests
from bs4 import BeautifulSoup


def grab_notice():
    url = 'http://www.iiuc.ac.bd/cse/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    texts = list()
    links = list()
    dates = list()
    data = open('notices.txt', 'w')
    for title in soup.findAll('font', {'color': '#623131'}):
        text = title.string.strip()
        texts.append(text)

    for time in soup.findAll('font', {'color': '#8CAEFD'}):
        date = time.string.strip()
        dates.append(date)

    for link in soup.findAll('a', {'style': 'text-decoration:none;color:#734E37 '}):
        href = url + link.get('href')
        links.append(href)

    for a in range(len(texts)):
        data.write(texts[a]+'   '+dates[a]+'\n'+links[a]+'\n')
        print(texts[a]+'   '+dates[a])
        print(links[a])
    data.close()


grab_notice()
