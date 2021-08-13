import copy
import dash
import dash_core_components as dcc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
from dash_html_components.Q import Q
import dash_table

import numpy as np
import pandas as pd

from dash.dependencies import Input, Output

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

N = 100

df = pd.DataFrame({
    'category': (
        (['apples'] * 5 * N) +
        (['oranges'] * 10 * N) +
        (['figs'] * 20 * N) +
        (['pineapples'] * 15 * N)
    )
})
df['x'] = np.random.randn(len(df['category']))
df['y'] = np.random.randn(len(df['category']))

app.title = "layout practice"
app.layout  = html.Div([    
    dcc.Store(id='signal'),
    dcc.Store(id='signal2'),
    
    html.H1(children="Jubaesi layout dashboard test", style={
        "text-align": "center"
    }),       
    
    html.Div([
        html.Div([ #Top left devision
            html.Div([  # Division for image
                html.Img(src=app.get_asset_url("sample_image.jpg"), style={
                    'width':"60%",         
                })
            ], style={
                "border":"0.5px black solid",
                'display': 'flex',
                "margin":"3px",
                "verticalAlign": "top",                
                'align-items': 'center',     # For centerlize
                'justify-content': 'center', # For centerlize
            }),
            
            html.Div([
                dcc.Markdown('''
                    # Hello dash                          
                    ## This is sample of jubaesi dashboard                                            
                ''')
            ], style={
                    "border":"0.5px black solid",
                    'display': 'flex',
                    "text-align":"justify",
                    "verticalAlign": "top",                
                    'align-items': 'center',     # For centerlize
                    'justify-content': 'center', # For centerlize
               }),
        ], style={
            "border":"0.5px black solid",
            'width': '32%',
            "height":"98%",
            'display': 'grid',
            "margin":"3px",
            "verticalAlign": "top",
            'align-items': 'center',     # For centerlize
            'justify-content': 'center', # For centerlize
            }),    
        # --------------------------------

        # --------------------------------
        html.Div([
            dcc.Dropdown(
                id='dropdown1',
                options=[{'label': i, 'value': i} for i in df['category'].unique()],
                value='apples'
            ),               
             
            html.Div([
                dcc.Graph(id='graph-1', style={
                    "width":"500px",
                    "height":"300px",
                    "border":"0.5px black solid",
                    'display': 'inline-block',
                    "margin-left":"1px",
                    "margin-right":"1px",
                })
            ]),             
            
            html.Div([
                dcc.Graph(id='graph-2', style={
                    "width":"500px",
                    "height":"300px",
                    "border":"0.5px black solid",
                    'display': 'inline-block',
                    "margin-left":"1px",
                    "margin-right":"1px"
                })
            ]),
        ], style={
            "border":"0.5px black solid",
            'width': '32%',
            "height":"98%",
            'display': 'grid',
            "margin":"3px",
            "verticalAlign": "top",
            'align-items': 'center',
            'justify-content': 'center', 
            }),        
        # --------------------------------        
        html.Div([
            dcc.Dropdown(
                id='dropdown2',
                options=[{'label': i, 'value': i} for i in df['category'].unique()],
                value='apples'
            ),                
            html.Div([
                dcc.Graph(id='graph-3', style={
                    "width":"500px",
                    "height":"300px",
                    "border":"0.5px black solid",
                    'display': 'inline-block',
                    "margin-left":"1px",
                    "margin-right":"1px"
                })
            ]),
            html.Div([
                dcc.Graph(id='graph-4', style={
                    "width":"500px",
                    "height":"300px",
                    "border":"0.5px black solid",
                    'display': 'inline-block',
                    "margin-left":"1px",
                    "margin-right":"1px"
                })
            ]),
        ], style={
            "border":"0.5px black solid",
            'width': '32%',
            "height":"98%",
            'display': 'grid',
            "margin":"3px",
            "verticalAlign": "top",
            'align-items': 'center',
            'justify-content': 'center',
            }),
        # --------------------------------  
    ], style={
        "border":"1px black solid",
        'width': '100%',
        "height":"750px",
        'display': 'flex',
        "margin":"3px",
        'align-items': 'center',
        'justify-content': 'center',
        }),
    
    
    html.Div([
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='apples', value='tab-1'),
            dcc.Tab(label='oranges', value='tab-2'),     
        ]),
        html.Div(id='tabs-content')    
    ], style={
        'width': '100%',
        "border":"1px black solid",
        'display': 'inline-block',
        "margin":"3px",
       }, className='one columns'),      
])

@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dash_table.DataTable(
                id="table",
                columns = [{'name':i, 'id':i} for i in df.columns],
                data=df.loc[df["category"] == "apples"][:10].to_dict('records'),
            )
        ], className="row")
    elif tab == 'tab-2':
        return html.Div([
            dash_table.DataTable(
                id="table",
                columns = [{'name':i, 'id':i} for i in df.columns],
                data=df.loc[df["category"] == "oranges"][:10].to_dict('records'),
            )
        ], className="row")

def global_store(value):
    return df[df['category'] == value]

def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_dataframe = global_store(value)
    fig['data'][0]['x'] = filtered_dataframe['x']
    fig['data'][0]['y'] = filtered_dataframe['y']
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b':20, 't': 10}}
    
    return fig

@app.callback(Output('signal', 'data'), Input('dropdown1', 'value'))
def compute_value(value):
    global_store(value)
    return value

@app.callback(Output('signal2', 'data'), Input('dropdown2', 'value'))
def compute_value2(value):
    global_store(value)
    return value

@app.callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })

@app.callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2d',
        }]
    })
    
@app.callback(Output('graph-3', 'figure'), Input('signal2', 'data'))
def update_graph_3(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })
    
@app.callback(Output('graph-4', 'figure'), Input('signal2', 'data'))
def update_graph_4(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2d',
        }]
    })   

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)