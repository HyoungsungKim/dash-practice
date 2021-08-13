import copy
import dash
import dash_core_components as dcc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
from dash_html_components.P import P
from dash_html_components.Q import Q
import dash_table
import dash_bootstrap_components as dbc

import numpy as np
import pandas as pd

from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "layout practice"

app.layout  = html.Div([    
    #Title
    html.Div(children="This is Div but work like title", style={
        "background":"lightgray",
        "height":"215px"
        }),                    
    html.Hr(),
    
    # Body                       
    html.Div([
        html.Div([
            html.Div("하나", className="box1"),
            html.Div("둘", className="box2"),
            html.Div("셋", className="box3")
            ], style={
                "display":"flex"
            })
        ], style={
            "background":"#f2f4f7",
            "margin":"0",
            "min-height":"700px",
    }),
    
    html.Hr(),
    # Footer
    html.Footer(children="Hello footer", style={
        "background":"darkgray",
        "height":"310px"
    })    
])


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
    