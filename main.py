import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
from cards_generator import gen_card
from spaces import spaces
from styles import *
from charts_generator import bar, perf_card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='assets')

# ----------------------------------CARDS--------------------------------------------

X1 = gen_card(name='X1', util=10)
X2 = gen_card(name='X2', util=71)
X3 = gen_card(name='X3', util=30)
X4 = gen_card(name='X4', util=13)
X5 = gen_card(name='X5', util=50)
X6 = gen_card(name='X6', util=25)
X7 = gen_card(name='X7', util=43)
X8 = gen_card(name='X8', util=27)
X9 = gen_card(name='X9', util=11)
X10 = gen_card(name='X10', util=74)

card_graph = dbc.Card(
    dcc.Graph(id='my_bar', figure={'data': [{'x': [1, 2, 3, 4, 5], 'y': [20, 21, 19, 28, 35], 'type': 'bar'}
                                            ]
                                   }
              )
)

# ----------------------------------APP LAYOUT------------------------------------------
header = html.Div(className='header', children=[
    html.H2("Header", style={'text-align': 'left', "padding-left": "1rem "}),
    dbc.Nav([]),
],
                  style=HEADER_STYLE

                  )

barchart = bar('bar')
linechart = bar('line')
mainspace = html.Div(className='main-space', children=
[
    html.H2(id='output_text', children=[], style={'text-align': 'center', "padding": "1rem"}),
    #html.P(id='output_text', children=[]),
    #dbc.Row([barchart], class_name='h-30'),
    barchart,
    html.Br(),
    #dbc.Row(dbc.CardGroup([perf_card, linechart]), style={'height': '20%'}),
    dbc.Row([dbc.Col(perf_card, width=3, lg=3),
             dbc.Col(linechart, width=9, lg=9)])
],
                     style=MAINSPACE_STYLE
                     )

sidebar = html.Div(className='side-bar', children=
[
    html.H2('Sidebar', style={'color': 'white'}),
    html.Hr(style={'color': 'white'}),
    dbc.Nav(
        [
            dbc.Row([dbc.Col(X1, width='auto'),
                     dbc.Col(X2, width='auto')], justify='center'),
            dbc.Row([dbc.Col(X3, width='auto'),
                     dbc.Col(X4, width='auto')], justify='center'),
            dbc.Row([dbc.Col(X5, width='auto'),
                     dbc.Col(X6, width='auto')], justify='center'),
            dbc.Row([dbc.Col(X7, width='auto'),
                     dbc.Col(X8, width='auto')], justify='center'),
            dbc.Row([dbc.Col(X9, width='auto'),
                     dbc.Col(X10, width='auto')], justify='center'),
        ],
        navbar=False,
        navbar_scroll=True,
        vertical=True,
        pills=True,
    ),
],
                   style=SIDEBAR_STYLE,
                   )

app.layout = html.Div(className='bg', children=[
    dcc.Location(id="url"),
    #header,
    mainspace,
    sidebar,

],
                      style=BACK_STYLE
                      )


# -------------------------------------------------------------------------------------
@app.callback(
    [Output(component_id='output_text', component_property='children'),
    Output(component_id='bar', component_property='figure'),
    Output(component_id='line', component_property='figure')],
    # Input(component_id='buttonX1', component_property='X1')
    Input("url", "pathname")
)
def render_page_content(pathname):
    name = pathname[1:]
    if pathname == '/'+name:
        text = name

        x = np.arange(10)
        rand = np.random.randint(30, size=10)
        bar = px.bar(x=x, y=x*rand, height=300)
        bar.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            margin=dict(t=0, l=5, b=5, r=0)
        )
        line = px.line(x=x, y=x * rand, height=200)
        line.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            margin=dict(t=0, l=5, b=5, r=0)
        )

        return text, bar, line


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
