# coding=utf-8

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from joblib import load
from pathlib import Path
import pandas as pd
import numpy as np

from app import app
from .plots.models import plot_indicator, get_model_params

model = list(Path(".").glob("**/model2.joblib"))[0]
patient_data = pd.DataFrame()

title = html.Div(
    className="title", children=[html.H1("Analysis Result")], id="models_title",
)


radio = dcc.RadioItems(
    id="medicamentos",
    options=[
        {"label": "Adalimumab", "value": "adalimumab"},
        {"label": "Certolizumab", "value": "certolizumab"},
        {"label": "Etanercept", "value": "etanercept"},
        {"label": "Golimumab", "value": "golimumab"},
        {"label": "Guselkumab", "value": "guselkumab"},
        {"label": "Infliximab", "value": "infliximab"},
        {"label": "Ixekinumab", "value": "ixekinumab"},
        {"label": "Secukinumab", "value": "secukinumab"},
        {"label": "Ustekinumab", "value": "ustekinumab"},
    ],
    value="adalimumab",
    labelStyle={"display": "block"},
    style={"column-count": "4"},
)

layout = html.Div(
    [
        dcc.Location(id="path"),
        html.Div(title),
        html.Div(
            html.Div(
                [
                    html.H4("Analyze Patient"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Name:"),
                                    html.Label(id="name", children="Jhon Doe"),
                                ],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("Age:"), html.Label(id="edad")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("Sex:"), html.Label(id="sexo")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("BMI:"), html.Label(id="imc")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("PASI:"), html.Label(id="pasi")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("DLQI:"), html.Label(id="dlqi")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("BSA:"), html.Label(id="bsa")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("PGA:"), html.Label(id="pga")],
                                style={"display": "block"},
                            ),
                        ],
                        style={"column-count": "4"},
                    ),
                    html.Div([html.H5("Biological Treatment"), radio]),
                    html.Div(
                        [
                            html.Button(
                                "Analyze",
                                id="calculate_model",
                                className="button",
                                autoFocus=True,
                            ),
                            html.Label(id="analysis_result", className="result",),
                        ],
                        style={"padding-top": "10px"},
                    ),
                ]
            ),
            className="pretty_container",
        ),
        html.H2(
            "Historical Data", style={"text-align": "center", "padding-top": "20px"},
        ),
        html.Div(
            [
                dcc.Graph(id="pasi_graph", animate=True,),
                dcc.Graph(id="dlqi_graph", animate=True,),
                dcc.Graph(id="bsa_graph", animate=True,),
            ],
            id="grafico",
        ),
    ]
)


@app.callback(
    [
        Output("pasi_graph", "figure"),
        Output("dlqi_graph", "figure"),
        Output("bsa_graph", "figure"),
    ],
    [Input("path", "search")],
)
def update_figures(search):
    """
    update figures
    :param search:
    :return:
    """
    identificador_paciente = search.split("=")[1]
    # print("patient id: {}".format(identificador_paciente))
    return (
        plot_indicator("pasi_rt", identificador_paciente, "weeks"),
        plot_indicator("dlqi", identificador_paciente, "weeks"),
        plot_indicator("bsa", identificador_paciente, "weeks"),
    )


@app.callback(
    [
        Output("edad", "children"),
        Output("sexo", "children"),
        Output("imc", "children"),
        Output("pasi", "children"),
        Output("dlqi", "children"),
        Output("bsa", "children"),
        Output("pga", "children"),
    ],
    [Input("path", "search")],
)
def update_patient_fields(search):
    """
    Update the patient fields
    :param search:
    :return:
    """
    global patient_data
    identificador_paciente = search.split("=")[1]
    patient_data = get_model_params(identificador_paciente)
    return (
        patient_data["edad"],
        patient_data["sexo_paciente"],
        patient_data["imc"],
        patient_data["pasi"],
        patient_data["dlqi"],
        patient_data["bsa"],
        patient_data["pga"],
    )


@app.callback(
    Output("analysis_result", "children"),
    [Input("calculate_model", "n_clicks"), Input("medicamentos", "value")],
)
def calculate_result(n_clicks, medicamento):
    global patient_data
    patient_data_copy = patient_data.copy()
    df_minmax = pd.DataFrame(
        data={
            "dlqi": [0, 30],
            "imc": [10, 35],
            "bsa": [0, 100],
            "edad": [0, 100],
            "pasi": [0, 72]
            # "depresion_total": [0, 10],
            # "ansiedad_total": [0, 10],
            # "trastorno_sexual_total": [0, 10],
            # "psi_total": [0, 10],
        },
        index=["min", "max"],
    )

    for c in df_minmax.columns:
        temp = patient_data_copy[c].astype("float")
        patient_data_copy[c] = (temp - df_minmax[c]["min"]) / (
            df_minmax[c]["max"] - df_minmax[c]["min"]
        )
    patient_data_copy["sexo_paciente"] = patient_data_copy["sexo_paciente"].apply(
        lambda x: -1 if x == "m" else 1
    )

    medicinas = {
        "certolizumab": 0,
        "adalimumab": 0,
        "etanercept": 0,
        "golimumab": 0,
        "guselkumab": 0,
        "infliximab": 0,
        "ixekinumab": 0,
        "secukinumab": 0,
        "ustekinumab": 0,
        "mometasona": 0,
    }

    medicinas[medicamento] = 1

    if n_clicks:
        clf = load(model)
        probability = clf.predict_proba(
            np.array(
                [
                    [
                        patient_data_copy["pasi"],
                        patient_data_copy["edad"],
                        patient_data_copy["sexo_paciente"],
                        patient_data_copy["imc"],
                        patient_data_copy["dlqi"],
                        patient_data_copy["bsa"],
                        patient_data_copy["pga"],
                        medicinas["adalimumab"],
                        medicinas["certolizumab"],
                        medicinas["etanercept"],
                        medicinas["golimumab"],
                        medicinas["guselkumab"],
                        medicinas["infliximab"],
                        medicinas["ixekinumab"],
                        medicinas["secukinumab"],
                        medicinas["ustekinumab"],
                        medicinas["mometasona"],
                    ],
                ]
            )
        )

        print("proba: ", probability)
        return "The therapeutic failure rate for this patient is: {}%".format(
            round(probability[0][1] * 100, 1)
        )
    return ""
