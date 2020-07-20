#--------------------- Packages
from app import app
from dash.dependencies import Input, Output, State
from layout_assets.datatable import datatable_asset
from layout_assets.game_logos import game_logos_asset
from layout_assets.tf_idf_bar import tf_idf_bar_asset
from layout_assets.wordcloud import wordcloud_asset
from model.preprocessing import df
from model.knn import knn_game_recommendations
from model.knn_svd import knnsvd_game_recommendations

import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import pandas as pd


#--------------------- Tab 2
"""Second Tab of Plotly Dash Web Application"""
# game_list input for dropdown
game_list = [x for x in df['name']]

# Tab 2
tab_2_layout = html.Div(
    [
        # Heading for game input and dropdown
        html.Div(
            [
                dcc.Markdown('### Select up to five video games.'),
                dcc.Dropdown(
                    id = 'Games',
                    options = [{'label': game, 'value': game} for game in game_list],
                    value = [],
                    multi = True, 
                    placeholder = "Select a video game.",
                    style = {'color': '#f7f7f7', 'width': '97.4%', 'fontSize': '2.5rem'}
                ),
                dcc.Markdown('### Select a recommendation method.'),
            ], style = {"padding-left" : "2rem"}
        ),
        
        # Heading for recommendations methods, dropdown, and button
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id = 'Recommendation_Methods',
                            options = [
                                {'label': 'K-Nearest Neighbors', 'value': 'KNN'},
                                {'label': 'K-Nearest Neighbors + SVD', 'value': 'KNN+SVD'},
                            ],
                            placeholder = "Select an algorithm.",
                            value = 'RA',
                        style = {'width': '80%', 'color': '#f7f7f7',
                                 'fontSize': '2.0rem',  "padding-left" : "2rem"},
                        ),
                    ], className = 'nine columns'
                ),
                html.Div(
                    [
                        html.Button('Click me for recommendations.', id='Button')
                        
                    ], style = {'padding-right': '10rem', 'padding-bottom': '2px'}, className = 'three columns'
                )
            ], 
        ),
        # Heading for recommendation results
        html.Div(
            [
                html.H3('Recommendations'),
            ], style = {"padding-left": "2rem", "padding-top": "4rem"}
        ),
        
        # Data Table
        html.Div(
            [
                html.Div(
                    [
                        dcc.Loading(
                            id = "loading-1",
                             type = "default",
                            children =  html.Div(id = 'datatable', style = {'fontWeight': 'bold'})
                        ),         
                         
                    ],
                ), 
            ], className = 'row'
        ),
        # Images of recommended titles       
        html.Div( 
                 [
                     html.Div(
                         [
                             dcc.Loading(
                                 id = "loading-2",
                                 type = "default",
                                 children = html.Div(
                                     dcc.Graph(id = 'logo_recommendations')
                                 )
                             )
                         ]
                     ),
                
                 ], className = 'row'
        ),
        
        # Heading for wordcloud and tf-idf distribution
        html.Div(
            [
                html.H3('Text Visualizations'),
                    
            ], style = {"padding-left": "2rem"}
        ),
        
        # Split into two columns
        html.Div(
            [
                dcc.Loading(
                    id = "loading-3",
                    type = "default",
                    children = html.Div(id = 'wc_image')
                )
            ], className = 'one-half column' 
        ),
        html.Div(
            [
                dcc.Loading(
                    id = "loading-4",
                    type = "default",
                    children = html.Div(
                        dcc.Graph(id ='tf-idf')
                    )
                )
            ], className = 'one-half column'
        ),
    ]
)

# Callback Functions
"""Recommendation Results Callback - Datatable, Wordcloud, logo-recommendations, tf-idf bar distribution and wordcloud."""
@app.callback(
    [Output('datatable', 'children'),
     Output('logo_recommendations', 'figure'),
     Output('tf-idf', 'figure'),
     Output('wc_image', 'children'),
    ],
    
    [Input(component_id = 'Button', component_property = 'n_clicks')],
    
    # Recommendation Method
    [State(component_id = 'Recommendation_Methods', component_property = 'value'),
    
    # Input_Games
    State(component_id = 'Games', component_property = 'value'),
    ],
)


def callback_recommendation_results(Button, Recommendation_Methods, Games):
    """Returns recommendation_results - datatable, game_logos, tf_idf bar distribution and wordcloud."""
    
    # K-Nearest Neighbors
    if (Recommendation_Methods == 'KNN') & (Button != None):
        # 10 titles of recommended games
        results = knn_game_recommendations(df = df, games = Games)
        
        # Create a dataframe of their name, developer, genre, and image_url
        tmp_df = pd.DataFrame(columns = ['name', 'developer',
                                         'genre', 'theme',
                                         'image_url']
                             )
        for x in results:
            tmp = df[df['name'] == x][['name', 'developer', 'genre', 'theme', 'image_url']]
            tmp_df = tmp_df.append(tmp)
            tmp_df = tmp_df.reset_index(drop = True)
        
        # Recommendedation Results
        ## Datatable
        div_datatable = datatable_asset(df = tmp_df)
        
        ## Game Logos
        div_game_logos = game_logos_asset(df = tmp_df)
        
        ## TF-IDF Bar Distribution
        div_tf_idf_bar = tf_idf_bar_asset(df = df, games = Games)
        
        ## Wordcloud
        wc_img = wordcloud_asset(df = df, games = Games)
        div_wc = html.Img(src="data:image/png;base64," + wc_img)
        
        return div_datatable, div_game_logos, div_tf_idf_bar, div_wc
        
    
    # K-Nearest Neighbors + Singular Value Decomposition
    elif (Recommendation_Methods == 'KNN+SVD') & (Button != None):
        # 10 titles of recommended games
        results = knnsvd_game_recommendations(df = df, games = Games)
        
        # Create a dataframe of their name, developer, genre, and image_url
        tmp_df = pd.DataFrame(columns = ['name', 'developer',
                                         'genre', 'theme',
                                         'image_url']
                             )
        for x in results:
            tmp = df[df['name'] == x][['name', 'developer', 'genre', 'theme', 'image_url']]
            tmp_df = tmp_df.append(tmp)
            tmp_df = tmp_df.reset_index(drop = True)
        
        # Recommendedation Results
        ## Datatable
        div_datatable = datatable_asset(df = tmp_df)
        
        ## Game Logos
        div_game_logos = game_logos_asset(df = tmp_df)
        
        ## TF-IDF Bar Distribution
        div_tf_idf_bar = tf_idf_bar_asset(df = df, games = Games)
        
        ## Wordcloud
        wc_img = wordcloud_asset(df = df, games = Games)
        div_wc = html.Img(src="data:image/png;base64," + wc_img)
        
        return div_datatable, div_game_logos, div_tf_idf_bar, div_wc
        
    else:
     
        return 'Select a recommendation method and click the button'
