# coding=utf-8

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([dcc.Location(id="path"), html.Div(id="patient_id")])


@app.callback(Output("patient_id", "children"), [Input("path", "search")])
def update_output(search):
    """
    update
    :param search:
    :return:
    """
    return search.split("=")[1]
