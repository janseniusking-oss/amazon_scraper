from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class AmazonScraper:
    def __init__(self):
        # Configuration du navigateur Chrome "invisible"
        self.options = Options()
        # self.options.add_argument("--headless") # Décommente cette ligne si tu ne veux VRAIMENT pas voir la fenêtre s'ouvrir
        self.options.add_argument("--disable-blink-features=AutomationControlled") # Cache le fait qu'on est un robot
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    def scrape_search(self, url):
        print("Lancement du vrai navigateur Chrome...")
        
        # Lancement du navigateur
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        
        try:
            print(f"Navigation vers : {url}")
            driver.get(url)
            
            # On attend un peu que la page charge (comme un humain)
            time.sleep(random.uniform(3, 6))
            
            # On récupère le code HTML de la page
            html = driver.page_source
            
            # On sauvegarde pour le debug
            with open("debug_amazon.html", "w", encoding="utf-8") as f:
                f.write(html)
                
            print(f"Titre de la page : {driver.title}")
            
            produits = []
            
            # On cherche les blocs de produits
            items = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
            print(f"Nombre de blocs de produits trouvés : {len(items)}")

            for item in items:
                try:
                    titre = item.find_element(By.CSS_SELECTOR, "h2").text.strip()
                except:
                    titre = "Titre inconnu"
                
                try:
                    prix_brut = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text.strip()
                    prix = float(prix_brut.replace('.', '').replace(',', '.'))
                except:
                    prix = 0.0 
                
                try:
                    lien_relatif = item.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                    lien = lien_relatif
                except:
                    lien = ""

                produits.append({
                    'titre': titre,
                    'prix': prix,
                    'lien': lien,
                    'image_url': None
                })
            
            return produits

        finally:
            # On ferme toujours le navigateur à la fin
            driver.quit()