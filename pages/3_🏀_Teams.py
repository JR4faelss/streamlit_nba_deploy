import streamlit as st
import pandas as pd
from NBA_Teams import nba_teams

st.set_page_config(
    page_title="Teams",
    page_icon="🏀",
    layout="wide",
)

df_data = st.session_state["data"]

seasons = df_data["season"].unique()
season = st.sidebar.selectbox("Season:", seasons)
df_season = df_data[df_data["season"] == season]

teams = df_season["team_abbreviation"].unique()
team = st.sidebar.selectbox("Team:", teams)
df_filtered = df_season[df_season["team_abbreviation"]==team].set_index("player_name")

st.logo(image="Logo-NBA-640x400.png",size="large")

st.markdown(f"## • {nba_teams[team]}")

columns = ["gp","age","pts","reb","ast",
           "oreb_pct","dreb_pct",
           'player_height','player_weight',
           'net_rating','ts_pct','ast_pct',
           'country','college','draft_year','draft_round','draft_number']

st.dataframe(df_filtered[columns],
             column_config={
                "player_name": st.column_config.Column("Nome", width=140),
                "gp": st.column_config.ProgressColumn("Jogos Disputados",min_value=0,format="%d", max_value=82),
                "age": st.column_config.NumberColumn("Idade", format="%d"),
                "pts": st.column_config.NumberColumn("PPG", format="%.1f",help="Pontos por jogo"),
                "reb": st.column_config.NumberColumn("RPG", format="%.1f",help="Rebotes por jogo"),
                "ast": st.column_config.NumberColumn("APG", format="%.1f",help="Assistências por jogo"),
                "oreb_pct":st.column_config.NumberColumn("Off Reb", format="percent",help="Porcentagem de Rebotes Ofensivos"),
                "dreb_pct":st.column_config.NumberColumn("Def Reb", format="percent",help="Porcentagem de Rebotes Defensivos"),
                "player_height": st.column_config.NumberColumn("Altura", format="%d cm"),
                "player_weight": st.column_config.NumberColumn("Peso", format="%d kg"),
                "net_rating": st.column_config.NumberColumn("Net Rating", format="%1f",help="Pontuação Líquida do Jogador"),
                "country": st.column_config.Column("País", width="small",help="País de Origem"),
                "college": st.column_config.Column("College", width=160,help="Universidade que Jogou"),
                "draft_year": st.column_config.Column("Ano de Draft", width="small"),
                "draft_round": st.column_config.Column("Rodada do Draft", width="small"),
                "draft_number": st.column_config.Column("Posição do Draft"),
                "ts_pct": st.column_config.NumberColumn("True Shot %", format="percent",help="Porcentagem de Arremessos Verdadeiros"),
                "ast_pct": st.column_config.NumberColumn("Assist %", format="percent",help="Porcentagem de Assistências Verdadeiras")
             })