
import requests
from bs4 import BeautifulSoup

def setopati_financial():
    try:
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
                'image': img_url,
                # 'source' is MISSING in original code
            })
        print(f"Setopati Financial: Found {len(combined_news)} items")
        if combined_news:
            print(f"Sample: {combined_news[0]}")
    except Exception as e:
        print(f"Setopati Error: {e}")

def ekantipur_financial():
    try:
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
            combined_news.append({
                'title': title,
                'link': link,
                'source': 'Ekantipur'
            })
        print(f"Ekantipur Financial: Found {len(combined_news)} items")
        if combined_news:
            print(f"Sample: {combined_news[0]}")
    except Exception as e:
        print(f"Ekantipur Error: {e}")

if __name__ == "__main__":
    setopati_financial()
    ekantipur_financial()
