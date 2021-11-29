from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


def bar(id):
    bar_chart = dbc.Card(
        dbc.CardBody([dcc.Graph(id=id, figure={})]),
    )
    return bar_chart


def line(id):
    line_chart = dcc.Graph(id=id, figure={}, style={'height': '30vh'})
    return line_chart


perf_card = dbc.Card(
    dbc.CardBody(html.H2('Performance'), className='align-self-center',
                 style={'text-align': 'center', 'font-size': 'x-large', 'height': 232}),
    #style={'height': '75%'},
    #inverse=True,
    outline=True,
)
