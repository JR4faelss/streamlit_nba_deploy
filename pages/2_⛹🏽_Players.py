import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="⛹🏽",
    layout="wide",
)

df_data = st.session_state["data"]

teams = df_data["team_abbreviation"].unique()
team = st.sidebar.selectbox("Team:", teams)

df_season = df_data[df_data["team_abbreviation"] == team]
seasons = df_season["season"].unique()
season = st.sidebar.selectbox("Season:", seasons)

df_players = df_season[df_season["season"] == season]
players = df_players["player_name"].unique()
player = st.sidebar.selectbox("Player:", players)

player_stats = df_players[df_players["player_name"] == player]

st.logo(image="Logo-NBA-640x400.png",size="large")

st.title(f"• {player_stats["player_name"].values[0]}")

st.divider()

st.markdown("# **Info:**")

col1, col2, col3 = st.columns(3)
col1.markdown(f"### :gray[**Idade**:] {player_stats['age'].values[0]:.0f}")
col2.markdown(f"### :gray[**País:**] {player_stats['country'].values[0]}")
col3.markdown(f"### :gray[**College:**] {player_stats['college'].values[0]}")

col1.markdown(f"### :gray[**Time:**] {player_stats['team_abbreviation'].values[0]}")
col2.markdown(f"### :gray[**Season:**] {player_stats['season'].values[0]}")
col3.markdown(f"### :gray[**Draftado em:**] {player_stats['draft_year'].values[0]}")

st.divider()

st.markdown("# **Stats:**")

col1, col2, col3 = st.columns(3)
if player_stats['pts'].values[0] >= 25:
    col1.markdown(f"### :red[**PPG:**] {player_stats['pts'].values[0]}🔥")
else:
    col1.markdown(f"### :red[**PPG:**] {player_stats['pts'].values[0]}")
if player_stats['reb'].values[0] >= 10:
    col2.markdown(f"### :green[**RPG:**] {player_stats['reb'].values[0]}🔥")
else:
    col2.markdown(f"### :green[**RPG:**] {player_stats['reb'].values[0]}")
if player_stats['ast'].values[0] >= 10:
    col3.markdown(f"### :blue[**APG:**] {player_stats['ast'].values[0]}🔥")
else: 
    col3.markdown(f"### :blue[**APG:**] {player_stats['ast'].values[0]}")

col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns(3)

col1.markdown(f"### :orange[**True Shot:**] {player_stats['ts_pct'].values[0] * 100:.2f}%")
col2.markdown(f"### :violet[**Partidas:**] {player_stats['gp'].values[0]}")
col3.markdown(f"### **Net Rating:** {player_stats['net_rating'].values[0]}")