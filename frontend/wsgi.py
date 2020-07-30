import sys

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from server import (
    riesgo_asociado_layout,
    dashboard,
    nutricion_layout,
    home_layout,
    models_layout,
)

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "margin-top": "6rem",
}
content = html.Div(id="dashboard_content", style=CONTENT_STYLE)

app.layout = html.Div(
    [dcc.Location(id="url", refresh=True), dashboard.dashboard, content]
)


@app.callback(Output("dashboard_content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """
    Router
    :param pathname:
    :return:
    """
    if pathname == "/":
        app.title = "Dashboard"
        return home_layout.layout
    elif pathname == "/models":
        return models_layout.layout
    elif pathname == "/nutricion":
        return nutricion_layout.layout
    elif pathname == "/terapias":
        return riesgo_asociado_layout.layout
    else:
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P("The pathname {} was not recognised...".format(pathname)),
            ]
        )


# Configuring APP running as Web
if __name__ == "__main__":
    # app.run_server(debug=True)
    if len(sys.argv) > 1:
        app.run_server(host="0.0.0.0", port=sys.argv[1], threaded=True)
    else:
        app.run_server(host="0.0.0.0", port=8080, debug=True, threaded=True)
