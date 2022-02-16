import altair as alt 
import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output


movies = pd.read_json("./data/movies.json")

app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.layout = html.Div([
    "万実がちゃん大好きなレベル",
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='vote_average',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in movies.select_dtypes(include=np.number).columns]),
    dcc.Dropdown(
        id='colour-widget',
        value='studios',  # REQUIRED to show the plot on the first page load
        options=[{'label': "Studios", 'value': "studios"}, {'label': "Genres", 'value': "genres"}])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('colour-widget', 'value'))
def plot_altair(xcol, colour):
    chart = alt.Chart(movies).mark_point().encode(
        x=xcol,
        y='vote_average',
        color=colour,
        tooltip='vote_average').interactive()
    return chart.to_html()

if __name__ == '__main__': 
    app.run_server(debug=False)