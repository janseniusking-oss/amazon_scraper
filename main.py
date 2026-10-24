from app.controllers.scraping_controller import ScrapingController
import sys

def main():
    # Lien de recherche Amazon (exemple : "iphone 13")
    url = "https://www.amazon.fr/s?k=iphone+13"
    
    try:
        controller = ScrapingController()
        controller.run_scraping(url)
    except KeyboardInterrupt:
        print("\nArrêt manuel.")
        sys.exit(0)

if __name__ == "__main__":
    main()