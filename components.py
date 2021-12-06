from cards_generator import gen_card
import dash_bootstrap_components as dbc
from datetime import datetime as dt
from dash import dcc, html
from styles import *

def bar(id):
    chart = dbc.Card(
        dbc.CardBody([dcc.Graph(id=id, figure={})], style={'background-color':'rgba(221,220,220, 0.2)'})
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
timeline = bar('time')

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

date_start = dcc.DatePickerSingle(
        id='date-picker-start',
        min_date_allowed=dt(2021, 12, 2).date(),
        max_date_allowed=dt(2022, 12, 2).date(),
        initial_visible_month=dt(2022, 6, 2).date(),
        date=dt(2022, 6, 2).date(),
        style={'margin-top':'10%'}
    )

date_end = dcc.DatePickerSingle(
        id='date-picker-end',
        min_date_allowed=dt(2021, 12, 2).date(),
        max_date_allowed=dt(2022, 12, 2).date(),
        initial_visible_month=dt(2022, 12, 2).date(),
        date=dt(2022, 12, 2).date(),
        style={'margin-top':'10%'}
    )

freq_menu = dcc.Dropdown(
    options=[
            {'label': 'Daily', 'value': 'daily'},
            {'label': 'Weekly', 'value': 'weekly'},
        ],
    value='daily',
    searchable=False,
    clearable=False,
    style={'margin-top':'18%'}
)

download_but = dbc.Button("Download", color="primary", style={'width':'70%',"margin-top": "5%", 'fontSize': 25})

alert = dbc.Alert(
    "'Start' date must be prior to 'End' date.",
    id="alert-fade",
    dismissable=True,
    is_open=False,
    color="danger",
    style={'fontSize': 25}
)

# ----------------------------------BODIES--------------------------------------------

header = html.Div(className='header', children=[
        html.H2("Header", style={'text-align': 'left', "padding-left": "1rem"}),
        dbc.Nav([]),
    ],
    style=HEADER_STYLE
)

start = html.Div(children=[dbc.Row([
            dbc.Col(html.Plaintext('Start', style={'fontSize': 25}), width='auto'),
            dbc.Col(date_start, width='auto')], justify='center'
    )]
)

end = html.Div(children=[dbc.Row([
            dbc.Col(html.Plaintext('End', style={'fontSize': 25}), width='auto'),
            dbc.Col(date_end, width='auto')], justify='center'
    )]
)

freq = html.Div(children=[dbc.Row([
            dbc.Col(html.Plaintext('Frequency', style={'fontSize': 25}), width='auto'),
            dbc.Col(freq_menu, width='4')], justify='center'
    )]
)

dates_space = html.Div(children=[
    dbc.Row([
             dbc.Col(start, width='3'),
             dbc.Col(end, width='2'),
             dbc.Col(freq, width='4'),
             dbc.Col(download_but)]),

    ],
    style = {'width': '100%','background-color': 'rgba(192,192,192,1)', 'padding-top': '1%', 'padding-bottom': '0.3%'
    }
)

mainspace = html.Div(className='main-space', children=[
        html.H2(id='output_text', children=[], style={'text-align': 'center', 'font-size':80}),
        html.Hr(),
        dates_space,
        alert,
        html.P(),
        barchart,
        html.Br(),
        slider,
        dbc.Row([dbc.Col(perf_card, width=3, lg=3),
                 dbc.Col(linechart, width=9, lg=9)])
    ],
    style=MAINSPACE_STYLE
)


sidebar = html.Div(className='side-bar', children=[
        html.H2('Sidebar', style={'padding-top': '7%'}),
        html.Hr(),
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



