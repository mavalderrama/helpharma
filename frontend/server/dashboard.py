from app import app
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

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
                dbc.NavLink("Models", href="/models", id="page-2-link"),
                dbc.NavLink("Nutrición", href="/nutricion", id="page-3-link"),
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
title = html.Div(
    className="title",
    children=[html.H1("Treatment Failure Diagnostic Decision Support System")],
    id="title",
)


@app.callback(
    [
        Output("page-1-link", "active"),
        Output("page-2-link", "active"),
        Output("page-3-link", "active"),
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
        return True, False, False
    if pathname == "/models":
        return False, True, False
    if pathname == "/nutricion":
        return False, False, True


dashboard = html.Div([sidebar, title])
