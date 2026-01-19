from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


def setopati_news():
    resp = requests.get('https://www.setopati.com/politics', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(resp.text, 'lxml')
    news = soup.find_all("div", class_="items col-md-6")
    combined_news=[]
    for div in news:
        anchor = div.find('a')
        if not anchor:
            continue

        link = anchor.get('href')

        title_tag = anchor.find('span', class_='main-title')
        title = title_tag.get_text(strip=True) if title_tag else "No Title"

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        

       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url
        })

    return combined_news
def setopati_financial():
    resp = requests.get('https://www.setopati.com/kinmel', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(resp.text, 'lxml')
    news = soup.find_all("div", class_="items col-md-4")
    combined_news=[]
    for div in news:
        anchor = div.find('a')
        if not anchor:
            continue

        link = anchor.get('href')

        title_tag = anchor.find('span', class_='main-title')
        title = title_tag.get_text(strip=True) if title_tag else "No Title"

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        

       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url
        })

    return combined_news


def home(request):  
    news_list= [setopati_news(), setopati_financial()]
    return render(request, "home.html", {"news_list": news_list})