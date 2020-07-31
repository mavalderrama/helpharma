# coding=utf-8

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from joblib import load

from app import app
from .plots.models import plot_indicator, get_model_params

title = html.Div(
    className="title", children=[html.H1("Analysis Result")], id="models_title",
)

radio = dcc.RadioItems(
    id="medicamentos",
    options=[
        {"label": "Adalimumab", "value": "a"},
        {"label": "Certolizumab", "value": "b"},
        {"label": "Etanercept", "value": "c"},
        {"label": "Golimumab", "value": "d"},
        {"label": "Guselkumab", "value": "e"},
        {"label": "Infliximab", "value": "f"},
        {"label": "Ixekinumab", "value": "g"},
        {"label": "Secukinumab", "value": "h"},
        {"label": "Ustekinumab", "value": "i"},
    ],
    value="a",
    labelStyle={"display": "block"},
    style={"column-count": "4"},
)

modal = html.Div(
    [
        dbc.Button("Open", id="open-centered"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("This modal is vertically centered"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-centered", className="ml-auto")
                ),
            ],
            id="modal-centered",
            centered=True,
        ),
    ]
)

"""
pasi
edad
sexo
imc
dlqi
bsa
pga
"""

layout = html.Div(
    [
        dcc.Location(id="path"),
        html.Div(title),
        html.Div(
            html.Div(
                [
                    html.H4("Analizar Paciente"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Nombre:"),
                                    html.Label(id="name", children="Jhon Doe"),
                                ],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("Edad:"), html.Label(id="edad")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("Sexo:"), html.Label(id="sexo")],
                                style={"display": "block"},
                            ),
                            html.Div(
                                [html.H5("IMC:"), html.Label(id="imc")],
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
                    html.Div([html.H5("Medicamento a Suministrar"), radio]),
                    html.Div(
                        [html.Button("Analizar", className="button", autoFocus=True,)],
                        style={"padding-top": "10px"},
                    ),
                ]
            ),
            className="pretty_container",
        ),
        html.H2(
            "Histórico de Clinimetrías",
            style={"text-align": "center", "padding-top": "20px"},
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
    print("patient id: {}".format(identificador_paciente))
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
    identificador_paciente = search.split("=")[1]
    data = get_model_params(identificador_paciente)
    return (
        data["edad"],
        data["sexo_paciente"],
        data["imc"],
        data["pasi"],
        data["dlqi"],
        data["bsa"],
        data["pga"],
    )


@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
