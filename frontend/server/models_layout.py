# coding=utf-8

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from .plots.models import plot_indicator

title = html.Div(
    className="title", children=[html.H1("Analysis Result")], id="models_title",
)


layout = html.Div(
    [
        dcc.Location(id="path"),
        html.Div(title),
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
def update_output(search):
    """
    update
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


# dlqi_plot = plot_indicator('dlqi',identificador_paciente,'weeks')
# bsa_plot = plot_indicator('bsa',identificador_paciente,'weeks')
