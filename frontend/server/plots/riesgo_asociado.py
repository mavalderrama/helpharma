from pathlib import Path

import pandas as pd
import plotly.express as px

from .database.db import runQuery

# riesgo_asociado_df = pd.read_excel(list(Path("../").glob("**/riesgo_asociado.xlsx"))[0])
riesgo_asociado_df = runQuery("select * from riesgo_asociado")

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
consultas_totales_df = df_ra_g0.groupby(["Consultas_totales"], as_index=False).sum()

figura_riesgo_asociado = px.bar(
    consultas_totales_df,
    x="Consultas_totales",
    y=["No Aplica", "Riesgo Alto", "Riesgo Intermedio"],
    barmode="group",
)
