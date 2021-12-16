#--------------------- Packages
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output
from layout_assets.tab_1 import tab_1_layout
from layout_assets.tab_2 import tab_2_layout

import numpy as np
import pandas as pd

# --------------------- Main Layout
"""Main Page of Web Application"""

# Style of Tabs
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'fontSize': '2.5rem'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'fontSize': '2.5rem',
}

# Layout
main_layout = html.Div(
    [
        html.Div(

            # Create Banner Layout (Title and Logos)
            [
                html.Div(
                    [

                        # Input Title of Dashboard, Include title and href link
                        html.H2(
                            id="banner-title",
                            children=[
                                html.A(
                                    "Video Game Recommendation Engine",
                                    href="https://github.com/SulmanK/Video-Game-Recommendation-Engine",
                                    style={
                                        "text-decoration": "none", "color": "inherit", 'padding-left': '55rem'},
                                )
                            ]
                        ),

                        # Insert Github Logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "github_logo.png"))
                            ], href="https://github.com/SulmanK/Video-Game-Recommendation-Engine",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "dash_banner.png"))
                            ], href="https://dash.plotly.com/",
                        ),
                    ], className="row",
                )
            ], className="banner"
        ),

        # Two Tab Webpage
        html.Div(
            [
                dcc.Tabs(
                    id="tabs-with-classes",
                    value='tab-1-example',
                    parent_className='custom-tabs',
                    className='custom-tabs-container',
                    children=[
                        dcc.Tab(
                            label='About',
                            value='tab-1-example',
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style=tab_style,
                            selected_style=tab_selected_style,
                        ),
                        dcc.Tab(
                            label='Application',
                            value='tab-2-example',
                            className='custom-tab',
                            selected_className='custom-tab--selected',
                            style=tab_style,
                            selected_style=tab_selected_style,
                        ),
                    ]
                ),
            ]
        ),
        html.Div(id='tabs-content-classes'),
    ],  # style = {'maxWidth': '2000px', 'height': '80vh', 'minWidth': '1500px'}
)
# ------------------- Function Callbacks

# Render the multi-tab web application.


@app.callback(
    Output('tabs-content-classes', component_property='children'),
    [Input(component_id='tabs-with-classes', component_property='value'), ]
)
def render_image(tab):
    if tab == 'tab-1-example':
        return tab_1_layout

    elif tab == 'tab-2-example':
        return tab_2_layout
