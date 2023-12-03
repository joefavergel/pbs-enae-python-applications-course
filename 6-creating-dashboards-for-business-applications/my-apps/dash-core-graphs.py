import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Hello Graph', style={'text-align': 'center'}),

    dcc.Graph(
        id='my-first-graph',
        figure=dict(data=[dict(x=[0, 1, 2], y=[3, 4, 2])])
    )
])


if __name__ == '__main__':
 app.run_server()
