import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import webbrowser
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import casefunctions


app = dash.Dash(__name__, external_stylesheets = ['assets/bootstrap.css', dbc.themes.BOOTSTRAP])
app.title = 'First Dash App'

app.layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        html.H4('MY FIRST DASH APP', style={'fontWeight': 'bold'})
                    ]
                ),
                dbc.CardBody(
                    [
                        # Input
                        dbc.Row(
                            [
                                dbc.Label("Input Value", width=3),
                                dbc.Col(
                                    dbc.Input(
                                        type="text", id="input_value", placeholder="inputs please!",
                                        value=None
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Process", width=3),
                                dbc.Col(
                                    dcc.Dropdown(
                                        id='process_type',
                                        searchable=True,
                                        options = [
                                            dict(label='Factorial', value=1),
                                            dict(label='Palindrome Check', value=2),
                                            dict(label='Greeter', value=3),
                                        ],
                                        style={'color': 'black'}
                                    ),
                                    width=5,
                                ),
                            ],
                            className="mb-3",
                        ),
                        html.Br(),
                        html.Div(
                            dbc.Button("Give me Stuff", color="info", className="me-1", id='confirm_process'),
                            className='d-grid gap-2'
                        ), 
                        html.Hr(),
                        html.Div(
                            "No process yet", 
                            id='output_container',
                            style={'border': '2px dashed #777', 'border-radius': '5px',
                                   'padding': '1em'},
                            className='text-center'
                        )
                    ]
                ),
            ],
            className='card text-white bg-dark mb-3'
        )
    ],
    style={
        'position': 'fixed',
        'top': '50%',
        'left': '50%',
        'transform': 'translate(-50%, -50%)',
        'width': '40%'
    }
)


@app.callback(
    [
        Output('output_container', 'children')
    ],
    [
        Input('confirm_process', 'n_clicks')
    ],
    [
        State('input_value', 'value'),
        State('process_type', 'value'),
    ]
)
def run_process(btnclick, inputvalue, processtype):
    if processtype == 1:
        output_text = str(casefunctions.factorial(inputvalue))
    elif processtype == 2:
        input_ispalindrome = casefunctions.is_palindrome(inputvalue)
        if input_ispalindrome:
            output_text = f'{inputvalue} is a palindrome.'
        else:
            output_text = f'{inputvalue} is NOT a palindrome.'
    else:
        output_text = casefunctions.greeter(inputvalue)
    
    return [output_text]



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/')
    app.run_server(debug=False)