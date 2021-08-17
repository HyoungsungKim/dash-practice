from typing import Text
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

from dash_html_components.Tr import Tr
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from rec_sys import RecSys
from dash_bootstrap_templates import load_figure_template

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], title="Layout test")

LOGO = "https://user-images.githubusercontent.com/72614349/110689028-7523dd80-819f-11eb-8cc6-a62b25f99287.png"

rec_sys = RecSys()
filtered_userIds, filtered_ratings = rec_sys.filter_out_users()

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
                [   
                    #dbc.Input(className="form-control mr-sm-2", type="search", placeholder="Search"),
                    dbc.Badge("User id", color="primary"),
                    dbc.Select(
                        id="target_userId",
                        options=[
                            {"label": col, "value":col} for col in filtered_userIds[:30]
                        ],
                        value=filtered_userIds[0][0],
                    ),                    
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

content_second_row = dbc.Row([
    html.Div(
        [
            dbc.Card(
                [
                    html.Div(html.H6("Preferred genre", className="m-0 font-weight-bold text-primary"),
                             className="card-header py-3 d-flex flex-row align-items-center justify-content-between"),
                    dbc.CardBody(
                        [
                            dcc.Graph(id="preferred_genre_fig",
                                        #style={"display": "block", "width": "907px", "height": "320px"}, 
                            )
                        ],
                    )
                ],
                className="shadow mb-5"
            )
        ],
        className="col-xl-8 col-lg-7"
    ),
    
    html.Div(
        [
            dbc.Card(
                [
                    html.Div(html.H6("Recommendation", className="m-0 font-weight-bold text-primary"),
                             className="card-header py-3 d-flex flex-row align-items-center justify-content-between"),
                    html.Div(
                        [     
                            dbc.Row(html.H5("You may like...", className="mb-0 font-weight-bold text-gray-800"), className="d-sm-flex align-items-center justify-content-between mb-4"),
                            dbc.Row(
                                html.Div(
                                    id="recommendation_table",                                
                                    className="table-responsive"
                                )
                            )
                        ],
                        className="card-body"
                    )
                ],
                className="shadow mb-4"
            )
        ],
        className="col-xl-4 col-lg-7"
    )
])

@app.callback(
    Output("preferred_genre_fig", "figure"),
    #Output("recommendation_result", "recommendation")      
    [
        Input("target_userId", "value")
    ]
)
def make_preferred_genre_graph(target_userId):
    
     
    target_userId = int(target_userId)
    target_user_row = rec_sys.get_target_row(filtered_ratings, target_userId)
    
    genre_columns_name = rec_sys.get_genre_names()
        
    preferred_genre = pd.DataFrame({"preferences":target_user_row.reshape(-1), "genres":genre_columns_name}).sort_values(by="preferences", ascending=False)
    #print(preferred_genre)
    #print(preferred_genre["genres"])
    #preferred_genre_fig = px.bar(preferred_genre, x="preferences", y="genres")
    #preferred_genre_fig.update_yaxes(tickvals=preferred_genre["preferences"])    
    
    preferred_genre_fig = px.bar(preferred_genre, x="genres", y="preferences")
    preferred_genre_fig.update_layout(transition_duration=1000)
    preferred_genre_fig.update_xaxes(tickvals=preferred_genre["genres"])    
    preferred_genre_fig.update_yaxes(tickvals=[0, 0.25, 0.5, 0.75, 1])    
    
    return preferred_genre_fig

@app.callback(
    Output("recommendation_table", "children"),
    Input("target_userId", "value")    
)
def make_recommendation_table(target_userId):
    target_userId = int(target_userId)
    
    _, src_userId_array = rec_sys.sample_bounded_userId(filtered_userIds)
    recommended_movies = rec_sys.operate_rec_sys(filtered_ratings, target_userId, src_userId_array)

    table = dash_table.DataTable(
        data = recommended_movies.to_dict("records"),
        columns=[{"id": c, "name": c} for c in recommended_movies.columns],
        page_size=10
    )
    
    return table
    

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
                                    content_second_row,
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
    
    