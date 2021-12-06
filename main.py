import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, Input, Output, State  # pip install dash (version 2.0.0 or higher)
from components import *


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
    [Input("url", "pathname"), Input('my-slider', 'value'),
     Input('date-picker-start', 'date'), Input('date-picker-end', 'date')]
)
def render_page_content(pathname, value, start_date, end_date):
    name = pathname[1:]
    if pathname == '/' + name:
        text = name
        df = pd.read_csv('Data.csv')
        df = df.loc[df['Machine'] == name]
        df.set_index('Day', inplace=True)
        if start_date < end_date:
            df = df.loc[start_date: end_date]


        x = np.arange(value)
        rand = np.random.randint(30, size=value)
        bar = px.bar(x=df.index.tolist(), y=df['Utilisation'], height=300)
        bar.layout.yaxis.tickformat = ',.0%'
        #bar.layout.yaxis.hoverformat = 'closest'
        bar.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(221,220,220, 0.2)',
            plot_bgcolor="rgba(221,220,220, 0.2)",
            margin=dict(t=0, l=5, b=5, r=0)
        )

        line = px.line(x=x, y=x * rand, height=200)
        line.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            margin=dict(t=0, l=5, b=5, r=0)
        )
        return text, bar, line


@app.callback(
    Output("alert-fade", "is_open"),
    [Input('date-picker-start', 'date'), Input('date-picker-end', 'date')],
    [State("alert-fade", "is_open")]
)
def date_alert(start_date, end_date, is_open):
    if start_date < end_date:
        is_open = False
    else:
        is_open = True
    return  is_open

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
