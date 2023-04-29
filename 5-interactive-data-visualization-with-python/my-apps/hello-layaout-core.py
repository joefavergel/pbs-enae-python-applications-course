import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

component1 = dcc.Dropdown(
    value='MTL', options=[
        {'label': 'New York city', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'Ciudad de Guatemala', 'value': 'GT'},
    ]
)

component2 = dcc.Checklist(
    value='MTL', options=[
        {'label': 'New York city', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'Ciudad de Guatemala', 'value': 'GT'},
    ]
)

component3 = dcc.Slider(min=0, max=9, value=5)

component4 = dcc.Tabs(value='tab-2-example', children=[
    dcc.Tab(label='tab one', value='tab-1-example', children=[
        component1, component3
    ]),
    dcc.Tab(label='tab two', value='tab-2-example', children=[
        component2
    ])
])

app.layout = html.Div(component4)


if __name__ == "__main__":
    app.run_server()