from app.scraper.amazon_scraper import AmazonScraper
from app.models.produit import Produit

class ScrapingController:
    def __init__(self):
        self.scraper = AmazonScraper()
        # On initialise la base de données dès le départ
        Produit.init_db()

    def run_scraping(self, search_url):
        print(f"Début du scraping : {search_url}")
        
        # 1. On récupère les données
        data = self.scraper.scrape_search(search_url)
        
        # 2. On les sauvegarde
        count = 0
        for item in data:
            p = Produit(
                titre=item['titre'],
                prix=item['prix'],
                lien=item['lien'],
                image_url=item['image_url']
            )
            p.save()
            count += 1
        
        print(f"Scraping terminé. {count} produits ajoutés en base.")
        return count