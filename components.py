from cards_generator import gen_card
import dash_bootstrap_components as dbc
from dash import dcc, html
from styles import *

def bar(id):
    chart = dbc.Card(
        dbc.CardBody([dcc.Graph(id=id, figure={})]),
    )
    return chart
# ----------------------------------MACHINES--------------------------------------------
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

# ----------------------------------CONTENTS--------------------------------------------
barchart = bar('bar')
linechart = bar('line')

perf_card = dbc.Card(
    dbc.CardBody(html.H2('Performance'), className='align-self-center',
                 style={'text-align': 'center', 'font-size': 'x-large', 'height': 232}),
    color="success",
    outline=True,
)

slider = dcc.Slider(
        id='my-slider',
        min=0,
        max=35,
        step=1,
        value=10,
    )

# ----------------------------------BODIES--------------------------------------------

header = html.Div(className='header', children=[
        html.H2("Header", style={'text-align': 'left', "padding-left": "1rem "}),
        dbc.Nav([]),
    ],
    style=HEADER_STYLE
)

mainspace = html.Div(className='main-space', children=[
        html.H2(id='output_text', children=[], style={'text-align': 'center', "padding": "1rem"}),
        slider,
        barchart,
        html.Br(),
        dbc.Row([dbc.Col(perf_card, width=3, lg=3),
                 dbc.Col(linechart, width=9, lg=9)])
    ],
    style=MAINSPACE_STYLE
)


sidebar = html.Div(className='side-bar', children=[
        html.H2('Sidebar', style={'color': 'white', 'padding-top': '7%'}),
        html.Hr(style={'color': 'white'}),
        dbc.Nav(
            [
                dbc.Row([dbc.Col(X1, width='auto', lg=6),
                         dbc.Col(X2, width='auto', lg=6)], justify='center'),
                dbc.Row([dbc.Col(X3, width='auto', lg=6),
                         dbc.Col(X4, width='auto', lg=6)], justify='center'),
                dbc.Row([dbc.Col(X5, width='auto', lg=6),
                         dbc.Col(X6, width='auto', lg=6)], justify='center'),
                dbc.Row([dbc.Col(X7, width='auto', lg=6),
                         dbc.Col(X8, width='auto', lg=6)], justify='center'),
                dbc.Row([dbc.Col(X9, width='auto', lg=6),
                         dbc.Col(X10, width='auto', lg=6)], justify='center'),
            ],
            navbar=False,
            navbar_scroll=True,
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



