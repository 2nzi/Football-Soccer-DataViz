from mplsoccer import Pitch
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



def display_player_names_and_positions_oneTeam(home_lineups, position_id_to_coordinates_home):
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
        ax.scatter(x_coords_home, y_coords_home, color='red', s=300, edgecolors='white', zorder=3)

        for position_id, (x, y) in coordinates_dict_home.items():
            name = player_names_dict_home.get(position_id, "Unknown")
            ax.text(x, y - 4, f'{name.split()[-1]}', color='black', ha='center', va='center', fontsize=12, zorder=6)

    # Display the plot in Streamlit
    st.pyplot(fig)
