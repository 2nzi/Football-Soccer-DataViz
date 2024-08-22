import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import requests
from statsbombpy import sb
from mplsoccer import Pitch
import matplotlib.pyplot as plt

competition = sb.competitions()

#Gender Choice
# on = st.toggle("Men" if st.session_state.get('competition_gender', 'women') == 'women' else "Women")
# competition_gender = 'men' if on else 'women'
# st.session_state.competition_gender = competition_gender
competition_gender = "male"

competition_gender_df = competition[competition['competition_gender']==competition_gender]
# st.write(competition_gender_df)

#Competition Choice
# competitions = competition['competition_name'].str.replace(r'^1\.\s*', '', regex=True).unique()
competitions = competition_gender_df['competition_name'].unique()
selected_competition = st.selectbox(
    "Choose your competition",
    competitions,
)
selected_competition_df = competition_gender_df[competition_gender_df['competition_name']==selected_competition]
# st.write(selected_competition_df)

#Season Choice
seasons = selected_competition_df['season_name'].unique()
selected_season = st.selectbox(
    "Choose your season",
    seasons,
)

competition_id = selected_competition_df[selected_competition_df['season_name']==selected_season]['competition_id'].iloc[0]
season_id = selected_competition_df[selected_competition_df['season_name']==selected_season]['season_id'].iloc[0]

matches = sb.matches(competition_id=competition_id, season_id=season_id)
# st.write(matches)


#Season Choice
# teams = selected_competition_df[['home_team','away_team']].unique()
teams = pd.concat([matches['away_team'], matches['home_team']]).unique()
selected_team = st.selectbox(
    "Choose your team",
    teams,
)
one_team_matches = matches[(matches['home_team'] == selected_team) | (matches['away_team'] == selected_team)]
# st.write(one_team_matches)

matches = one_team_matches['match_id']

selected_match = st.selectbox(
    "Choose your match",
    matches,
)

selected_one_team_matches = one_team_matches[one_team_matches['match_id']==selected_match]
match_id = selected_one_team_matches['match_id'].iloc[0]
# st.write(selected_one_team_matches)

home_team = selected_one_team_matches['home_team'].iloc[0]
away_team = selected_one_team_matches['away_team'].iloc[0]

home_lineups = sb.lineups(match_id=match_id)[home_team]
away_lineups = sb.lineups(match_id=match_id)[away_team]

# st.write(home_lineups)
# st.write(away_lineups)


events = sb.events(match_id=match_id)

pitch_width = 120
pitch_height = 80
nb_line = 7
space_line = (pitch_width/2)/7
space_col = (pitch_height)/7

x_line1 = 5
x_line2 = x_line1 + space_line
x_line3 = x_line2 + space_line
x_line4 = x_line3 + space_line
x_line5 = x_line4 + space_line
x_line6 = x_line5 + space_line
x_line7 = x_line6 + space_line

x_col1 = 5
x_col2 = x_line1 + space_line
x_col3 = x_line2 + space_line
x_col4 = x_line3 + space_line
x_col5 = x_line4 + space_line
x_col6 = x_line5 + space_line
x_col7 = x_line6 + space_line

position_id_to_coordinates_home = {
    1: (x_line1, 40),
    2: (x_line2, 70),
    3: (x_line2, 55),
    4: (x_line2, 40),
    5: (x_line2, 25),
    6: (x_line2, 10),
    7: (x_line3, 70),
    8: (x_line3, 10),
    9: (x_line3, 55),
    10: (x_line3, 40),
    11: (x_line3, 25),
    12: (x_line4, 70),
    13: (x_line4, 55),
    14: (x_line4, 40),
    15: (x_line4, 25),
    16: (x_line4, 10),
    17: (x_line5, 70),
    18: (x_line5, 55),
    19: (x_line5, 40),
    20: (x_line5, 25),
    21: (x_line5, 10),
    22: (x_line7, 55),
    23: (x_line7, 40),
    24: (x_line7, 25),
    25: (x_line6, 40)
}

position_id_to_coordinates_away = {1: (115.0, 40), 2: (106.42857142857143, 70), 3: (106.42857142857143, 55), 4: (106.42857142857143, 40), 5: (106.42857142857143, 25), 6: (106.42857142857143, 10), 7: (97.85714285714286, 70), 8: (97.85714285714286, 10), 9: (97.85714285714286, 55), 10: (97.85714285714286, 40), 11: (97.85714285714286, 25), 12: (89.28571428571428, 70), 13: (89.28571428571428, 55), 14: (89.28571428571428, 40), 15: (89.28571428571428, 25), 16: (89.28571428571428, 10), 17: (80.71428571428572, 70), 18: (80.71428571428572, 55), 19: (80.71428571428572, 40), 20: (80.71428571428572, 25), 21: (80.71428571428572, 10), 22: (63.57142857142858, 55), 23: (63.57142857142858, 40), 24: (63.57142857142858, 25), 25: (72.14285714285714, 40)}

def display_player_names_and_positions(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away):
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
        pitch_color='#1f77b4', 
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

# Example usage with the provided lineups (assuming home_lineups and away_lineups are your DataFrames)
display_player_names_and_positions(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away)


# st.image('https://raw.githubusercontent.com/luukhopman/football-logos/master/logos/FR1/AS%20Monaco.png')
