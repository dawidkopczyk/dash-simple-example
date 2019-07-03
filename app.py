import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

df = pd.read_csv('https://raw.githubusercontent.com/quanteeai/dash-simple-example/master/data/ul_data.csv')

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Unit Linked Funds Performance',
            style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='dropdown-main',
        options=[
            {'label': 'MultiInvestment Fund', 'value': 'Fund1'},
            {'label': 'Global Equity Fund', 'value': 'Fund2'},
            {'label': 'Pension Fund', 'value': 'Fund3'}
        ],
        value='Fund1'),
    dcc.Graph(id='plot-main')])

@app.callback(Output('plot-main', 'figure'),
              [Input('dropdown-main', 'value')])

def update_plot(dropdown_value):
    labels, data = df.Date, df[dropdown_value]
    return {
        'data': [{
            'x': labels,
            'y': data,
            'line': {'width': 3}
        }],
        'layout': {
            'margin': {'l': 50, 'r': 30, 'b': 100, 't': 30}
        }
    }
            
if __name__ == '__main__':
    app.run_server(debug=False)