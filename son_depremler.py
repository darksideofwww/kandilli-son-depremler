#darksideofwww <son depremler>
import requests
from bs4 import BeautifulSoup

# URL'imizi belirledik
url = 'http://www.koeri.boun.edu.tr/scripts/lst0.asp'

# URL'den HTML kodunu aldığımız bölüm
response = requests.get(url)
html = response.content

# HTML kodunu BeautifulSoup kütüphanesi ile analiz edelimm
soup = BeautifulSoup(html, 'html.parser')

# Son 10 depremi bulacağımız yer
depremler = soup.find_all('pre')[0].get_text().split('\n')[11:21]

# ekrana yazdırdığımız kısım
for deprem in depremler:
    print(deprem)
