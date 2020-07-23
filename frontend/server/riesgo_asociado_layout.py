import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from app import app
from .plots.riesgo_asociado import figura_riesgo_asociado, consultas_totales_df
from .plots.terapias import terapia_df, terapia_tot

# Define my layout
# Adding more CSS styles
colors = {"background": "#FFFFFF", "text": "#7FDBFF"}
layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.Img(
            src=app.get_asset_url("helpharma_logo.png"),
            alt="helPharma-Team12",
            width="200",
        ),
        html.H1(
            children="Biologic therapy for Psoriasis treatment | Failure estimation diagnostic decision support system"
        ),
        html.Div(
            children="""
        Team 12 - DS4A_2020.
    """
        ),
        # html.Label('Multi-Select Dropdown of Risk Levels'),
        html.Div(
            className="row",
            children=[
                html.Div(
                    [
                        dcc.Dropdown(
                            id="dropdown-options",
                            options=[
                                {"label": "No Aplica", "value": "No Aplica"},
                                {"label": "Riesgo Alto", "value": "Riesgo Alto"},
                                {
                                    "label": "Riesgo Intermedio",
                                    "value": "Riesgo Intermedio",
                                },
                            ],
                            value=["No Aplica", "Riesgo Alto", "Riesgo Intermedio"],
                            multi=True,
                        ),
                        dcc.Graph(
                            id="example-graph",
                            animate=True,
                            figure=figura_riesgo_asociado,
                        ),
                        dcc.Dropdown(
                            id="terapias-options",
                            options=[
                                {
                                    "label": "Alta del Programa",
                                    "value": "Alta del Programa",
                                },
                                {
                                    "label": "Seguimiento Presencial",
                                    "value": "SEGUIMIENTO PRESENCIAL",
                                },
                            ],
                            value=["Alta del Programa", "SEGUIMIENTO PRESENCIAL"],
                            multi=True,
                        ),
                        dcc.Graph(
                            id="terapias-graph", animate=True, figure=terapia_tot,
                        ),
                    ],
                    className="six columns",
                )
            ],
        ),
    ],
)


@app.callback(
    Output(component_id="example-graph", component_property="figure"),
    [Input(component_id="dropdown-options", component_property="value")],
)
def update_figure_riesgo_asociado(input_value):
    """
    update figure riesgo asociado
    :param input_value:
    :return:
    """
    return px.bar(
        consultas_totales_df, x="Consultas_totales", y=input_value, barmode="group"
    )


@app.callback(
    Output(component_id="terapias-graph", component_property="figure"),
    [Input(component_id="terapias-options", component_property="value")],
)
def update_terapias(input_value):
    """
    update figure riesgo asociado
    :param input_value:
    :return:
    """
    return px.bar(terapia_df, x="Terapias_totales", y=input_value, barmode="group")
