import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import flask
from flask import Flask, request, send_from_directory

asset_style = ['assets/style.css']

# server = flask.Flask(__name__)
# app = dash.Dash(__name__, server=server)

app = dash.Dash(
    __name__,
    external_stylesheets=asset_style)
server = app.server

print(server)
print()

@server.route('/vtk/')
def send_html(path):
    return send_from_directory('vtk', path)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python
    '''),
    dcc.RangeSlider(id="slider", className="slider"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5],
                    'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.H5("Dash Cnavas testing"),
    # Testing different src for iframe - local html file
    html.Div(children=[
        html.Iframe(
            id='iframe-vtk',
            # src="https://kitware.github.io/vtk-js/examples/GeometryViewer/GeometryViewer.html",
            # src= send_html('test.html'),
            height=600,
            width=800)], style={'text-align': 'center'}
    ),
    dcc.Loading(
        html.Button(id="test-button")
    )
])


@app.callback(
    [Output('test-button', 'children'),
     Output('iframe-vtk', 'src')],
    [Input('test-button', 'n_clicks')]
)
def testing_button(clicks):
    print("number of clicks {}".format(clicks))
    print()
    output = "Start"
    source = send_html('test.html')
    if clicks is None:
        output = "Button"
    else:
        output = "Button {}".format(clicks)

    return output, source


if __name__ == '__main__':
    app.run_server(debug=True)
