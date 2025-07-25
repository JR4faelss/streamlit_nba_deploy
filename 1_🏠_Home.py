import streamlit as st
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("C:/Users/joao_/OneDrive/Área de Trabalho/Asimov Academy/Aplicativos Web com StreamLit/Projeto Streamlit NBA/nbaplayers.csv", index_col=0)
    df_data.sort_values(by="team_abbreviation", ascending=True, inplace=True)
    st.session_state["data"] = df_data

st.sidebar.markdown("Desenvolvido por [JR4faelss](https://github.com/JR4faelss)")

st.logo(image="Logo-NBA-640x400.png",size="large")

st.markdown("# NBA Players Data! 🏀")

st.divider()

st.markdown(
    """
    O conjunto de dados dos jogadores da **NBA** contém informações e estatísticas
    da temporada 1996-97 até a temporada 2019-20. Ele inclui detalhes como
    nome do jogador, time, temporada e várias estatísticas de desempenho.
    
    Este dataset é ideal para entusiastas do basquete, analistas de dados
    e pesquisadores interessados em explorar tendências, estatísticas de desempenho, 
    e a evolução dos jogadores na NBA ao longo do tempo."""
)

st.divider()

st.subheader("Elementos do Dataset:")

st.markdown(
    """
    Nome, Time, Temporada, Jogos Disputados, Idade, País de Origem,
    Altura, Peso, Pontos Por Jogo, Rebotes por Jogo,
    Assistências por Jogo, Universidade que Jogou,
    Ano de Draft, Rodada do Draft, Posição do Draft,
    Net Rating, Porcentagem de Rebotes Ofensivos e Defensivos,
    Usage, Porcentagem de True Shots, Porcentagem de Assistencias.
    """
)
