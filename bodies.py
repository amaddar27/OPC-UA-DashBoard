from components import *

# ----------------------------------BODIES--------------------------------------------

header = html.Div(className='header', children=[
        html.H2("Header", style={'text-align': 'left', "padding-left": "1rem"}),
        dbc.Nav([]),
    ],
    style=HEADER_STYLE
)

start = html.Div(children=[dbc.Row([
            dbc.Col(html.P('Start', style={'fontSize': 25}), width='auto', align="end"),
            dbc.Col(date_start, width='auto',  align="start")], justify='center'
    )]
)

end = html.Div(children=[dbc.Row([
            dbc.Col(html.P('End', style={'fontSize': 25}), width='auto'),
            dbc.Col(date_end, width='auto')], justify='center'
    )]
)

freq = html.Div(children=[dbc.Row([
            dbc.Col(html.P('Frequency', style={'fontSize': 25}), width='auto',  align="end"),
            dbc.Col(freq_menu, width='4')], justify='center'
    )],  className="pad-row"
)

dates_space = html.Div(children=[
    dbc.Row([
             dbc.Col(start, width='3'),
             dbc.Col(end, width='2'),
             dbc.Col(freq, width='4'),
             dbc.Col(download_but,  align="start")]),

    ],
    style = {'width': '100%','background-color': 'rgba(192,192,192,1)', 'padding-top': '1%', 'padding-bottom': '0.3%'
    }
)

home_space = html.Div([
        html.H2(children=['Home'], style={'text-align': 'center', 'font-size':80}),
        html.Hr(),
        slider,
        dbc.Row([dbc.Col(perf_card, width=3, lg=3),
                 dbc.Col(linechart, width=9, lg=9)])
    ],
    style=MAINSPACE_STYLE
)


content_space = html.Div(className='main-space', children=[
        html.H2(id='output_text', children=[], style={'text-align': 'center', 'font-size':80}),
        html.Hr(),
        dates_space,
        alert,
        html.P(),
        barchart
    ],
    style=MAINSPACE_STYLE
)


sidebar = html.Div(className='side-bar', children=[
        dbc.Row([dbc.Col(dcc.Link('[LOGO]', href='/home', style={'font-size':25}), width=3),
                 dbc.Col(html.H2('Sidebar', style={'fontSize': 50}), width=6)
                 ], align="center", justify="start", className="g-0", style={'padding-top':'7%'}),
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