#--------------------- Packages
from PIL import Image
from plotly.subplots import make_subplots
from urllib.request import urlopen

import numpy as np
import pandas as pd
import plotly.express as px
import urllib
#--------------------- Game Recommendation Logos
def game_logos_asset(df):
    "Function to return jpeg images of the top 10 recommendations in a 2 by 5 grid."
    fig = make_subplots(rows = 2, cols = 5)
    for x,y in zip(range(0, 5), range(1, 6)):
        try:
            tmp_customdata = np.stack((df['name'][x], df['genre'][x])) 
            tmp_url = df['image_url'][x]
            tmp_img = Image.open(urlopen(tmp_url))
            tmp_img = tmp_img.resize((200, 200))
            tmp_fig = px.imshow(tmp_img)
            tmp_trace = tmp_fig['data'][0]
            tmp_fig.update_traces(
                hovertemplate = "<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name = '#' + str(x + 1) 
            )
            fig.add_trace(tmp_trace, row = 1, col = y)
        except urllib.error.HTTPError:
            tmp_customdata = np.stack((df['name'][x], df['genre'][x])) 
            placeholder_url = 'https://giantbomb1.cbsistatic.com/uploads/scale_large/11/110673/3026329-gb_default-16_9.jpg'
            tmp_img = Image.open(urlopen(placeholder_url))	
            tmp_img = tmp_img.resize((200, 200))
            tmp_fig = px.imshow(tmp_img)
            tmp_trace = tmp_fig['data'][0]
            tmp_fig.update_traces(
                hovertemplate = "<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name = '#' + str(x + 1)
            )
            fig.add_trace(tmp_trace, row = 1, col = y)

    for x,y in zip(range(5, 10), range(1, 6)):
        try:
            tmp_customdata = np.stack((df['name'][x], df['genre'][x])) 
            tmp_url = df['image_url'][x]
            tmp_img = Image.open(urlopen(tmp_url))
            tmp_img = tmp_img.resize((200, 200))
            tmp_fig = px.imshow(tmp_img)
            tmp_trace = tmp_fig['data'][0]
            tmp_fig.update_traces(
                hovertemplate = "<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name = '#' + str(x + 1) 
            )
            fig.add_trace(tmp_trace, row = 2, col = y)
        except urllib.error.HTTPError:
            tmp_customdata = np.stack((df['name'][x], df['genre'][x]))
            placeholder_url = 'https://giantbomb1.cbsistatic.com/uploads/scale_large/11/110673/3026329-gb_default-16_9.jpg'
            tmp_img = Image.open(urlopen(placeholder_url))	
            tmp_img = tmp_img.resize((200, 200))
            tmp_fig = px.imshow(tmp_img)
            tmp_trace = tmp_fig['data'][0]
            tmp_fig.update_traces(
                hovertemplate = "<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name = '#' + str(x + 1)
            )
            fig.add_trace(tmp_trace, row = 2, col = y)

    fig.update_xaxes(showticklabels = False)
    fig.update_yaxes(showticklabels = False)
    fig.update_layout(coloraxis_showscale = False, height = 650,
                      plot_bgcolor = '#f7f7f7', paper_bgcolor = '#f7f7f7', 
                      hoverlabel = dict(
                          font_size = 24, 
                          font_family = "Rockwell"))
    
    return fig