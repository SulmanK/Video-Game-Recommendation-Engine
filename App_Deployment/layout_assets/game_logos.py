# --------------------- Packages
from plotly.subplots import make_subplots
from skimage import io
from skimage.transform import resize
from skimage.color import rgba2rgb
from urllib.request import urlopen

import numpy as np
import pandas as pd
import plotly.express as px
import urllib
# --------------------- Game Recommendation Logos


def game_logos_asset(df):
    "Function to return jpeg images of the top 10 recommendations in a 2 by 5 grid."

    # Create 2 x 5 grid  figure object
    fig = make_subplots(rows=2, cols=5)

    # Iterate through the first row (1 x 5) grid and populate with game logos
    for x, y in zip(range(0, 5), range(1, 6)):
        # Try assertion
        try:
            # Create information for our hover tooltip
            tmp_customdata = np.stack((df['name'][x], df['genre'][x]))

            # URL object of a specific game
            tmp_url = df['image_url'][x]

            # Read image from url
            tmp_img = io.imread(tmp_url)

            # Resize image to 200 x 200
            tmp_img = resize(tmp_img, (200, 200))

            # Now, we must check whether our images are RGBA, if so we must convert to RGB
            # Check if shape matches RGB (RGB can be (M, N) or (M, N, 3) )
            if len(tmp_img.shape) == 2:

                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )
                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=1, col=y)

            # Check if shape is RGB but not RGBA
            elif (len(tmp_img.shape) == 3) & (tmp_img.shape[2] != 4):

                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )
                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=1, col=y)

            # Check the image is a RGBA
            else:

                # Convert to RGB
                tmp_img = rgba2rgb(tmp_img)

                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )

                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=1, col=y)

        # Execute this block if we have recieve url error codes
        except urllib.error.HTTPError:
            # Create information for our hover tooltip
            tmp_customdata = np.stack((df['name'][x], df['genre'][x]))

            # Create our placeholder URL
            placeholder_url = 'https://cdn.shopify.com/s/files/1/0021/8972/products/Logo_T-Shirt2_600x.png?v=1488325804'

            # Read image from url
            tmp_img = io.imread(placeholder_url)

            # Resize image to 200 x 200
            tmp_img = resize(tmp_img, (200, 200))

            # Convert to RGB
            tmp_img = rgba2rgb(tmp_img)

            # Create a plotly express figure object
            tmp_fig = px.imshow(tmp_img)

            # Create an individual trace of the above figure for our grid
            tmp_trace = tmp_fig['data'][0]

            # Append that trace with the tmp_customdata (hover data)
            tmp_fig.update_traces(
                hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name='#' + str(x + 1)
            )

            # Add the trace to our grid
            fig.add_trace(tmp_trace, row=1, col=y)

    # Iterate through the second row (1 x 5) grid and populate with game logos
    for x, y in zip(range(5, 10), range(1, 6)):
        # Try assertion
        try:
            # Create information for our hover tooltip
            tmp_customdata = np.stack((df['name'][x], df['genre'][x]))

            # URL object of a specific game
            tmp_url = df['image_url'][x]

            # Read image from url
            tmp_img = io.imread(tmp_url)

            # Resize image to 200 x 200
            tmp_img = resize(tmp_img, (200, 200))

            # Now, we must check whether our images are RGBA, if so we must convert to RGB
            # Check if shape matches RGB (RGB can be (M, N) or (M, N, 3) )
            if len(tmp_img.shape) == 2:

                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )
                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=2, col=y)

            # Check if shape matches RGB and not RGBA
            elif (len(tmp_img.shape) == 3) & (tmp_img.shape[2] != 4):
                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )
                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=2, col=y)

            # Check if the img is RGBA
            else:

                # Convert from RGBA to RGB
                tmp_img = rgba2rgb(tmp_img)

                # Create a plotly express figure object
                tmp_fig = px.imshow(tmp_img)

                # Create an individual trace of the above figure for our grid
                tmp_trace = tmp_fig['data'][0]

                # Append that trace with the tmp_customdata (hover data)
                tmp_fig.update_traces(
                    hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                    "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                    name='#' + str(x + 1)
                )

                # Add the trace to our grid
                fig.add_trace(tmp_trace, row=2, col=y)

        # Execute this block if we have recieve url error codes
        except urllib.error.HTTPError:
            # Create information for our hover tooltip
            tmp_customdata = np.stack((df['name'][x], df['genre'][x]))

            # Create our placeholder URL
            placeholder_url = 'https://cdn.shopify.com/s/files/1/0021/8972/products/Logo_T-Shirt2_600x.png?v=1488325804'

            # Read image from url
            tmp_img = io.imread(placeholder_url)

            # Resize image to 200 x 200
            tmp_img = resize(tmp_img, (200, 200))

            # Convert from RGBA to RGB
            tmp_img = rgba2rgb(tmp_img)

            # Create a plotly express figure object
            tmp_fig = px.imshow(tmp_img)

            # Create an individual trace of the above figure for our grid
            tmp_trace = tmp_fig['data'][0]

            # Append that trace with the tmp_customdata (hover data)
            tmp_fig.update_traces(
                hovertemplate="<b>Title:</b>" + " " + str(tmp_customdata[0]) +
                "<br><b>Genre:</b>" + " " + str(tmp_customdata[1]),
                name='#' + str(x + 1)
            )

            # Add the trace to our grid
            fig.add_trace(tmp_trace, row=2, col=y)

    # Update figure parameters
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_layout(coloraxis_showscale=False, height=650,
                      plot_bgcolor='#f7f7f7', paper_bgcolor='#f7f7f7',
                      hoverlabel=dict(
                          font_size=24,
                          font_family="Rockwell"))

    return fig
