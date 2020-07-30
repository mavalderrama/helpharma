# coding=utf-8
import dash_core_components as dcc
import dash_html_components as html
import flask

from app import app
from .plots.home import patients, consultas_fig, \
                        dlqi_count, dlqi_mean, dlqi_std, \
                        pasi_mean, pasi_std, pasi_count, \
                        pga_mean, pga_std, pga_count

from .plots.nutricion import desnutricion_sum, obesidad_sum

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
                        html.H6("No. of Individual Patients", className="bold"),
                        html.H5(id="patients_number", children=patients, className="centered bold"),
                    ],
                    id="active_patients",
                    className="mini_container background_green",
                ),
                html.Div(
                    [
                        html.H6("Desnutricion (IMC < 18.5)", className="bold"),
                        html.H5(id="desnutricion_count", children=str((desnutricion_sum/patients * 100).round(2)) + " % (" + str(int(desnutricion_sum)) + ")", className="centered bold"), #pga_std
                    ],
                    id="desnutricion_count_indicator",
                    className="mini_container background_red",
                ),                 
                html.Div(
                    [
                        html.H6("Obesidad (IMC > 30)", className="bold"),
                        html.H5(id="obesidad_sum", children=str((obesidad_sum/patients * 100).round(2)) + " % (" + str(int(obesidad_sum)) + ")", className="centered bold"), # pasi_std
                    ],
                    id="obesidad_sum_indicator",
                    className="mini_container  background_red",
                ), 
                html.Div(
                    [
                        html.H6("DLQI Mean (of " + str(dlqi_count) + ")", className="bold"),
                        html.H5(id="dlqi_mean", children=dlqi_mean, className="centered bold"),
                    ],
                    id="dlqi_mean_indicator",
                    className="mini_container  background_blue",
                ), 
               #html.Div(
               #     [
               #         html.H6("DLQI Std. (of " + str(dlqi_count) + ")", className="bold"),
               #         html.H5(id="dlqi_std", children=dlqi_std, className="centered"),
               #     ],
               #     id="dlqi_std_indicator",
               #     className="mini_container  background_blue",
               # ),                   
                html.Div(
                    [
                        html.H6("PASI Mean (of " + str(pasi_count) + ")", className="bold"),
                        html.H5(id="pasi_mean", children=pasi_mean, className="centered bold"),
                    ],
                    id="pasi_mean_indicator",
                    className="mini_container  background_blue",
                ),            
 
                html.Div(
                    [
                        html.H6("PGA Mean (of " + str(pga_count) + ")", className="bold"),
                        html.H5(id="pga_mean", children=pga_mean, className="centered bold"),
                    ],
                    id="pga_mean_indicator",
                    className="mini_container background_blue",
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
