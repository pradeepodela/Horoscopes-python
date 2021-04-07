import requests
from bs4 import BeautifulSoup



def horscope(hrs):

    url = f'https://www.ganeshaspeaks.com/horoscopes/daily-horoscope/{hrs}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    hrp = soup.find("p", class_="margin-top-xs-0")
    print(f'todays horiscope for your sinsign {hrs} is ')
    print(hrp)
    
my_hrs = input('pls enter ur horiscope:')
horscope(my_hrs)
