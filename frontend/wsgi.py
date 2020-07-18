import sys

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from server import dashboard

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return dashboard.layout
    else:
        return 404


# Configuring APP running as Web
if __name__ == "__main__":
    # app.run_server(debug=True)
    if len(sys.argv) > 1:
        app.run_server(host="0.0.0.0", port=sys.argv[1])
    else:
        app.run_server(host="0.0.0.0", port=8080, debug=True)
