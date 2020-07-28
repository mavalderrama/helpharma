import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from app import app
from .plots.nutricion import (
    nutricion_desnutricion_fig,
    nutricion_desnutricion_df,
    nutricion_sintomas_fig,
    nutricion_sintomas_df,
)

# Define my layout
# Adding more CSS styles
colors = {"background": "#FFFFFF", "text": "#7FDBFF"}

title = html.Div(
    className="title", children=[html.H1("Nutrition Board")], id="nutrition_title"
)

layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        title,
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
                                {
                                    "label": "Diabetes Controlada",
                                    "value": "diabetes_controlada",
                                },
                                {
                                    "label": "Dislipidemia",
                                    "value": "dislipidema_colesterol_total_>200_tg_>150",
                                },
                                {
                                    "label": "Sindrome Metabolico",
                                    "value": "sindrome_metabolico",
                                },
                                {"label": "hba1c >7", "value": "hba1c_>7",},
                                {"label": "HTA controlada", "value": "hta_controlada",},
                                {
                                    "label": "HTA no controlada",
                                    "value": "hta_no_controlada",
                                },
                                {
                                    "label": "Pacientes sobrepeso imc 25-29",
                                    "value": "pacientes_con_sobrepeso_imc_25-29",
                                },
                                {
                                    "label": "Sin medic. requiera ajuste",
                                    "value": "sin_medicamento_que_requiera_ajuste",
                                },
                                {
                                    "label": "Tratamiento con medic. ajuste peso",
                                    "value": "tratamiento_con_medicamento_que_requiera_ajuste_por_peso_con_so",
                                },
                                {"label": "Otro motivo", "value": "otro_motivo",},
                            ],
                            value=[
                                "alta_por_nutricion",
                                "desnutricion_imc_<_18_5",
                                "obesidad_imc_>30_sin_medicamento_de_ajuste",
                                "diabetes_controlada",
                                "dislipidema_colesterol_total_>200_tg_>150",
                                "sindrome_metabolico",
                                "hba1c_>7",
                                "hta_controlada",
                                "hta_no_controlada",
                                "otro_motivo",
                                "pacientes_con_sobrepeso_imc_25-29",
                                "sin_medicamento_que_requiera_ajuste",
                                "tratamiento_con_medicamento_que_requiera_ajuste_por_peso_con_so",
                            ],
                            multi=True,
                        ),
                        dcc.Graph(
                            id="nutricion-graph",
                            animate=True,
                            figure=nutricion_desnutricion_fig,
                        ),
                        dcc.Dropdown(
                            id="nutricion-sintomas-options",
                            options=[
                                {
                                    "label": "Diabetes Controlada",
                                    "value": "diabetes_controlada",
                                },
                                {
                                    "label": "Dislipidemia",
                                    "value": "dislipidema_colesterol_total_>200_tg_>150",
                                },
                                {
                                    "label": "Sindrome Metabolico",
                                    "value": "sindrome_metabolico",
                                },
                            ],
                            value=[
                                "diabetes_controlada",
                                "dislipidema_colesterol_total_>200_tg_>150",
                                "sindrome_metabolico",
                            ],
                            multi=True,
                        ),
                        dcc.Graph(
                            id="nutricion-sintomas-graph",
                            animate=True,
                            figure=nutricion_sintomas_fig,
                        ),
                        dcc.Graph(
                            id="nutricion-sintomas-graph2",
                            animate=True,
                            figure=px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8]),
                        ),
                    ],
                    className="six columns",
                )
            ],
        ),
    ],
)


# fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
# fig.show()


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
    return px.bar(nutricion_desnutricion_df, x="anno", y=input_value, barmode="group")


@app.callback(
    Output(component_id="nutricion-sintomas-graph", component_property="figure"),
    [Input(component_id="nutricion-sintomas-options", component_property="value")],
)
def nutricion_sintomas_update(input_value):
    return px.bar(nutricion_sintomas_df, x="anno", y=input_value, barmode="group")
