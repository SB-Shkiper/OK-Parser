from bs4 import BeautifulSoup
import lxml
import stealth_requests
from fake_useragent import UserAgent

ua = UserAgent()
random_user = ua.random
print('Enter a link to the OK page')
ok_link = input('>>> ')
url = f'{ok_link}'

headers = {'User -Agent': random_user}
proxy= {
'http': 'your proxy',
'https': 'your proxy'
}

rec = stealth_requests.get(url, headers=headers, proxies=proxy)
soup = BeautifulSoup(rec.text, features="lxml")

#data
image = soup.find('img',class_='photo-img__pcb42')
name = soup.find('span',class_='title__bilbo')
last_visit = soup.find('div',class_ ='last-visit-mark__bilbo')
elements = soup.find_all('div', class_='meta-text__bilbo')

if image:
    img = image.get('src')

name_text = name.text.strip()
last_visit_text = last_visit.text.strip()
ignore = ['Подробнее', 'More', 'Learn more',]
filtered_elements = [el.text.strip() for el in elements if el.text.strip() != ignore]

if len(filtered_elements) >= 2:
    city = filtered_elements[0]
    birthday = filtered_elements[1]
else:
    city = None
    birthday = None

print('Photo: ' + img)
print('Name: ' + name_text)
print(last_visit_text)
print('City: ' + city)
print('Birthday: ' + birthday)
