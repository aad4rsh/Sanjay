
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
    # setopati_financial()
    # ekantipur_financial()
    
    print("Testing NepalPress...")
    # Test one category
    resp = requests.get('https://www.nepalpress.com/category/business/', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    soup = BeautifulSoup(resp.text, 'lxml')
    # Selector from user image: div.column-news
    news_items = soup.find_all("div", class_="column-news")
    print(f"Found {len(news_items)} items using 'column-news'")
    
    count = 0
    for div in news_items:
        if count >= 3: break
        
        # Structure from image:
        # div.column-news > div.uk-card > a > img
        # div.column-news > div.news-title > h3.title > a
        
        # Try to find the uk-card first to be safe, or just search descendants
        uk_card = div.find("div", class_="uk-card")
        if not uk_card:
            print("No uk-card found in column-news")
            continue
            
        # Link and Image usually in the first anchor inside uk-card (wrapper)
        # or the image might be lazy loaded.
        first_anchor = uk_card.find('a')
        link = first_anchor.get('href') if first_anchor else None
        
        img_tag = first_anchor.find('img') if first_anchor else None
        img_url = ""
        if img_tag:
             img_url = img_tag.get('data-src') or img_tag.get('src')
        
        # Title
        # Siblings of uk-card? No, image showed news-title as sibling of a?
        # Image:
        # div.column-news
        #   div.uk-card
        #     a (image link)
        #     div.news-title
        #       h3.title
        #         a (text)
        
        # So news-title IS inside uk-card ?? 
        # Looking at indentation in image:
        # div.column-news
        #   div.uk-card
        #     ::before
        #     a href="..." (Image link)
        #     div.news-title
        # So yes, news-title is a sibling of the image link, INSIDE uk-card.
        
        title_div = uk_card.find("div", class_="news-title")
        title = "No Title"
        if title_div:
            h3 = title_div.find("h3", class_="title")
            if h3:
                title_a = h3.find("a")
                if title_a:
                     title = title_a.get_text(strip=True)
                     if not link: link = title_a.get('href')

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Image: {img_url}")
        print("-" * 20)
        count += 1
