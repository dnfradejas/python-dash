# Dash related dependencies
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# To open browser upon running your app
import webbrowser

# Importing your app definition from app.py so we can use it
from app import app

from apps import commonmodules as cm
from apps.movies import movies_home, movies_profile
from apps.movies import movies_home
from apps import home


CONTENT_STYLE = {
    "margin-top": "1em",
    "margin-left": "1em",
    "margin-right": "1em",
    "padding": "1em 1em",
}

app.layout = html.Div(
    [
        # Location Variable -- contains details about the url
        dcc.Location(id='url', refresh=True),

        # Adding the navbar
        cm.navbar,

        # Page Content -- Div that contains page layout
        html.Div(id='page-content', style=CONTENT_STYLE),

    ]
)


@app.callback(
    [
        Output('page-content', 'children')
    ],
    [
        # If the path (i.e. part after the website name; 
        # in url = youtube.com/watch, path = '/watch') changes, 
        # the callback is triggered
        Input('url', 'pathname')
    ]
)
def displaypage (pathname):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'url':
            if pathname == '/' or pathname == '/home':
                # From the imported module 'home', we get the layout variable
                returnlayout = home.layout

            elif pathname == '/movies':
                returnlayout = movies_home.layout

            elif pathname == '/movies/movies_profile':
                returnlayout = movies_profile.layout
            else:
                returnlayout = 'error404'

            return [returnlayout]
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)