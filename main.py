import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, Input, Output, State  # pip install dash (version 2.0.0 or higher)
from bodies import *


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='assets')

# ----------------------------------APP LAYOUT------------------------------------------

url_content_div = html.Div([dcc.Location(id="url", refresh=False),html.Div(id='page-content')])

home_layout = html.Div(children=[
        home_space,
        sidebar],
    style=BACK_STYLE)

content_layout = html.Div(children=[
        content_space,
        sidebar],
    style=BACK_STYLE)


app.layout = url_content_div

app.validation_layout = html.Div([
    url_content_div,
    home_layout,
    content_layout,
])
#app.config.suppress_callback_exceptions = True

# -------------------------------------------------------------------------------------
@app.callback(Output(component_id='page-content', component_property='children'),
              Input(component_id='url', component_property='pathname'))
def display_page(pathname):
    name = pathname[1:]
    print(name)
    if pathname == '/home' or pathname == '/':
        return home_layout
    elif pathname == '/' + name:
        return content_layout



@app.callback(
    Output(component_id='line', component_property='figure'),
    [Input('my-slider', 'value')]
)
def load_home(value):
    x = np.arange(value)
    rand = np.random.randint(100, size=value)
    line = px.line(x=x, y=rand, height=230)
    line.update_layout(
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor="rgba(221,220,220, 0.2)",
        margin=dict(t=15, l=5, b=5, r=0)
    )
    return line

@app.callback(
    [Output(component_id='output_text', component_property='children'),
     Output(component_id='bar', component_property='figure')],
    [Input("url", "pathname"),
     Input('date-picker-start', 'date'), Input('date-picker-end', 'date')]
)
def render_page_content(pathname, start_date, end_date):
    text = pathname[1:] # used for the header of the page to show machine's name
    df = pd.read_csv('Data.csv')
    df = df.loc[df['Machine'] == text]
    df.set_index('Day', inplace=True)
    if start_date < end_date:
        df = df.loc[start_date: end_date]

    bar = px.bar(df, x=df.index.tolist(), y=df['Utilisation'], height=300,  labels={'x': 'Date'})
    bar.layout.yaxis.tickformat = ',.0%'
    bar.update_layout(
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor="rgba(221,220,220, 0.075)",
        margin=dict(t=0, l=5, b=5, r=0)
    )
    return text, bar


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
