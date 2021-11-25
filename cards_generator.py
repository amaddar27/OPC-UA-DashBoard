from dash import html
import dash_bootstrap_components as dbc

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

def get_colour(util):
    if 60 <= util :
        colour = 'rgba(152,161,72,1)'
    elif 35 <= util < 60:
        colour = 'rgba(243,156,18,1)'
    else:
        colour = 'rgba(231,76,60,1)'
    return {'background': colour}

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

def get_style(name, util):
    if name in {'X10', 'X9'}:
        style = {"width": "8rem", 'height': '7rem'}  # css styling
    else:
        style = {"width": "8rem", 'height': '7rem', "margin-bottom": "20px"}
    style = merge_two_dicts(get_colour(util), style)
    return style



def gen_card(name, util):
    card = dbc.Card(
        gen_body(name, util),
        style=get_style(name, util),
        #color="success",  # https://bootswatch.com/default/ for more card colors
        inverse=True,  # change color of text (black or white)
        outline=False,  # True = remove the block colors from the background and header
    )
    return card
