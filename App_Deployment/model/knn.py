#--------------------- Packages
from model.tf_idf import tf_idf_inputs, tf
from sklearn.neighbors import NearestNeighbors

import pandas as pd

#--------------------- KNN 
def knn_game_recommendations(df, games):
    """Function to return the top 10 games using K-nearest Neighbors."""
    
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
    
    # TF-IDF Vectorizer (Imported From TF-IDF Module)
    
    # Nearest Neighbors
    nn = NearestNeighbors(n_neighbors = 15, algorithm = 'ball_tree', metric = 'minkowski')
    nn.fit(tf_idf_inputs)
    
    # Transforming the predictions
    tf_idf_predictions = tf.transform([str(game_text_strings)])
    results = nn.kneighbors(tf_idf_predictions.todense())
    
    # Input IDS
    ## Checks for the datatype of the inputted games either None or the title of the game
    input_ids = []
    for x in games:
        if x != None:
            input_ids.append(df[df['name'] == x].index[0])
    
    # Recommended Game ID's
    ## Checks to see if any of the recommended titles are not the inputted games - do not get recommended games you selected
    tmp_ids = [x for x in results[1][0]]
    top_10_ids = []
    for x in tmp_ids:
        if x not in input_ids:
            top_10_ids.append(x)
    
    # The TOP 10 games selected
    ## Returns the title of recommended games    
    
    ## Labeling the name and genre of the top 10_games
    titles = df[['name', 'genre']]
    indices = pd.Series(df.index, index = df['name'])

    return titles.iloc[top_10_ids][0:10]['name'].values
