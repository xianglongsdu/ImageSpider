import requests
from bs4 import BeautifulSoup as bs

dirname ='./images/'
for i in range(2, 3):
    url = 'http://www.jiepaids.com/forum-459-' + str(i) + '.html'
    res = requests.get(url)
    soup = bs(res.content, 'html.parser')
    all_a = soup.find('ul', class_='ml mlt mtw cl').find_all('a', class_='z')
    for a in all_a:
        img_url = a['href']
        response = requests.get(img_url)
        img_soup = bs(response.content, 'html.parser')
        images = img_soup.find_all('img', class_='zoom')
        for image in images:
            filename = dirname + image['src'].split('/')[-1]
            img = requests.get(image['src'])
            f = open(filename, 'wb')
            f.write(img.content)
            f.close()





    