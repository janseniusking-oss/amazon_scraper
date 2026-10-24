import sqlite3

def afficher_produits():
    conn = sqlite3.connect('data/scraper.db')
    cursor = conn.cursor()
    cursor.execute("SELECT titre, prix, lien FROM produits ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    
    print("\n--- DERNIERS PRODUITS SCRAPPÉS ---")
    if not rows:
        print("Aucun produit trouvé en base.")
    for row in rows:
        print(f"[{row[1]}€] {row[0]}")
        print(f"   -> Lien : {row[2]}")
    print("----------------------------------\n")
    conn.close()