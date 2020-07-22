from pathlib import Path

import pandas as pd
import plotly.express as px
from .database.db import runQuery

riesgo_asociado_df = pd.read_excel(list(Path("../").glob("**/riesgo_asociado.xlsx"))[0])

IDs_Unicos = riesgo_asociado_df[["ID", "Resultado Total", "Fecha"]].copy()
IDs_Unicos = (
    IDs_Unicos.drop_duplicates(keep="first")
    .reset_index()
    .sort_values("ID", ascending=True)
)
table = pd.pivot_table(
    IDs_Unicos, values="Fecha", index="ID", columns="Resultado Total", aggfunc="max"
)
df_IDs_Unicos = pd.DataFrame(data=table)
df_ra_g0 = (
    IDs_Unicos.groupby(["ID", "Resultado Total"], as_index=True)
    .count()["Fecha"]
    .unstack("Resultado Total")
)
df_ra_g0.fillna(0, inplace=True)
df_ra_g0["Consultas_totales"] = (
    df_ra_g0["No Aplica"] + df_ra_g0["Riesgo Alto"] + df_ra_g0["Riesgo Intermedio"]
)
#nutricion_df = df_ra_g0.groupby(["Consultas_totales"], as_index=False).sum()

nutricion_full_df = runQuery("select * from nutricion_y_dietetica_df")

nutricion_anno_df = nutricion_full_df.groupby(["anno"]).sum().reset_index()

nutricion_df = nutricion_anno_df[["anno", "alta_por_nutricion", "desnutricion_imc_<_18_5", "obesidad_imc_>30_sin_medicamento_de_ajuste"]]

nutricion_asociado = px.bar(
    nutricion_df,
    x="anno",
    y=["alta_por_nutricion", "desnutricion_imc_<_18_5", "obesidad_imc_>30_sin_medicamento_de_ajuste"],
    barmode="group",
)
