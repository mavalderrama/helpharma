# coding=utf-8
import dash_core_components as dcc
import dash_html_components as html
import flask

from app import app
from .plots.home import patients, consultas_fig

title = html.Div(
    className="title",
    children=[html.H1("Helpharma Psoriasis Dashboard")],
    id="nutrition_title",
)

logos = html.Div(
    html.Img(
        src=app.get_asset_url("psoriasis_hand.png"),
        id="hand_logo",
        style={"width": "250px"},
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
                        html.H6("No. of Individual Patients"),
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
                        html.Div(
                            [
                                logos,
                                html.Div(
                                    [
                                        html.Form(
                                            [
                                                html.H6("Analyze Patient by ID:"),
                                                dcc.Input(
                                                    id="patient_id",
                                                    type="search",
                                                    placeholder="Patient ID",
                                                    name="id",
                                                ),
                                                html.Button(
                                                    "Analyze",
                                                    className="button",
                                                    type="submit",
                                                    autoFocus=True,
                                                ),
                                            ],
                                            method="post",
                                            action="/post",
                                        )
                                    ],
                                    style={"padding-top": "10px"},
                                    id="psoriasis_search",
                                ),
                            ]
                        )
                    ],
                    className="pretty_container",
                    style={"display": "flex", "align-items": "center"},
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Graph(
                                    id="consulta_graph",
                                    animate=True,
                                    figure=consultas_fig,
                                )
                            ],
                            # style={"width": "90%"},
                            id="test",
                        )
                    ],
                    className="pretty_container",
                ),
            ],
            className="row container-display",
        ),
    ]
)


@app.server.route("/post", methods=["POST"])
def on_post():
    """
    Post form
    :return:
    """
    data = flask.request.form
    return flask.redirect("/models?id={}".format(data.to_dict()["id"]))
