# coding=utf-8

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from .plots.models import plot_indicator

from app import app

#layout = html.Div([dcc.Location(id="path"), html.Div(id="patient_id")])


identificador_paciente = '537530'

@app.callback(Output("patient_id", "children"), [Input("path", "search")])
def update_output(search):
    """
    update
    :param search:
    :return:
    """
    global identificador_paciente
    identificador_paciente = search.split("=")[1]
    print(identificador_paciente)
    return search.split("=")[1]

pasi_rt_plot = plot_indicator('pasi_rt',identificador_paciente,'weeks')
#dlqi_plot = plot_indicator('dlqi',identificador_paciente,'weeks')
#bsa_plot = plot_indicator('bsa',identificador_paciente,'weeks')

layout = html.Div([dcc.Location(id="path"), html.Div(id="patient_id"), html.Div([
                                dcc.Graph(
                                    id="pasi_graph",
                                    animate=True,
                                    figure=pasi_rt_plot,
                                )    
],id="grafico")])