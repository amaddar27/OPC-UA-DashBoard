from dash import html
import dash_bootstrap_components as dbc


def gen_body(name, util):
    body = dbc.CardBody(
        [
            html.Div(
                dbc.Button(name, id='button'+name, value=name, color="secondary", style={"margin-bottom": "20px"}),
                className="d-grid gap-2"
            ),
            # html.P('\n'),
            html.P(
                '{}%'.format(util),
                className="align-self-center",
                style={'text-align': 'center', 'font-size': 'x-large'}
            ),
        ]
    )
    return body

def get_style(name):
    if name == 'X10' or name == 'X9':
        return {"width": "8rem", 'height': '7rem'}  # css styling
    else:
        return {"width": "8rem", 'height': '7rem', "margin-bottom": "20px"}


def gen_card(name, util):
    card = dbc.Card(
        gen_body(name, util),
        style=get_style(name),
        color="success",  # https://bootswatch.com/default/ for more card colors
        inverse=True,  # change color of text (black or white)
        outline=False,  # True = remove the block colors from the background and header
    )
    return card
