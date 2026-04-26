import requests
from bs4 import BeautifulSoup
import json
import os

def scrape():
    url = "https://nakios.fit"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = []

        # On cherche les cartes de films (à adapter selon les balises du site)
        # Exemple générique :
        items = soup.select('.item, .post, .movie-card') 
        
        for item in items[:20]: # On prend les 20 derniers
            title_tag = item.find('h2') or item.find('h3')
            link_tag = item.find('a')
            img_tag = item.find('img')

            if title_tag and link_tag:
                movies.append({
                    "title": title_tag.text.strip(),
                    "link": link_tag['href'],
                    "img": img_tag['src'] if img_tag else "https://via.placeholder.com/200x300"
                })

        with open('movies.json', 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)
        print("Mise à jour réussie.")

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    scrape()
