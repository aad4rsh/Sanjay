import requests
from bs4 import BeautifulSoup

def debug_ekantipur():
    url = 'https://ekantipur.com/politics'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser') 
        teaser = soup.find("div", class_="teaser offset")
        
        if teaser:
            print("Found teaser.")
            parent = teaser.parent
            print(f"Parent Tag: {parent.name}, Classes: {parent.get('class')}")
            print("\n--- Parent Children ---")
            for child in parent.children:
                if child.name:
                    print(f"Tag: {child.name}, Classes: {child.get('class')}")
                    if child.get('class') and 'image' in child.get('class'):
                         print("   -> Found sibling div.image!")
        else:
             print("Teaser not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_ekantipur()
