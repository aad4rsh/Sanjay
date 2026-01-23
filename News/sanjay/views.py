from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import random
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
        title = title_tag.get_text(strip=True) if title_tag else None

        if not title:
            continue

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        

       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url,
            'source': 'Setopati'
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
        title = title_tag.get_text(strip=True) if title_tag else None

        if not title:
            continue

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
def setopati_sports():
    resp = requests.get('https://www.setopati.com/sports', headers={
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
        title = title_tag.get_text(strip=True) if title_tag else None

        if not title:
            continue

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        
       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url,
            'source': 'Setopati'
        })
    return combined_news
def setopati_global():
    resp = requests.get('https://www.setopati.com/global', headers={
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
        title = title_tag.get_text(strip=True) if title_tag else None

        if not title:
            continue

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        

       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url,
            'source': 'Setopati'
        })

    return combined_news
def setopati_blog():
    resp = requests.get('https://www.setopati.com/blog', headers={
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
        title = title_tag.get_text(strip=True) if title_tag else None

        if not title:
            continue

        img_tag = anchor.find('img')
        img_url =""
        if img_tag:
            img_url = img_tag.get('data-src') or img_tag.get('src')
        
       
        combined_news.append({
            'title':title,
            'link': link,
            'image': img_url,
            'source': 'Setopati'
        })
    return combined_news

def ekantipur_politics():
    resp = requests.get('https://ekantipur.com/politics', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(resp.text, 'lxml')
    # Based on the user provided image, the container is div.teaser.offset
    news_items = soup.find_all("div", class_="teaser offset")
    combined_news = []
    
    for div in news_items:
        h2 = div.find('h2')
        if not h2:
            continue
            
        anchor = h2.find('a')
        if not anchor:
            continue

        title = anchor.get_text(strip=True)
        link = anchor.get('href')
        if link and not link.startswith('http'):
            link = 'https://ekantipur.com' + link

        img_url = ""
        # The 'image' div is a sibling, not a child of 'teaser offset'.
        # We look in the parent container.
        parent = div.parent
        image_div = parent.find('div', class_='image') if parent else None
        
        if image_div:
            figure = image_div.find('figure')
            if figure:
                img_a = figure.find('a')
                if img_a:
                    img_tag = img_a.find('img')
                    if img_tag:
                         img_url = img_tag.get('data-src') or img_tag.get('src')
                # Sometimes img is direct child of figure if not wrapped in 'a'
                elif not img_url:
                     img_tag = figure.find('img')
                     if img_tag:
                         img_url = img_tag.get('data-src') or img_tag.get('src')
        
        combined_news.append({
            'title': title,
            'link': link,
            'image': img_url,
            'source': 'Ekantipur'
        })

    return combined_news
def ekantipur_financial():
    resp = requests.get('https://ekantipur.com/business', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(resp.text, 'lxml')
    news_items = soup.find_all("div", class_="teaser offset")
    combined_news = []
    
    for div in news_items:
        h2 = div.find('h2')
        if not h2:
            continue
            
        anchor = h2.find('a')
        if not anchor:
            continue
        title = anchor.get_text(strip=True)
        link = anchor.get('href')
        if link and not link.startswith('http'):
            link = 'https://ekantipur.com' + link

        img_url = ""
        # The 'image' div is a sibling, not a child of 'teaser offset'.
        # We look in the parent container.
        parent = div.parent
        image_div = parent.find('div', class_='image') if parent else None
        
        if image_div:
            figure = image_div.find('figure')
            if figure:
                img_a = figure.find('a')
                if img_a:
                    img_tag = img_a.find('img')
                    if img_tag:
                         img_url = img_tag.get('data-src') or img_tag.get('src')
                # Sometimes img is direct child of figure if not wrapped in 'a'
                elif not img_url:
                     img_tag = figure.find('img')
                     if img_tag:
                         img_url = img_tag.get('data-src') or img_tag.get('src')
        
        combined_news.append({
            'title': title,
            'link': link,
            'image': img_url,
            'source': 'Ekantipur'
        })
    return combined_news

def home(request):  
    politics_news = setopati_news() + ekantipur_politics()
    random.shuffle(politics_news)
    financial_news = setopati_financial() + ekantipur_financial()
    random.shuffle(financial_news)
    global_news = setopati_global()
    random.shuffle(global_news)
    sports_news = setopati_sports()
    random.shuffle(sports_news)
    blog_news = setopati_blog()
    random.shuffle(blog_news)
    
    # General news mixes everything
    general_news = politics_news + financial_news
    random.shuffle(general_news)

    return render(request, "home.html", {
        "politics_news": politics_news[:4],  # Only first 4 items
        "financial_news": financial_news[:4], 
        "global_news": global_news[:4], # Only first 4 items
        "sports_news": sports_news[:4],
        "blog_news": blog_news[:4]
    })

def news_list(request, category):
    """View for displaying all news articles of a specific category"""
    if category == 'politics':
        news = setopati_news() + ekantipur_politics()
        random.shuffle(news)
        title = "Politics News"
    elif category == 'economy':
        news = setopati_financial() + ekantipur_financial()
        random.shuffle(news)
        title = "Economy News"
    elif  category  == 'global':
        news = setopati_global()
        title = "Global News"
    elif category == 'sports':
        news = setopati_sports()
        title = "Sports News"
    elif category == 'blog':
        news = setopati_blog()
        title = "Blog News"

    else:
        news = []
        title = "News"
    
    return render(request, "news_list.html", {
        "news": news,
        "category": category,
        "title": title
    })