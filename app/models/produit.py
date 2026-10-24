import sqlite3
import os

class Produit:
    def __init__(self, titre, prix, lien, image_url=None):
        self.titre = titre
        self.prix = prix
        self.lien = lien
        self.image_url = image_url

    @staticmethod
    def init_db():
        """Initialise la base de données SQLite."""
        # On s'assure que le dossier data existe
        os.makedirs('data', exist_ok=True)
        
        conn = sqlite3.connect('data/scraper.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                prix REAL,
                lien TEXT NOT NULL,
                image_url TEXT,
                date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def save(self):
        """Sauvegarde un produit dans la base."""
        conn = sqlite3.connect('data/scraper.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produits (titre, prix, lien, image_url)
            VALUES (?, ?, ?, ?)
        ''', (self.titre, self.prix, self.lien, self.image_url))
        conn.commit()
        conn.close()