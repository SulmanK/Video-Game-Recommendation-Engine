#--------------------- Packages
from dash import dash_table

import pandas as pd


#--------------------- Datatable
def datatable_asset(df):
    """Function to create a datatable which is used to return the top 10 titles."""
    datatable = dash_table.DataTable(
        id='typing_formatting_1',
        data=df.to_dict('records'),
        columns=[
            {
                'id': 'name',
                'name': 'Title',
                'type': 'text'
            },

            {
                'id': 'developer',
                'name': 'Developer',
                'type': 'text'
            },

            {
                'id': 'genre',
                'name': 'Genre(s)',
                'type': 'text'
            },

            {
                'id': 'theme',
                'name': 'Theme(s)',
                'type': 'text'
            },

        ],

        # Highlight Cells based on conditions - first, second, and third row
        style_data_conditional=[
            {
                "if": {"row_index": 0},
                "backgroundColor": "#FFD700",
                'color': 'black'
            },

            {
                "if": {"row_index": 1},
                "backgroundColor": "#C0C0C0",
                'color': 'black'

            },

            {
                "if": {"row_index": 2},
                "backgroundColor": "#CD7F32",
                'color': 'black'

            }
        ],

        # Formatting the data/headers cells
        style_cell={'backgroundColor': '#f7f7f7', 'font-family': 'helvetica',
                    'fontColor': '#000000', 'fontSize': 24
                    },

        style_data={'border': '1px solid #00a8ff', 'font-size': 24,
                    'font-family': 'helvetica'
                    },

        style_header={'border': '1px solid #00a8ff', 'font-size': 28,
                      'font-family': 'helvetica'
                      },

        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",

    )
    return datatable
