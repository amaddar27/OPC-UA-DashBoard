from cards_generator import gen_card
import dash_bootstrap_components as dbc
from datetime import datetime as dt
from dash import dcc, html
from styles import *

def bar(id):
    chart = dbc.Card(
        dbc.CardBody([dcc.Graph(id=id, config={'displayModeBar': False},figure={},)])
    )
    return chart
# ----------------------------------MACHINES--------------------------------------------
X1 = gen_card(name='X1', util=10)
X2 = gen_card(name='X2', util=71)
X3 = gen_card(name='X3', util=30)
X4 = gen_card(name='X4', util=13)
X5 = gen_card(name='X5', util=50)
X6 = gen_card(name='X6', util=85)
X7 = gen_card(name='X7', util=43)
X8 = gen_card(name='X8', util=27)
X9 = gen_card(name='X9', util=11)
X10 = gen_card(name='X10', util=74)

# ----------------------------------CONTENTS--------------------------------------------
barchart = bar('bar')
linechart = bar('line')
timeline = bar('time')

perf_card = dbc.Card(
    dbc.CardBody([
        html.Div(html.H2('Average Performance'), className='align-self-center',
                 style={'text-align': 'center', 'font-size': 'x-large', 'margin-bottom':'10%'}),
        html.P(
            '43%',
            className="align-self-center",
            style={'text-align': 'center', 'font-size': 70}
        ),
    ]),
    style={'height': 233}
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
        style={'margin-top':'0%'}
    )

date_end = dcc.DatePickerSingle(
        id='date-picker-end',
        min_date_allowed=dt(2021, 12, 2).date(),
        max_date_allowed=dt(2022, 12, 2).date(),
        initial_visible_month=dt(2022, 12, 2).date(),
        date=dt(2022, 12, 2).date(),
        style={'margin-top':'0%'}
    )

freq_menu = dcc.Dropdown(
    options=[
            {'label': 'Daily', 'value': 'daily'},
            {'label': 'Weekly', 'value': 'weekly'},
        ],
    value='daily',
    searchable=False,
    clearable=False,
    style={'margin-top':'0%'}
)

download_but = dbc.Button("Download", color="primary", style={'width':'70%',"margin-bottom": "2%", 'fontSize': 25})

alert = dbc.Alert(
    "'Start' date must be prior to 'End' date.",
    id="alert-fade",
    dismissable=True,
    is_open=False,
    color="danger",
    style={'fontSize': 25}
)





