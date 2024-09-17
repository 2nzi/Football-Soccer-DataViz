import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import requests
from statsbombpy import sb
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import config_location_player as clp
import functions
import Pitch3D
import json
import numpy as np

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 20%; /* Adjust this percentage to resize the image */
    }
    .ban-image {
        display: block;
        margin-left: 0;
        margin-right: 0;
        width: 100%; /* Adjust this percentage to resize the image */
        height: 50%; /* Adjust this percentage to resize the image */
    }
    .banner-image {
        background-image: url('https://statsbomb.com/wp-content/uploads/2023/03/IconLockup_MediaPack-min.png');
        background-size: cover;
        background-position: center;
        height: 300px; /* Adjust the height to your preference */
        width: 100%;
        margin: 0 auto;
        margin-bottom: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="banner-image"></div>', unsafe_allow_html=True)


# st.markdown(
#     '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsmWldT7_OE2kDhbehYcuTNHzItGFbeH5igw&s" class="centered-image"> <br> <br> <br>',
#     unsafe_allow_html=True
# )



#PARTIE 1 : MATCH CHOOSEN
col1, col2 = st.columns([1, 3])
with col1:

    competition = sb.competitions()

    #Gender Choice
    # on = st.toggle("Men" if st.session_state.get('competition_gender', 'women') == 'women' else "Women")
    # competition_gender = 'men' if on else 'women'
    # st.session_state.competition_gender = competition_gender
    competition_gender = "male"
    competition_gender_df = competition[competition['competition_gender']==competition_gender]



    #Competition Choice
    competitions = competition_gender_df['competition_name'].unique()
    selected_competition = st.selectbox(
        "Choose your competition",
        competitions,
    )
    selected_competition_df = competition_gender_df[competition_gender_df['competition_name']==selected_competition]





    #Season Choice
    seasons = selected_competition_df['season_name'].unique()
    selected_season = st.selectbox(
        "Choose your season",
        seasons,
    )

    competition_id = selected_competition_df[selected_competition_df['season_name']==selected_season]['competition_id'].iloc[0]
    season_id = selected_competition_df[selected_competition_df['season_name']==selected_season]['season_id'].iloc[0]
    matches = sb.matches(competition_id=competition_id, season_id=season_id)


    #Season Choice
    # teams = selected_competition_df[['home_team','away_team']].unique()
    teams = pd.concat([matches['away_team'], matches['home_team']]).unique()
    selected_team = st.selectbox(
        "Choose your team",
        teams,
    )
    one_team_matches = matches[(matches['home_team'] == selected_team) | (matches['away_team'] == selected_team)]
    # matches = one_team_matches['match_id']
    matches = one_team_matches['match_date']

    selected_match = st.selectbox(
        "Choose your match",
        matches,
    )
    selected_one_team_matches = one_team_matches[one_team_matches['match_date']==selected_match]
    match_id = selected_one_team_matches['match_id'].iloc[0]

    home_team = selected_one_team_matches['home_team'].iloc[0]
    home_score = selected_one_team_matches['home_score'].iloc[0]
    home_color = "#0B8494"

    away_team = selected_one_team_matches['away_team'].iloc[0]
    away_score = selected_one_team_matches['away_score'].iloc[0]
    away_color = "#F05A7E" 

    home_lineups = sb.lineups(match_id=match_id)[home_team]
    away_lineups = sb.lineups(match_id=match_id)[away_team]

    events = sb.events(match_id=match_id)
    home_tactic_formation = events['tactics'].iloc[0]['formation']
    away_tactic_formation = events['tactics'].iloc[1]['formation']







#PARTIE 2 : DASHBOARD
with col2:

    st.write(events.filter(regex='^bad_behaviour_card|^team$'))


    home_possession, away_possession = functions.get_possession(events)
    home_xg, away_xg = functions.get_total_xg(events)
    home_shots, away_shots = functions.get_total_shots(events)
    home_off_target, away_off_target = functions.get_total_shots_off_target(events)
    home_on_target, away_on_target = functions.get_total_shots_on_target(events)
    home_passes, away_passes = functions.get_total_passes(events)
    home_successful_passes, away_successful_passes = functions.get_successful_passes(events)
    home_corners, away_corners = functions.get_total_corners(events)
    home_fouls, away_fouls = functions.get_total_fouls(events)
    home_yellow_cards, away_yellow_cards = functions.get_total_yellow_cards(events)
    home_red_cards, away_red_cards = functions.get_total_red_cards(events)

    categories_scores = [
        {"catégorie": "Possession de balle (%)", "Home Team": home_possession, "Away Team": away_possession},
        {"catégorie": "xG (Buts attendus)", "Home Team": home_xg, "Away Team": away_xg},
        {"catégorie": "Tirs", "Home Team": home_shots, "Away Team": away_shots},
        {"catégorie": "Tirs cadrés", "Home Team": home_on_target, "Away Team": away_on_target},
        {"catégorie": "Tirs non cadrés", "Home Team": home_off_target, "Away Team": away_off_target},
        {"catégorie": "Passes", "Home Team": home_passes, "Away Team": away_passes},
        {"catégorie": "Passes réussies", "Home Team": home_successful_passes, "Away Team": away_successful_passes},
        {"catégorie": "Corners", "Home Team": home_corners, "Away Team": away_corners},
        {"catégorie": "Fautes", "Home Team": home_fouls, "Away Team": away_fouls},
        {"catégorie": "Cartons Jaunes", "Home Team": home_yellow_cards, "Away Team": away_yellow_cards},
        {"catégorie": "Cartons Rouges", "Home Team": home_red_cards, "Away Team": away_red_cards},
    ]


    categories = [entry['catégorie'] for entry in categories_scores]
    home_scores = [entry['Home Team'] for entry in categories_scores]
    away_scores = [entry['Away Team'] for entry in categories_scores]


    functions.display_normalized_scores(home_scores, away_scores, categories, home_color, away_color)


    # st.image('img/logo_stade.png', width=200)  
    pitch_color='#d2d2d2',
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <span style='color: {home_color}; margin-right: 30px;'>{home_team} {home_score}</span>
            <span style='margin-right: 30px;'>-</span>
            <span style='color: {away_color};'>{away_score} {away_team}</span>
        </div>
        <div style='text-align: center;'>
            <span style='color: {pitch_color}; margin-right: 30px;'>{home_tactic_formation}</span>
            <span style='margin-right: 30px;'> </span>
            <span style='color: {pitch_color};'>{away_tactic_formation}</span>
        </div>
        """,
        unsafe_allow_html=True
    )


    col21, col22 = st.columns([1,1])

    position_id_to_coordinates_home = clp.initial_player_position_allpitch_home
    position_id_to_coordinates_away = clp.initial_player_position_allpitch_away
    # functions.display_player_names_and_positions_twoTeam(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away)
    
    with open('data/club.json', encoding='utf-8') as f:
        images_data = json.load(f) 

    # Integrate club logo
    home_team_image = functions.get_best_match_image(home_team, images_data)
    away_team_image = functions.get_best_match_image(away_team, images_data)


    with col21:

        # if home_team_image:
        #     st.image(home_team_image)

        functions.display_player_names_and_positions_oneTeam(home_lineups, position_id_to_coordinates_home, home_color)

        st.markdown(
            f"""
            <div style='text-align: center;'>
                <span style='color: {home_color}; margin-right: 30px;'>{selected_one_team_matches['home_managers'].iloc[0]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )     

    with col22:

        # if away_team_image:
        #     st.image(away_team_image)

        functions.display_player_names_and_positions_oneTeam(away_lineups, position_id_to_coordinates_away,away_color)
   
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <span style='color: {away_color}; margin-right: 30px;'>{selected_one_team_matches['away_managers'].iloc[0]}</span>
            </div>
            """,
            unsafe_allow_html=True
        )        


def ensure_3d_coordinates(coord):
    if len(coord) == 2:
        return coord + [0]
    return coord

shot_events = events.filter(regex='^(shot|location|team)').dropna(how='all')
shot_events_location = shot_events[shot_events['shot_end_location'].notna()]

shot_events_location['location'] = shot_events_location['location'].apply(ensure_3d_coordinates)
shot_events_location['shot_end_location'] = shot_events_location['shot_end_location'].apply(ensure_3d_coordinates)

start_points = shot_events_location['location'].tolist()
end_points = shot_events_location['shot_end_location'].tolist()

st.write(shot_events_location)

Pitch3D.main_3D_pitch(start_points,end_points)