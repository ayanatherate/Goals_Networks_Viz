# -*- coding: utf-8 -*-


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


hide_streamlit_style2= '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container__1QSob{visibility:hidden;}
.viewerBadge_link__1S137{visibility:hidden;}
.css-1rs6os {visibility: hidden;}
.css-17ziqus {visibility: hidden;}
.css-1aumxhk {
background-color: #011839;
background-image: none;
color: #ffffff
}
</style>
'''
st.markdown(hide_streamlit_style2, unsafe_allow_html=True) 

page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpaperaccess.com/full/1092593.png");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
title_html=f'<h1 style="font-family:Calibri; color:#DEF294; font-size: 30px;">Graph Network Visualization of WC 2022 finalists, all Goals and Chances created so far till the Final: Argentina & France</h1>'
st.markdown(title_html, unsafe_allow_html=True)
st.write()



caption2='What exactly are these graph networks?'
write3='The Graphs are interactive. So you can click on any bubble inside the graphs to view the nearest neighbors associated with each player. For example, Lionel Messi has Dybala, Otamendi, Di Maria & others as neighbors in the graph. That means, everytime a Goal Chance (includes Shots, SHots on Goals & Goals) was created by Messi in this World Cup, he was linked with either or more of the players that are in his neighbourhood.'
write4='It goes without saying that Players (nodes) in the graph with the maximum number of edges connected to it have been the players with the most number of Goal Chances & Goals created. More often than not, they are much centrallized in the Graph Structure.'
writeup2_html=f'<h3 style="font-family:Calibri; color:#DBEDEE; font-size: 15px;">{caption2}<br><br>{write3}<br>{write4}</h3>'
st.markdown(writeup2_html, unsafe_allow_html=True)
st.write()
writeup2_html=f'<h3 style="font-family:Calibri; color:#DEF294; font-size: 20px;">Go Ahead, Zoom In and play around with the Visualizations! Best Viewed on Medium Sized to Larger Screens.</h3>'
st.markdown(writeup2_html, unsafe_allow_html=True)


df=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/WC2022finals.github.io/main/Argentina_WC2022.csv")
dff=pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/WC2022finals.github.io/main/France_WC2022.csv")

G = nx.from_pandas_edgelist(df, 'Player', 'Assists', 'xG')
G1 = nx.from_pandas_edgelist(dff, 'Player', 'Player.1', 'xG')

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
got_net1 = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")


# set the physics layout of the network
got_net.from_nx(G)
got_net1.from_nx(G1)

    # Generate network with specific layout settings
got_net.repulsion(node_distance=420,
                   central_gravity=0.33,
                   spring_length=110,
                   spring_strength=0.10,
                   damping=0.95)

got_net1.repulsion(node_distance=420,
                   central_gravity=0.33,
                   spring_length=110,
                   spring_strength=0.10,
                   damping=0.95)






try:
    path = '/tmp'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    got_net1.save_graph(f'{path}/pyvis_graph1.html')
    
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
    HtmlFile1 = open(f'{path}/pyvis_graph1.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    got_net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
    
writeup2_html=f'<h3 style="font-family:Calibri; color:#AAC2EA; font-size: 25px;">ARGENTINA</h3>'
st.markdown(writeup2_html, unsafe_allow_html=True)
components.html(HtmlFile.read(), height=735,width=735)

writeup2_html=f'<h3 style="font-family:Calibri; color:#AAC2EA; font-size: 25px;">FRANCE</h3>'
st.markdown(writeup2_html, unsafe_allow_html=True)
components.html(HtmlFile1.read(), height=735,width=735)

writeup2_html='<style> .link{color:white}</style> <a class="link" href="https://fbref.com/en/squads/b1b36dcd/France-Men-Stats"> Data Scraped from Fbref.com website </a>'
st.markdown(writeup2_html, unsafe_allow_html=True)


     
