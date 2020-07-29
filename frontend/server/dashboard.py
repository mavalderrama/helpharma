import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

logos = html.Div(
    children=[
        html.Img(
            src=app.get_asset_url("helpharma_logo.png"),
            id="helpharma_logo",
            className="logo",
        )
    ],
)

#############################################################################
# Sidebar Layout
#############################################################################
sidebar = html.Div(
    [
        logos,
        html.Hr(style={"height": "0.5px", "background-color": "#ccc"}),
        html.P("DS4A - Team 12", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", id="page-1-link"),
                # dbc.NavLink("Models", href="/models", id="page-2-link"),
                dbc.NavLink("Nutrición", href="/nutricion", id="page-3-link"),
                dbc.NavLink("Terapias/Riesgo", href="/terapias", id="page-4-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)
#############################################################################
# Title Layout
#############################################################################


@app.callback(
    [
        Output("page-1-link", "active"),
        Output("page-3-link", "active"),
        Output("page-4-link", "active"),
    ],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    """
    Sets the active state to on
    :param pathname:
    :return:
    """
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return (
            True,
            False,
            False,
        )
    if pathname == "/nutricion":
        return False, True, False
    if pathname == "/terapias":
        return False, False, True
    else:
        return True, False, False


dashboard = html.Div([sidebar])
