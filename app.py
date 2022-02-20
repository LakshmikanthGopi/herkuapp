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



import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px



df=pd.read_csv('https://raw.githubusercontent.com/srinathkr07/IPL-Data-Analysis/master/matches.csv')



app = dash.Dash(__name__)

server = app.server

fig=px.bar(df,x='winner')

app.layout = html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)
