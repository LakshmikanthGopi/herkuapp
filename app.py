'''import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
 
app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    ),
    html.H1(id='product')  # this is the output
], style={'width':'50%'})
 
@app.callback(
    Output('product', 'children'),
    [Input('range-slider', 'value')])
def update_value(value_list):
    return value_list[0]*value_list[1]
 
if __name__ == '__main__':
    app.run_server(debug=True)'''




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import scipy.stats as st
import statistics as s

!pip install dash==2.0.0

!pip install jupyter-dash -q 
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html



df=pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')


import plotly.express as px


app = JupyterDash(__name__)

server = app.server

fig=px.bar(df,x='winner')

app.layout = html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
