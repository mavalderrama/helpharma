
import pandas as pd
import plotly.express as px

from .database.db import runQuery


nutricion_full_df = runQuery("select * from nutricion_y_dietetica_df")
nutricion_anno_df = nutricion_full_df.groupby(["anno"]).sum().reset_index()

       
#'diabetes_controlada',
#'dislipidema_colesterol_total_>200_tg_>150', 'hba1c_>7',
#'hta_controlada', 'hta_no_controlada',
#'otro_motivo',
#'pacientes_con_sobrepeso_imc_25-29',
#'sin_medicamento_que_requiera_ajuste', 'sindrome_metabolico',
#'tratamiento_con_medicamento_que_requiera_ajuste_por_peso_con_so'
       
nutricion_desnutricion_df = nutricion_anno_df[
    [
        "anno",
        "alta_por_nutricion",
        "desnutricion_imc_<_18_5",
        "obesidad_imc_>30_sin_medicamento_de_ajuste",
    ]
]

nutricion_desnutricion_fig = px.bar(
    nutricion_desnutricion_df,
    x="anno",
    y=[
        "alta_por_nutricion",
        "desnutricion_imc_<_18_5",
        "obesidad_imc_>30_sin_medicamento_de_ajuste",
    ],
    barmode="group",
)
