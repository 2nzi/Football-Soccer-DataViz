from mplsoccer import Pitch
import streamlit as st
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
import plotly.express as px 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

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



def box_plot_pass(events,team):

    event_filterTeam = events[events['team']==team]
    event_pass = event_filterTeam.filter(regex='^(pass)', axis=1).dropna(how='all')
    event_pass_length = event_pass['pass_length']

    fig = px.box(event_pass_length, y=event_pass_length, labels={'y':'Pass Length'}, title=f'{team} Distribution of Pass Length')
    fig.update_layout(width=300, height=600)  # 200 pixels de largeur, 400 pixels de hauteur

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)












def get_possession(events):
    """
    Extracts and normalizes the possession counts for the two teams from the events DataFrame.

    Parameters:
    - events (pd.DataFrame): DataFrame containing an events column 'possession_team'.

    Returns:
    - home_team_possession (float): Normalized possession percentage for the home team, rounded to one decimal place.
    - away_team_possession (float): Normalized possession percentage for the away team, rounded to one decimal place.
    """
    # Get possession counts
    possession_counts = events['possession_team'].value_counts()
    
    # Get the top two possession teams
    home_team_possession, away_team_possession = possession_counts.iloc[0], possession_counts.iloc[1]
    
    # Calculate total possession
    total_possession = home_team_possession + away_team_possession
    
    # Normalize possession and round to one decimal place
    home_team_possession = round((home_team_possession / total_possession) * 100, 1)
    away_team_possession = round((away_team_possession / total_possession) * 100, 1)
    
    return home_team_possession, away_team_possession



def get_total_xg(events):
    """
    Calcule la somme totale des xG (expected goals) par équipe et retourne les valeurs arrondies à 2 décimales.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'shot_statsbomb_xg' et 'team'.

    Returns:
    - home_xg (float): Somme totale des xG pour l'équipe à domicile, arrondie à 2 décimales.
    - away_xg (float): Somme totale des xG pour l'équipe à l'extérieur, arrondie à 2 décimales.
    """
    # Filtrer les colonnes et supprimer les lignes où 'shot_statsbomb_xg' est NaN
    data = events.filter(regex='^shot_statsbomb_xg|^team$').dropna(subset=['shot_statsbomb_xg'])
    
    # Grouper par 'team' et calculer la somme des xG
    data = data.groupby('team')['shot_statsbomb_xg'].sum()
    
    # Arrondir les résultats à 2 décimales
    home_xg, away_xg = round(data.iloc[0], 2), round(data.iloc[1], 2)
    
    return home_xg, away_xg

def get_total_shots(events):
    """
    Calcule le nombre total de tirs (shots) par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'shot_statsbomb_xg' et 'team'.

    Returns:
    - home_shots (int): Nombre total de tirs pour l'équipe à domicile.
    - away_shots (int): Nombre total de tirs pour l'équipe à l'extérieur.
    """
    # Filtrer les colonnes et supprimer les lignes où 'shot_statsbomb_xg' est NaN
    data = events.filter(regex='^shot_statsbomb_xg|^team$').dropna(subset=['shot_statsbomb_xg'])
    
    # Grouper par 'team' et compter le nombre de tirs
    shot_counts = data.groupby('team').count()['shot_statsbomb_xg']
    
    # Retourner les comptes pour les deux équipes
    home_shots, away_shots = shot_counts.iloc[0], shot_counts.iloc[1]
    
    return home_shots, away_shots


def get_total_shots_off_target(events):
    """
    Calcule le nombre total de tirs non cadrés (off target) par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'shot_outcome' et 'team'.

    Returns:
    - home_off_target (int): Nombre total de tirs non cadrés pour l'équipe à domicile.
    - away_off_target (int): Nombre total de tirs non cadrés pour l'équipe à l'extérieur.
    """
    # Define outcomes that indicate a shot was off target
    off_target_outcomes = ['Off T', 'Blocked', 'Missed']
    
    # Filter the events DataFrame for shots off target
    data = events[events['shot_outcome'].isin(off_target_outcomes)]
    
    # Group by 'team' and count the number of off-target shots
    off_target_counts = data.groupby('team').size()
    
    # Return the counts for the two teams
    home_off_target, away_off_target = off_target_counts.iloc[0], off_target_counts.iloc[1]
    
    return home_off_target, away_off_target


def get_total_shots_on_target(events):
    """
    Calcule le nombre total de tirs cadrés (on target) par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'shot_outcome' et 'team'.

    Returns:
    - home_on_target (int): Nombre total de tirs cadrés pour l'équipe à domicile.
    - away_on_target (int): Nombre total de tirs cadrés pour l'équipe à l'extérieur.
    """
    # Define outcomes that indicate a shot was on target
    on_target_outcomes = ['Goal', 'Saved', 'Saved To Post', 'Shot Saved Off Target']
    
    # Filter the events DataFrame for shots on target
    data = events[events['shot_outcome'].isin(on_target_outcomes)]
    
    # Group by 'team' and count the number of on-target shots
    on_target_counts = data.groupby('team').size()
    
    # Return the counts for the two teams
    home_on_target, away_on_target = on_target_counts.iloc[0], on_target_counts.iloc[1]
    
    return home_on_target, away_on_target



def get_total_passes(events):
    """
    Calcule le nombre total de passes par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'pass_outcome' et 'team'.

    Returns:
    - home_passes (int): Nombre total de passes pour l'équipe à domicile.
    - away_passes (int): Nombre total de passes pour l'équipe à l'extérieur.
    """
    # Filtrer les colonnes 'pass_outcome' et 'team', puis grouper par équipe et compter le nombre de passes
    pass_counts = events.filter(regex='^pass_end_location|^team$').groupby('team').count()['pass_end_location']
    
    # Retourner les comptes pour les deux équipes
    home_passes, away_passes = pass_counts.iloc[0], pass_counts.iloc[1]
    
    return home_passes, away_passes

def get_successful_passes(events):
    """
    Calculates the total number of successful passes for home and away teams.

    Parameters:
    - events (pd.DataFrame): DataFrame containing the columns for all passes and pass outcomes.

    Returns:
    - home_successful_passes (int): Successful passes for the home team.
    - away_successful_passes (int): Successful passes for the away team.
    """
    # Get the total passes using the get_total_passes function
    home_passes, away_passes = get_total_passes(events)
    
    # Identify unsuccessful passes based on 'type' or another column indicating unsuccessful outcomes
    unsuccessful_passes = events.filter(regex='^pass_outcome|^team$').groupby('team').count().reset_index()['pass_outcome']
    
    # Calculate successful passes by subtracting unsuccessful passes from total passes
    home_unsuccessful_passes = unsuccessful_passes.iloc[0]
    away_unsuccessful_passes = unsuccessful_passes.iloc[1]
    
    home_successful_passes = home_passes - home_unsuccessful_passes
    away_successful_passes = away_passes - away_unsuccessful_passes
    
    return home_successful_passes, away_successful_passes

def get_total_corners(events):
    """
    Calcule le nombre total de corners par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'pass_type' et 'team'.

    Returns:
    - home_corners (int): Nombre total de corners pour l'équipe à domicile.
    - away_corners (int): Nombre total de corners pour l'équipe à l'extérieur.
    """
    # Filtrer les colonnes 'pass_type' et 'team', puis grouper par équipe et compter le nombre de corners
    corner_counts = events.filter(regex='^pass_type|^team$').query('pass_type == "Corner"').groupby('team').count()['pass_type']
    
    # Extract the team names from the events DataFrame
    teams = events['team'].unique()
    
    # Handle cases where a team might not have any corners
    home_corners = corner_counts.get(teams[0], 0)
    away_corners = corner_counts.get(teams[1], 0)
    
    return home_corners, away_corners



def get_total_fouls(events):
    """
    Calcule le nombre total de fautes par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'team' et 'type'.

    Returns:
    - home_fouls (int): Nombre total de fautes pour l'équipe à domicile.
    - away_fouls (int): Nombre total de fautes pour l'équipe à l'extérieur.
    """
    fouls = events[events['type'] == 'Foul Committed']
    foul_counts = fouls.groupby('team').size()
    home_fouls, away_fouls = foul_counts.iloc[0], foul_counts.iloc[1]
    
    return home_fouls, away_fouls



def get_total_yellow_cards(events):
    """
    Calcule le nombre total de cartons jaunes par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'bad_behaviour_card' et 'team'.

    Returns:
    - home_yellow_cards (int): Nombre total de cartons jaunes pour l'équipe à domicile.
    - away_yellow_cards (int): Nombre total de cartons jaunes pour l'équipe à l'extérieur.
    """
    # Filtrer les colonnes 'bad_behaviour_card' et 'team', puis grouper par équipe et compter le nombre de cartons jaunes
    yellow_card_counts = events.filter(regex='^bad_behaviour_card|^team$').query('bad_behaviour_card == "Yellow Card"').groupby('team').count()['bad_behaviour_card']
    
    # Extraire les noms des équipes de l'événement DataFrame
    teams = events['team'].unique()
    
    # Gérer les cas où une équipe pourrait ne pas avoir de cartons jaunes
    home_yellow_cards = yellow_card_counts.get(teams[0], 0)
    away_yellow_cards = yellow_card_counts.get(teams[1], 0)
    
    return home_yellow_cards, away_yellow_cards

def get_total_red_cards(events):
    """
    Calcule le nombre total de cartons rouges par équipe.

    Parameters:
    - events (pd.DataFrame): DataFrame contenant les colonnes 'bad_behaviour_card' et 'team'.

    Returns:
    - home_red_cards (int): Nombre total de cartons rouges pour l'équipe à domicile.
    - away_red_cards (int): Nombre total de cartons rouges pour l'équipe à l'extérieur.
    """
    # Filtrer les colonnes 'bad_behaviour_card' et 'team', puis grouper par équipe et compter le nombre de cartons rouges
    red_card_counts = events.filter(regex='^bad_behaviour_card|^team$').query('bad_behaviour_card == "Red Card"').groupby('team').count()['bad_behaviour_card']
    
    # Extraire les noms des équipes de l'événement DataFrame
    teams = events['team'].unique()
    
    # Gérer les cas où une équipe pourrait ne pas avoir de cartons rouges
    home_red_cards = red_card_counts.get(teams[0], 0)
    away_red_cards = red_card_counts.get(teams[1], 0)
    
    return home_red_cards, away_red_cards




def display_normalized_scores(home_scores, away_scores, categories, home_color='blue', away_color='green', background_color='lightgray', bar_height=0.8, spacing_factor=2.5):
    """
    Displays a horizontal bar chart with normalized scores for home and away teams.

    Parameters:
    - home_scores: List of scores for the home team.
    - away_scores: List of scores for the away team.
    - categories: List of category names for each score.
    - home_color: Color of the bars representing the home team.
    - away_color: Color of the bars representing the away team.
    - background_color: Color of the background rectangles.
    - bar_height: Height of the bars and background rectangles.
    - spacing_factor: Factor to adjust the spacing between bars.
    """

    # Internal container size variables
    container_width = '50%'  # Adjust width as needed
    container_height = 'auto'  # Adjust height as needed

    # Normalizing the scores
    home_normalized = []
    away_normalized = []
    for home, away in zip(home_scores, away_scores):
        total = home + away
        if total != 0:
            home_normalized.append((home / total) * 100)
            away_normalized.append((away / total) * 100)
        else:
            home_normalized.append(0)
            away_normalized.append(0)

    # Augmenting the spacing between the bars by multiplying y_pos by a factor
    y_pos = np.arange(len(categories)) * spacing_factor

    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))

    # Adding light gray backgrounds for each category with the same height as the bars
    for i in range(len(categories)):
        ax.add_patch(plt.Rectangle((-100, y_pos[i] - bar_height / 2), 200, bar_height, color=background_color, alpha=0.3, linewidth=0))

    # Plotting normalized scores for both teams
    ax.barh(y_pos, home_normalized, height=bar_height, color=home_color, align='center', label='Home Team')
    ax.barh(y_pos, [-score for score in away_normalized], height=bar_height, color=away_color, align='center', label='Away Team')

    # Positioning the category names above the bars to avoid overlap
    for i in range(len(categories)):
        ax.text(0, y_pos[i] + bar_height / 2 + 0.1, categories[i], ha='center', va='bottom', fontsize=10)

    # Adding non-normalized values to the end of the bars
    for i in range(len(categories)):
        ax.text(home_normalized[i] / 2, y_pos[i], f'{home_scores[i]}', va='center', color='white', fontweight='bold')
        ax.text(-away_normalized[i] / 2, y_pos[i], f'{away_scores[i]}', va='center', color='white', fontweight='bold')

    # Adjusting the axis limits
    ax.set_xlim(-100, 100)
    ax.set_ylim(-1, max(y_pos) + spacing_factor)

    # Hiding the spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Removing y-ticks and x-ticks
    ax.set_yticks([])
    ax.set_xticks([])

    # Custom HTML/CSS to control the size of the container
    st.markdown(
        f"""
        <style>
        .resizable-graph-container {{
            width: {container_width}; /* Adjust the width as needed */
            height: {container_height}; /* Adjust the height as needed */
            padding: 10px;
            overflow: auto; /* Handle overflow if the graph is larger than the container */
        }}
        </style>
        <div class="resizable-graph-container">
        """,
        unsafe_allow_html=True
    )

    # Displaying the plot in Streamlit
    st.pyplot(fig)

    # Closing the custom container
    st.markdown('</div>', unsafe_allow_html=True)
