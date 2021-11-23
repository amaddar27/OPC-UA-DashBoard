import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
from cards_generator import gen_card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

HEADER_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    #"height": '10%',
    #"padding": "2rem 1rem",
    #"background-color": "white",
}


SIDEBAR_STYLE = {
    #"position": "fixed",
    #"top": 0,
    "left": 0,
    "bottom": 0,
    "width": "25%",
    "padding": "1rem ",
    #"background-color": "#f8f9fa",
    'bakcground-colo': 'black',
    "overflow": "scroll",
}

# ----------------------------------CARDS--------------------------------------------
X1 = gen_card(name='X1', util=10)
X2 = gen_card(name='X2', util=17)
X3 = gen_card(name='X3', util=30)
X4 = gen_card(name='X4', util=13)
X5 = gen_card(name='X5', util=21)
X6 = gen_card(name='X6', util=25)
X7 = gen_card(name='X7', util=43)
X8 = gen_card(name='X8', util=27)
X9 = gen_card(name='X9', util=11)
X10 = gen_card(name='X10', util=74)

# cards = dbc.CardGroup([X1, X2, X3, X4, X5, X6])

card_graph = dbc.Card(
    dcc.Graph(id='my_bar', figure={'data': [{'x':[1, 2, 3, 4, 5], 'y':[20, 21, 19, 28, 35], 'type': 'bar'}
                                            ]
                                    }
              )
)

# ----------------------------------APP LAYOUT------------------------------------------
header = html.Div([
    html.H2("Header", className='display-4', style={'text-align': 'left', "padding": "1rem "}),
    html.Hr(),
    dbc.Navbar([],
                style=HEADER_STYLE
               )
])
sidebar = html.Div(
    [
        #html.H2("Sidebar", className="display-4"),
        html.H2('Sidebar'),
        html.Hr(),
        html.Hr(),
        html.Hr(),
        html.Hr(),
        html.Hr(),



        dbc.Nav(
            [
                dbc.Row([dbc.Col(X1, width='auto'),
                        dbc.Col(X2, width='auto')]),
                dbc.Row([dbc.Col(X3, width='auto'),
                        dbc.Col(X4, width='auto')]),
                dbc.Row([dbc.Col(X5, width='auto'),
                        dbc.Col(X6, width='auto')]),
                dbc.Row([dbc.Col(X7, width='auto'),
                        dbc.Col(X8, width='auto')]),
                dbc.Row([dbc.Col(X9, width='auto'),
                        dbc.Col(X10, width='auto')]),
            ],
            navbar=False,
            navbar_scroll=True,
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

app.layout = html.Div([

    #html.H1("OPC-UA Monitoring", style={'text-align': 'center', "margin-bottom": "5vh"}),
    dbc.Row([
        dbc.Row(dbc.Col(header)),
        dbc.Row([dbc.Col(sidebar)])
    ])
    #header,
    #sidebar
    #dbc.Row([dbc.Col(sidebar, width=3)])





    #sidebar

],

    #className='row',
    #style={'height': '90vh', 'padding-left': '2%', 'padding-right': '1%', 'padding-bottom': '2%'}

)


'''
# -------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='my_bar', component_property='figure'),
    Input(component_id='buttonX1', component_property='X1')
)
def graph(button):
    data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
    # Create DataFrame
    df = pd.DataFrame(data)
    fig = {px.bar(df, x='Name', y='Age')}
    return fig
'''


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
