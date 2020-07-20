#--------------------- Packages
from model.tf_idf import tf_idf_inputs, tf

import numpy as np
import pandas as pd
import plotly.express as px

#--------------------- TF-IDF Distribution (Bar Chart)
def tf_idf_bar_asset(df, games):
    """Function to create a bar graph presenting the distribution of tf-idf values of words."""
    
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
    
    # TF-IDF Transformation
    tf_idf_predictions = tf.transform([str(game_text_strings)])
    
    # Get Feature Labels
    tmp_features = tf.get_feature_names()
    
    # Create Matrix
    prediction_matrix = pd.DataFrame(tf_idf_predictions.todense(), columns = tf.get_feature_names())
    
    # Subset non-zero columns
    non_zero_cols = prediction_matrix.loc[:, (prediction_matrix != 0).all()]
    
    # Sort the columns by highest to lowest
    tmp_col_names = [x for x in non_zero_cols.columns.values]
    tmp_values = non_zero_cols.values
    sorted_values = np.sort(tmp_values[0])
    sorted_columns = []
    
    for x in sorted_values:
        for y in tmp_col_names:
            if ((non_zero_cols[y].values[0] == x) == True) & ((y not in sorted_columns) == True):
                sorted_columns.append(y)
    
    tmp_df = pd.DataFrame({'words' : sorted_columns[::-1],
                           'tf_idf': sorted_values[::-1]})
    
    # Plot
    bar = px.bar(tmp_df, x = 'tf_idf',
                 y = 'words', orientation = 'h',
                 color = 'words', color_discrete_sequence = px.colors.qualitative.Pastel
                )
    
    bar.update_xaxes(linewidth = 1, linecolor = 'black', 
                     gridcolor = 'LightPink', automargin = True,  
                     ticks = "outside", tickwidth = 2,
                     tickcolor = 'black', ticklen = 12,
                     title = 'TF-IDF', title_font = dict(size = 22),
                    ) 
    bar.update_yaxes(linewidth = 1, linecolor = 'black', 
                     gridcolor = 'LightPink', ticks = "outside",
                     tickwidth = 2, tickcolor = 'black',
                     ticklen = 12, title = 'Words',
                     title_font = dict(size = 22),
                    )
    
    
    bar.update_layout(
        title = 'TF-IDF Distribution',
        title_font = dict(size = 26),
        font = dict(size = 18),
        legend = dict(
            x = 1,
            y = 1,
            traceorder = "normal",
            font = dict(
                family = "sans-serif",
                size = 18,
                color = "black"
            ),
            bgcolor = "#f7f7f7",
            bordercolor = "#f7f7f7",
            borderwidth = 1
        ),
        plot_bgcolor = "#f7f7f7", paper_bgcolor = "#f7f7f7",
        width = 925, height = 607, 
        hoverlabel = dict(
            font_size = 24, 
            font_family = "Rockwell")
    )

    return bar