import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd
from dash.dependencies import Output, Input

import numpy as np

#%matplotlib inline
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Make": ["Tata Motors", "Mahindra", "Kia Motors", "Toyota", "Renault", "Honda"],
        "Amount": [42293, 27603, 22622, 17131, 8518, 6589],
        
    }
)


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")
    dash_app.layout = html.Div(
        children=[
            html.H1(children="Sales"),
            html.Div(
                children="""
            Top 10 Best Selling Car Brands In India: March 2022.
        """
            ),
            dcc.Graph(
                id="example-graph",
                figure=px.bar(df, x="Make", y="Amount", barmode="group"),
            ),
        ]
    )

    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

'''    
df = pd.read_csv('engage project\dash_application\Sales_table.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=["Tata Motors", "Mahindra", "Kia Motors", "Toyota", "Renault", "Honda"], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df.Maker.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  )
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.Maker.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='Genmodel_ID', y='2020', color='Maker',
                  custom_data=['Maker', 'Genmodel_ID', '', 'pop'])
    fig.update_traces(mode='lines+markers')
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.Maker.isin(country_chosen)]
        dff2 = dff2[dff2.Genmodel_ID == 'BMW']
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='pop', names='Maker',
                      title='for BMW')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.Maker.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.Genmodel_ID == hov_year]
        fig2 = px.pie(data_frame=dff2, values='pop', names='Maker', title=f'Population for: {hov_year}')
        return fig2

if __name__ == '__main__':
    app.run_server(debug=True)
    '''