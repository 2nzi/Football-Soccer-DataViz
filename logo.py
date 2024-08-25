

#V1

# # Remplace par ta clé d'API et l'URL correcte de l'API
# api_url = "https://api.football-data.org/v2/competitions/PL/teams"
# headers = {"X-Auth-Token": "904dce08636845b3888ad5f2afce2792"}

# response = requests.get(api_url, headers=headers)
# data = response.json()

# for team in data['teams']:
#     st.image(team['crestUrl'], caption=team['name'])











#V2

# import requests
# import streamlit as st
# from PIL import Image
# from io import BytesIO

# # URL de base du dépôt GitHub
# base_url = "https://raw.githubusercontent.com/luukhopman/football-logos/master/logos/"

# # Dictionnaire des ligues et répertoires correspondants
# leagues = {
#     "Ligue 1": "FR1",
#     "Premier League": "GB1",
#     # Ajoute d'autres ligues ici
# }

# # Fonction pour obtenir le logo d'un club
# def get_club_logo(league, club_name):
#     # Crée l'URL complète en fonction de la ligue et du nom du club
#     url = f"{base_url}{leagues[league]}/{club_name.replace(' ', '%20')}.png"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         image = Image.open(BytesIO(response.content))
#         return image
#     else:
#         return None

# # Interface utilisateur avec Streamlit
# st.title("Recherche de logos de clubs de football")

# # Sélectionne la ligue
# selected_league = st.selectbox("Sélectionne la ligue", list(leagues.keys()))

# # Entrer le nom du club
# club_name = st.text_input("Entrez le nom du club (ex: Paris Saint-Germain)")

# if st.button("Rechercher"):
#     if selected_league and club_name:
#         logo = get_club_logo(selected_league, club_name)
#         if logo:
#             st.image(logo, caption=f"Logo de {club_name}")
#         else:
#             st.error("Logo non trouvé. Assurez-vous que le nom du club est correct.")
#     else:
#         st.error("Veuillez sélectionner une ligue et entrer un nom de club.")




#V3
import requests
from bs4 import BeautifulSoup

# URL de base du dépôt GitHub
base_url = "https://github.com/luukhopman/football-logos/tree/master/logos"

# Fonction pour obtenir tous les répertoires de ligues
def get_league_directories(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Trouve tous les répertoires de ligues
    league_dirs = [a['href'] for a in soup.find_all('a', class_='js-navigation-open Link--primary') if '/tree/master/logos/' in a['href']]
    return league_dirs

# Fonction pour obtenir toutes les images de logos dans un répertoire de ligue
def get_logos_in_league(league_url):
    response = requests.get(f"https://github.com{league_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    # Trouve toutes les images de logos dans le répertoire
    logos = [a['href'] for a in soup.find_all('a', class_='js-navigation-open Link--primary') if a['href'].endswith('.png')]
    return logos

# Fonction pour convertir le lien GitHub en lien direct pour télécharger l'image
def convert_to_raw_url(github_url):
    return github_url.replace('/blob/', '/raw/').replace('github.com', 'raw.githubusercontent.com')

# Scraper les ligues et les logos
def scrape_all_logos():
    leagues = get_league_directories(base_url)
    all_logos = {}
    
    for league in leagues:
        league_name = league.split('/')[-1]
        logos = get_logos_in_league(league)
        all_logos[league_name] = [convert_to_raw_url(f"https://github.com{logo}") for logo in logos]
    
    return all_logos

# Fonction pour enregistrer les liens dans un fichier texte
def save_links_to_file(logos_data, filename="logos_links.txt"):
    with open(filename, 'w') as file:
        for league, logos in logos_data.items():
            file.write(f"Ligue: {league}\n")
            for logo in logos:
                file.write(f"{logo}\n")
            file.write("\n")

# Exécution du scraping et enregistrement des liens
logos_data = scrape_all_logos()
save_links_to_file(logos_data)

print("Les liens des logos ont été enregistrés dans 'logos_links.txt'")
