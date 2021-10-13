import requests;
from bs4 import BeautifulSoup;

def how_many_sad(url):
    wiki = url;
    response=requests.get(wiki);

    soup = BeautifulSoup(response.text, 'html.parser')

    txt = soup.getText();

    print(txt.count('sad'));

how_many_sad('https://en.wikipedia.org/wiki/Sadness');