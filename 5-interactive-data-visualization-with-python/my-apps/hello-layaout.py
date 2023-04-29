import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(
            "Visualizacion iteractiva de datos con Python",
            style={'text-align': 'center'}
        ),
        html.H2(
            "Skill Tools"
        ),
        html.Div(
            id='my-div',
            children="Dash: A web app framework for Python",
            style={'text-align': 'center'}
        )
    ]
)


if __name__ == "__main__":
    app.run_server()