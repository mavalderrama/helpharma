# coding=utf-8

from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app


from flask import request

layout = html.Div([dcc.Location(id="path"), html.Div(id="patient_id")])


@app.callback(Output("patient_id", "children"), [Input("path", "search")])
def update_output(search):
    """
    update
    :param search:
    :return:
    """
    return search.split("=")[1]
