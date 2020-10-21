import os
import urllib

print(os.getcwd())

url = 'https://yandex.ru'
html = urllib.urlopen(url).read()

f = open('index.html', 'w')
f.write(html)