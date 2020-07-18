import dash

# Read style of internet (css file)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# Init my app dash and define my style CSS
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
server = app.server
