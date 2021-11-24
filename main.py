import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
from cards_generator import gen_card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

HEADER_STYLE = {
    "position": "fixed",
    "top": '2%',
    "left": '1%',
    "right": '1%',
    "background": "cyan",
    'overflow': 'auto'
}


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": '14%',
    "left": '1%',
    "bottom": '2%',
    "width": "22%",
    "padding": "1rem ",
    'background': 'cyan',
    "overflow": "auto",
}

MAINSPACE_STYLE = {
                'position': 'fixed',
                'top': '14%',
                'width': '75%',
                'right': '1%',
                'bottom': '2%',
                'background-color': 'cyan',
                "overflow": "auto"
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

card_graph = dbc.Card(
    dcc.Graph(id='my_bar', figure={'data': [{'x':[1, 2, 3, 4, 5], 'y':[20, 21, 19, 28, 35], 'type': 'bar'}
                                            ]
                                    }
              )
)

# ----------------------------------APP LAYOUT------------------------------------------
header = html.Div([
    html.H2("Header", className='display-4', style={'text-align': 'left', "padding-left": "1rem "}),
    dbc.Nav([]),

    ],
    style=HEADER_STYLE

)

mainspace = html.Div([
        html.H2('Mainspace', style={'text-align': 'center', "padding": "1rem "}),
        dbc.Nav([],
                 vertical=False),
        ],
        style=MAINSPACE_STYLE
)

sidebar = html.Div(
    [
        html.H2('Sidebar'),
        html.Hr(),
        html.Hr(),
        html.Hr(),
        html.Hr(),
        html.Hr(),

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

app.layout = html.Div([

    header,
    sidebar,
    mainspace,


],


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
