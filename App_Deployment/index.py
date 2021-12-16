from dash.dependencies import Input, Output
from dash import html, dcc


from app import app, server
from layout_assets.main_layout import main_layout

app.layout = html.Div(
    [
        main_layout
    ], style = {'maxWidth': '2000px', 'height': '80vh', 'minWidth': '1500px'}
)


if __name__ == '__main__':
    app.run_server(debug = True)