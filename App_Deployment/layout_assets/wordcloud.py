#--------------------- Packages
from io import BytesIO
from wordcloud import WordCloud

import base64
import numpy as np
import pandas as pd

#--------------------- WordCloud
def wordcloud_asset(df, games):
    """Function to create and plot a worcloud."""
    # Iterate through each game selected and append the game's description into a list  
    game_text_list = []
    for x in games:
        if (x != None) & (df['name'].isin([x]).any() == True):
            game_text_list.append(((df[df['name'] == x]['total_contents'].values)))
        elif (x != None) & (df['name'].isin([x]).any() == False):
            return('Game inputted is not in dataset')
    
    # Concatenate the strings
    game_text_strings = ''
    for x in game_text_list:
        game_text_strings += x 
    
    # The regex expression is used to eliminate all non english letters
    regex_expression = r"[a-zA-Z]+"
    
    wc = WordCloud(width = 800, height = 600,
                   max_words = 10000, min_font_size = 18, 
                   relative_scaling = 0, background_color = '#f7f7f7',
                   contour_color = "black", regexp = regex_expression,
                   random_state = 2, colormap = 'cool',
                   collocations = False).generate(game_text_strings[0])
    
    wc_img = wc.to_image()
    with BytesIO() as buffer:
        wc_img.save(buffer, 'png')
        final_img = base64.b64encode(buffer.getvalue()).decode()
    
    return final_img