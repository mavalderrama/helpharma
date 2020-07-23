
import pandas as pd
import plotly.express as px

from .database.db import runQuery


nutricion_full_df = runQuery("select * from nutricion_y_dietetica_df")
nutricion_anno_df = nutricion_full_df.groupby(["anno"]).sum().reset_index()

nutricion_df = nutricion_anno_df[
    [
        "anno",
        "alta_por_nutricion",
        "desnutricion_imc_<_18_5",
        "obesidad_imc_>30_sin_medicamento_de_ajuste",
    ]
]

nutricion_asociado = px.bar(
    nutricion_df,
    x="anno",
    y=[
        "alta_por_nutricion",
        "desnutricion_imc_<_18_5",
        "obesidad_imc_>30_sin_medicamento_de_ajuste",
    ],
    barmode="group",
)
