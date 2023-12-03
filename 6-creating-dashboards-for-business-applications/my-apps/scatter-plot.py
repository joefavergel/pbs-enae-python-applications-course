import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
  'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
)

fig = px.scatter(
    df, x="gdpPercap", y="lifeExp", size="pop",
    color="continent", hover_name="country", log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)