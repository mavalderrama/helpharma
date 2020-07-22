import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from app import app
from .plots.nutricion import nutricion_asociado, nutricion_df

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
            children="Biologic therapy for Psoriasis treatment | Failure estimation diagnostic decision support system | Nutrición"
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
                            id="nutricion-dropdown-options",
                            options=[
                                {
                                    "label": "Alta Nutricion",
                                    "value": "alta_por_nutricion",
                                },
                                {
                                    "label": "Desnutricion (IMC < 18.5)",
                                    "value": "desnutricion_imc_<_18_5",
                                },
                                {
                                    "label": "Obesidad (IMC > 30, sin medic.)",
                                    "value": "obesidad_imc_>30_sin_medicamento_de_ajuste",
                                },
                            ],
                            value=[
                                "alta_por_nutricion",
                                "desnutricion_imc_<_18_5",
                                "obesidad_imc_>30_sin_medicamento_de_ajuste",
                            ],
                            multi=True,
                        ),
                        dcc.Graph(
                            id="nutricion-graph",
                            animate=True,
                            figure=nutricion_asociado,
                        ),
                    ],
                    className="six columns",
                )
            ],
        ),
    ],
)


@app.callback(
    Output(component_id="nutricion-graph", component_property="figure"),
    [Input(component_id="nutricion-dropdown-options", component_property="value")],
)
def nutricion_update(input_value):
    """
    update figure riesgo asociado
    :param input_value:
    :return:
    """
    return px.bar(nutricion_df, x="anno", y=input_value, barmode="group")
