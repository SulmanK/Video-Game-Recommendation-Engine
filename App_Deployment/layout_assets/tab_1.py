#--------------------- Packages
from dash import dcc, html


# --------------------- Tab 1
"""First Tab of Plotly Dash Web Application."""
tab_1_layout = html.Div(
    [
        dcc.Markdown(
            ''' 
With the number of products increasing exponentially, it burdens the consumer in which products to purchase. A novel solution is the use of recommender systems (engines) to "recommend" relevant products to the consumers based on their preferences. Applications of recommender systems include areas such as playlist generators for video and music services like Netflix, YouTube, and Spotify. Additionally, product recommendations for services such as Amazon. In this project, we'll explore novel techniques in recommending video games using the Giant Bomb video game database. 

**Process:**

1) _Gather the data from Giant Bomb API._

2) _Preprocess the data._

3) _Exploratory Data Analysis_

4) _Machine Learning_

* _TF-IDF &rarr; K-Nearest Neighbors (+ SVD)_

More information on the technical details is available on the GitHub repository. 

Click the Application Tab on the top of the page to begin!
                    '''
        )
    ], style={'padding': '2rem 4rem 2rem 4rem', 'fontSize': 28,
              'font-family': "Myriad Pro", 'color': "#000000", 'backgroundColor': "#f7f7f7"}
)
