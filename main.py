import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, Input, Output  # pip install dash (version 2.0.0 or higher)
from components import *

from spaces import spaces

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='assets')

# ----------------------------------APP LAYOUT------------------------------------------

app.layout = html.Div(className='bg', children=[
        dcc.Location(id="url"),
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
    [Input("url", "pathname"), Input('my-slider', 'value')]
)
def render_page_content(pathname, value):
    name = pathname[1:]
    if pathname == '/' + name:
        text = name

        x = np.arange(value)
        rand = np.random.randint(30, size=value)
        bar = px.bar(x=x, y=x * rand, height=300)
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
