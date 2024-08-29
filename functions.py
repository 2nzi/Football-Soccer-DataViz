from mplsoccer import Pitch
import streamlit as st
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process


def display_player_names_and_positions_middlePitch(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away):
    # Dictionaries to store coordinates and player names for both home and away teams
    coordinates_dict_home = {}
    player_names_dict_home = {}
    coordinates_dict_away = {}
    player_names_dict_away = {}

    # Process home team lineup
    for index, row in home_lineups.iterrows():
        player_name = row['player_name']
        position_info = row['positions'][0] if row['positions'] else {}
        position_id = position_info.get('position_id', 'Unknown')

        if position_id in position_id_to_coordinates_home:
            coordinates_dict_home[position_id] = position_id_to_coordinates_home[position_id]
            player_names_dict_home[position_id] = player_name

    # Process away team lineup
    for index, row in away_lineups.iterrows():
        player_name = row['player_name']
        position_info = row['positions'][0] if row['positions'] else {}
        position_id = position_info.get('position_id', 'Unknown')

        if position_id in position_id_to_coordinates_away:
            coordinates_dict_away[position_id] = position_id_to_coordinates_away[position_id]
            player_names_dict_away[position_id] = player_name

    # Plotting the pitch
    pitch = Pitch(
        # pitch_color='#1f77b4', 
        pitch_color='#d2d2d2', 
        line_color='white', 
        stripe=False, 
        pitch_type='statsbomb'
    )

    fig, ax = pitch.draw()

    # Plotting home team positions
    if coordinates_dict_home:
        x_coords_home, y_coords_home = zip(*coordinates_dict_home.values())
        ax.scatter(x_coords_home, y_coords_home, color='red', s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_home.items():
            name = player_names_dict_home.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Plotting away team positions
    if coordinates_dict_away:
        x_coords_away, y_coords_away = zip(*coordinates_dict_away.values())
        ax.scatter(x_coords_away, y_coords_away, color='blue', s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_away.items():
            name = player_names_dict_away.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Display the plot in Streamlit
    st.pyplot(fig)



def display_player_names_and_positions_twoTeam(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away):
    # Dictionaries to store coordinates and player names for both home and away teams
    coordinates_dict_home = {}
    player_names_dict_home = {}
    coordinates_dict_away = {}
    player_names_dict_away = {}

    # Process home team lineup
    for index, row in home_lineups.iterrows():
        player_name = row['player_name']
        position_info = row['positions'][0] if row['positions'] else {}
        position_id = position_info.get('position_id', 'Unknown')

        if position_id in position_id_to_coordinates_home:
            coordinates_dict_home[position_id] = position_id_to_coordinates_home[position_id]
            player_names_dict_home[position_id] = player_name

    # Process away team lineup
    for index, row in away_lineups.iterrows():
        player_name = row['player_name']
        position_info = row['positions'][0] if row['positions'] else {}
        position_id = position_info.get('position_id', 'Unknown')

        if position_id in position_id_to_coordinates_away:
            coordinates_dict_away[position_id] = position_id_to_coordinates_away[position_id]
            player_names_dict_away[position_id] = player_name

    # Plotting the pitch
    pitch = Pitch(
        # pitch_color='#1f77b4', 
        pitch_color='#d2d2d2', 
        line_color='white', 
        stripe=False, 
        pitch_type='statsbomb'
    )

    fig, ax = pitch.draw()

    # Plotting home team positions
    if coordinates_dict_home:
        x_coords_home, y_coords_home = zip(*coordinates_dict_home.values())
        ax.scatter(x_coords_home, y_coords_home, color='red', s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_home.items():
            name = player_names_dict_home.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Plotting away team positions
    if coordinates_dict_away:
        x_coords_away, y_coords_away = zip(*coordinates_dict_away.values())
        ax.scatter(x_coords_away, y_coords_away, color='blue', s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_away.items():
            name = player_names_dict_away.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Display the plot in Streamlit
    st.pyplot(fig)



def display_player_names_and_positions_oneTeam(home_lineups, position_id_to_coordinates_home,color):
    # Dictionaries to store coordinates and player names for the home team
    coordinates_dict_home = {}
    player_names_dict_home = {}

    # Process home team lineup
    for index, row in home_lineups.iterrows():
        player_name = row['player_name']
        position_info = row['positions'][0] if row['positions'] else {}
        position_id = position_info.get('position_id', 'Unknown')

        if position_id in position_id_to_coordinates_home:
            coordinates_dict_home[position_id] = position_id_to_coordinates_home[position_id]
            player_names_dict_home[position_id] = player_name

    # Plotting the pitch
    pitch = Pitch(
        pitch_color='#d2d2d2',
        line_color='white',
        stripe=False,
        pitch_type='statsbomb'
    )

    fig, ax = pitch.draw()

    # Plotting home team positions
    if coordinates_dict_home:
        x_coords_home, y_coords_home = zip(*coordinates_dict_home.values())
        ax.scatter(x_coords_home, y_coords_home, color=color, s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_home.items():
            name = player_names_dict_home.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Display the plot in Streamlit
    st.pyplot(fig)




# Function to find the best image match based on the team name
def get_best_match_image(team_name, images_data):
    image_names = [image['image_name'] for image in images_data]
    best_match, match_score = process.extractOne(team_name, image_names, scorer=fuzz.token_sort_ratio)
    if match_score > 70:  # Adjust the threshold as needed
        for image in images_data:
            if image['image_name'] == best_match:
                return image['image_link']
    return None




#make a class !

class StadiumImageFetcher:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def get_stadium_image_url(self, stadium_name):
        # Formulate the Google Image search URL
        query = stadium_name.replace(' ', '+')
        url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
        
        # Send the request
        response = requests.get(url, headers=self.headers)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Find the first image result
        images = soup.find_all('img')
        
        if images and len(images) > 1:  # The first image might be the Google logo, so skip it
            return images[1]['src']
        else:
            return None

    def display_stadium(self):
        st.title("Stadium Image Display")

        # Input the stadium name
        stadium_name = st.text_input("Enter the stadium name:")
        
        if stadium_name:
            # Get the image URL
            image_url = self.get_stadium_image_url(stadium_name)
            
            if image_url:
                st.image(image_url, caption=f'{stadium_name} Stadium')
            else:
                st.write("Image not found.")

def main_stadium():
    stadium = StadiumImageFetcher()
    stadium.display_stadium()

if __name__ == "__main__":
    main_stadium()
