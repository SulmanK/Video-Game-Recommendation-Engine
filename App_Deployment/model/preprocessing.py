#--------------------- Packages
import numpy as np
import pandas as pd
import psycopg2
import re


# --------------------- Pandas Dataframe
""" Script to load in the csv, preprocess the data and create a new feature called the total contents to be used as an input for text mining"""
## Read in CSV
DATABASE_URL = 'postgres://tmvczjjiivxgis:686b1d6bf3bcabceeaefcdd83fd5b382fb20c6e55ed653b4f9f3cd3516af5e7b@ec2-54-211-210-149.compute-1.amazonaws.com:5432/d3g6rt4h59b8fv'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
df = pd.read_sql('select * from video_games', con=conn, index_col='index')
conn.close()


# Preprocessing
# Drop entries that don't have a genre, theme, and concept value.
df = df.loc[(df['genre'] != 'None') & (df['theme'] != 'None')
            & (df['concept'] != 'None')].copy()

# Drop entries that are related to anime and adult.
df = df[(~df['theme'].str.contains("Anime")) &
        (~df['theme'].str.contains("Adult"))]
df = df.reset_index(drop=True)

# Apply text processing across various columns.
column_list = ['original_game_rating', 'original_release_date_', 'platform',
               'developer', 'genre', 'theme', 'concept', 'franchise']


# Function to label a column as None
def NONE(x):
    """Function to label a column as None if there are no contents."""
    if x == 'None':
        x = ''
        return x
    else:
        return x


# for x in df.columns[2:]:
for x in column_list:
    df[x] = df[x].apply(str)

    # If a column has no contents, it is labeled as none.
    df[x] = df[x].apply(NONE)

    # Remove Brackets
    df[x] = df[x].apply(lambda i: i.strip('[]'))

    # Strip quotation marks
    df[x] = df[x].apply(lambda i: i.strip("''"))
    df[x] = df[x].apply(lambda i: i.strip('""'))
    df[x] = df[x].apply(lambda i: re.sub('"', '', i))
    df[x] = df[x].apply(lambda i: re.sub("'", '', i))

    # Remove Whitespace between multiple string values
    df[x] = df[x].apply(lambda i: i.replace('  ', ' '))

    # Fix ','
    df[x] = df[x].apply(lambda i: i.replace("','", ' '))

    # Fix ","
    df[x] = df[x].apply(lambda i: i.replace('","', ' '))
    df[x] = df[x].apply(lambda i: i.replace(',', ' '))

    # Fix Genre Action Adventure

    # Fix '-'
    df[x] = df[x].apply(lambda i: i.replace('-', ' '))


# Total Content Description
df['total_contents'] = df['original_game_rating'] + " " + df['developer'] + " " + df['genre'] + \
    " " + df['theme'] + " " + df['concept'] + \
    " " + df['franchise'] + " " + df['platform']
