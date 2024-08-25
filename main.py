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
    matches = one_team_matches['match_id']


    selected_match = st.selectbox(
        "Choose your match",
        matches,
    )
    selected_one_team_matches = one_team_matches[one_team_matches['match_id']==selected_match]
    match_id = selected_one_team_matches['match_id'].iloc[0]
    st.write(selected_one_team_matches)

    home_team = selected_one_team_matches['home_team'].iloc[0]
    away_team = selected_one_team_matches['away_team'].iloc[0]

    home_lineups = sb.lineups(match_id=match_id)[home_team]
    away_lineups = sb.lineups(match_id=match_id)[away_team]
    events = sb.events(match_id=match_id)


with col2:
    col21, col22 = st.columns([1,1])

    position_id_to_coordinates_home = clp.initial_player_position_allpitch_home
    position_id_to_coordinates_away = clp.initial_player_position_allpitch_away
    # functions.display_player_names_and_positions_twoTeam(home_lineups, away_lineups, position_id_to_coordinates_home, position_id_to_coordinates_away)
    
    with col21:
        functions.display_player_names_and_positions_oneTeam(home_lineups, position_id_to_coordinates_home)

    with col22:
        functions.display_player_names_and_positions_oneTeam(away_lineups, position_id_to_coordinates_away)



# st.image('https://raw.githubusercontent.com/luukhopman/football-logos/master/logos/FR1/AS%20Monaco.png')



