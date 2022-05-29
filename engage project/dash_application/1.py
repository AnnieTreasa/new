'''import pandas as pd
import numpy as np
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
print(df.head())
print(df.corr)
print(df[['bore','stroke','compression-ratio','horsepower']].corr())'''

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv(path) # replace with your own data source
    df = px.data.tips()
    fig = px.scatter(
       df, x="engine-size", y="price", opacity=0.65,
       trendline='ols', trendline_color_override='darkblue'
    )
    fig.show()

app.run_server(debug=True)