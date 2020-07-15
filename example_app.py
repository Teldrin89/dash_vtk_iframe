import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

asset_style = ['assets/style.css']

app = dash.Dash(
    __name__,
    external_stylesheets=asset_style)

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
    # dc.DashCanvas(id='canvas-1')
    # html.Canvas(id="html-canvas"),
    # Testing different src for iframe - local html file
    # html.Iframe(
    #     src="https://kitware.github.io/vtk-js/examples/GeometryViewer/GeometryViewer.html",
    #     # src="assets/geom_view.html",
    #     height=300,
    #     width=600),
    dcc.Loading(
        html.Button(id="test-button")
    )

])


@app.callback(
    Output('test-button', 'children'),
    [Input('test-button', 'n_clicks')]
)
def testing_button(clicks):
    print("number of clicks {}".format(clicks))
    print()
    output = "Start"
    if clicks is None:
        output = "Button"
    else:
        output = "Button {}".format(clicks)

    return output


if __name__ == '__main__':
    app.run_server(debug=True)
