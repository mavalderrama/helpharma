# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import sys

# Read style of internet (css file)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# Init my app dash and define my style CSS
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define my layout
# Adding more CSS styles
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Define LAYOUT
#This use HTML tags
# html.H1 : The <h1> to <h6> tags are used to define HTML headings.
# html.Div : The <div> tag defines a division or a section in an HTML document.
#app.layout = html.Div(children=[
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children='Hello World Dash H1'),
    html.H2(
        children='Hello World Dash H2',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Dash: A web application framework for Python (First DIV).
    '''),

    dcc.Graph(
        id='example-graph_1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    dcc.Graph(
        id='example-graph_2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Div(children='''
        Dash: A web application framework for Python (Tail DIV).
    ''')
])

# Configuring APP running as Web 
if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', port=sys.argv[0])
