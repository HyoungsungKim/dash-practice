from typing import Text
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Tr import Tr
from numpy import flipud
import plotly.io as pio

from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], title="Layout test")

LOGO = "https://user-images.githubusercontent.com/72614349/110689028-7523dd80-819f-11eb-8cc6-a62b25f99287.png"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "1rem 2rem",
    "background-color": "#f8f9fa",
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

topbar = dbc.Navbar(
    [
        html.A(children="A tag", className="navbar-brand", href="https://www.google.com"),
        html.Button(
            children=html.Span(className="navbar-toggler-icon"),
            className="navbar-toggler",
            type="button", 
            **{
                "data-target":"#navbarSupportedContent",
                "aria-controls":"navbarSupportedContent",
                "aria-expanded":"false",
                "aria-label":"Toggle navigation",
            }
        ),
        
        html.Div(            
            [
              html.Ul(
                  [
                    html.Li(
                        [
                            html.A(
                                [
                                    "Home",
                                    html.Span(children="(current)", className="sr-only")
                                ]
                            ),
                        ]                            
                    ),
                  ],
                  className="navbar-nav mr-auto"
              ),
              
              dbc.Form(
                [   dbc.Input(className="form-control mr-sm-2", type="search", placeholder="Search"),
                    html.Button("Search", className="btn btn-outline-success my-2 my-sm-0", type="submit")
                ],
                className="form-inline my-2 my-lg-0"
              )
            ],
            className="collapse navbar-collapse",
        )
    ],
    className="topbar mb-4 static-top shadow"
)

sidebar = html.Ul(
    [
        html.A(
            [
                html.Div(
                    [html.I(className="fas fa-laugh-wink")],
                    className="sidebar-brand-icon rotate-n-15"
                ),
                html.Div(
                  "Jubaesi",
                  className="sidebar-brand-text mx-3"
                )
            ],
            className= "sidebar-brand d-flex align-items-center justify-content-center"
        ),        
        html.Hr(className="sidebar-divider my-0"),
        html.Li(
          className="nav-item active"
        ),
    ],
    className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
)

footer = html.Footer(
    [
        html.Div(
            [
                html.Div(
                    html.Span("copyright", className="copyright test-center my-auto"),
                    className="copyright text-center my-auto"
                )
            ],
            className="container my-auto")  
    ],
    className="sticky-footer bg-white"
)

content_first_row = dbc.Row([
    html.Div(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Div(children="Earning (Monthly)", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                                            html.H5("$40,000", className="mb-0 font-weight-bold text-gray-800")
                                        ],
                                        className="mr-2"
                                    ),
                                ],
                                align="center",                                
                                no_gutters=True
                            )                        
                        ],
                    )
                ],
                className="col shadow h-100 py-2",
                outline=True,
                style={
                    "border-left-color":"#4e73df",
                    "border-left-width":"4px"                       
                }
                
            ),
            className="col-xl-3 col-md-6 mb-4"
        ),
    html.Div(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Div(children="Earning (Monthly)", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                                            html.H5("$40,000", className="mb-0 font-weight-bold text-gray-800")
                                        ],
                                        className="mr-2"
                                    ),
                                ],
                                align="center",                                
                                no_gutters=True
                            )                        
                        ],
                    )
                ],
                className="col shadow h-100 py-2",
                outline=True,
                style={
                    "border-left-color":"#28b62c",
                    "border-left-width":"4px"                       
                }
                
            ),
            className="col-xl-3 col-md-6 mb-4"
        ),
    html.Div(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Div(children="Earning (Monthly)", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                                            html.H5("$40,000", className="mb-0 font-weight-bold text-gray-800")
                                        ],
                                        className="mr-2"
                                    ),
                                ],
                                align="center",                                
                                no_gutters=True
                            )                        
                        ],
                    )
                ],
                className="col shadow h-100 py-2",
                outline=True,
                style={
                    "border-left-color":"#36b9cc",
                    "border-left-width":"4px"                       
                }
                
            ),
            className="col-xl-3 col-md-6 mb-4"
        ),
    html.Div(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.Div(children="Earning (Monthly)", className="text-xs font-weight-bold text-primary text-uppercase mb-1"),
                                            html.H5("$40,000", className="mb-0 font-weight-bold text-gray-800")
                                        ],
                                        className="mr-2"
                                    ),
                                ],
                                align="center",                                
                                no_gutters=True
                            )                        
                        ],
                    )
                ],
                className="col shadow h-100 py-2",
                outline=True,
                style={
                    "border-left-color":"#f6c23e",
                    "border-left-width":"4px"                       
                }
                
            ),
            className="col-xl-3 col-md-6 mb-4"
        ),
]) 

#app.layout = dbc.Container(
app.layout = html.Div(
    id="wrapper",
    children=
        [
            sidebar,
            dbc.Container(id="content-Wrapper",
                children=
                [
                    html.Div(id="content",
                        children=[
                            topbar,
                            dbc.Container(
                                [
                                    html.Div(
                                        html.H1("Dashboard", className="h3 mb-0 text-gray-800"),
                                        className="d-sm-flex align-items-center justify-content-between mb-4"
                                    ),                                    
                                    content_first_row,
                                ],
                                fluid=True
                            ),

                        ],
                    ),
                    footer                    
                ],
                className="d-flex flex-column",
                fluid=True,
                style={
                    "padding-right":"0",
                    "padding-left":"0",
                }
            ),
        ],
    style={
            "display":"flex"
    }    
)     

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True)