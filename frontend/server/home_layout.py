# coding=utf-8
import flask
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from .plots.home import patients

from app import app

title = html.Div(
    className="title",
    children=[html.H1("Helpharma Psoriasis Dashboard")],
    id="nutrition_title",
)

logos = html.Div(
    html.Img(
        src=app.get_asset_url("psoriasis_hand.png"),
        id="hand_logo",
        style={"width": "200px"},
    ),
    style={"text-align": "center"},
)

layout = html.Div(
    [
        html.Div(title),
        html.Div(
            [
                html.Div(
                    [
                        html.H6("No. of Patients"),
                        html.H5(id="patients_number", children=patients),
                    ],
                    id="active_patients",
                    className="mini_container",
                ),
            ],
            className="row container-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        logos,
                        html.Div(
                            [
                                html.Form(
                                    [
                                        html.H6("Search by Patient ID:"),
                                        dcc.Input(
                                            id="patient_id",
                                            type="search",
                                            placeholder="Patient ID",
                                            name="id",
                                        ),
                                        html.Button(
                                            "Search...",
                                            className="button",
                                            type="submit",
                                        ),
                                    ],
                                    method="post",
                                    action="/post",
                                )
                            ],
                            style={"padding-top": "10px"},
                            id="psoriasis_search",
                        ),
                    ],
                    className="pretty_container",
                )
            ],
            className="row container-display",
        ),
    ]
)
from flask import abort, redirect, url_for


@app.server.route("/post", methods=["POST"])
def on_post():
    """
    Post form
    :return:
    """
    data = flask.request.form
    return flask.redirect("/models?id={}".format(data.to_dict()["id"]))


# @app.callback(
#     Output("container-button-basic", "children"),
#     [Input("submit-val", "n_clicks")],
#     [State("input-on-submit", "value")],
# )
# def update_output(n_clicks, value):
#     return 'The input value was "{}" and the button has been clicked {} times'.format(
#         value, n_clicks
#     )
