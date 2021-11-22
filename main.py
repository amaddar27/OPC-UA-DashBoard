import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
from cards_generator import gen_card

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
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

card_img = dbc.CardImg(src="/static/images/placeholder286x180.png", bottom=True)
card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"height": "85vh"},
)

card_graph = dbc.Card(
    dcc.Graph(id='my_bar', figure={}), body=True, color="secondary",
)

# ----------------------------------APP LAYOUT------------------------------------------

app.layout = html.Div([

    html.H1("OPCUA", style={'text-align': 'center', "margin-bottom": "15px"}),

    html.Div([
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
        className='col-3',
        # style={'width': '25'}
    ),

    html.Div([
        card_graph
    ],
        className='col-9',
        # style={'padding-top' : '1%'}
    ),

],

    className='row',
    style={'height': '90vh', 'padding-left': '2%', 'padding-right': '1%', 'padding-bottom': '2%'}

)


# -------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='my_bar', component_property='figure'),
    # Input(component_id='yaxis_raditem', component_property='value')
)
def graph():
    data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
    # Create DataFrame
    df = pd.DataFrame(data)
    fig = {px.bar(df, x='Name', y='Age')}
    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
