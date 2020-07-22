import sys

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from server import riesgo_asociado_layout, dashboard

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
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
        return riesgo_asociado_layout.layout
    elif pathname == "/models":
        return riesgo_asociado_layout.layout
    elif pathname == "/insights":
        return 404
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
        app.run_server(host="0.0.0.0", port=sys.argv[1])
    else:
        app.run_server(host="0.0.0.0", port=8080, debug=True)
