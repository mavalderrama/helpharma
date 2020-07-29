import pandas as pd
import plotly.express as px

from .database.db import runQuery

df_Terapia_fisica = runQuery("select * from terapia_fisica")

IDs_Unicos = df_Terapia_fisica[["id", "Modalidad cita", "Fecha"]].copy()
IDs_Unicos = (
    IDs_Unicos.drop_duplicates(keep="first")
    .reset_index()
    .sort_values("id", ascending=True)
)
table = pd.pivot_table(
    IDs_Unicos, values="Fecha", index="id", columns="Modalidad cita", aggfunc="max"
)
df_IDs_Unicos = pd.DataFrame(data=table)
df_tf_g0 = (
    IDs_Unicos.groupby(["id", "Modalidad cita"], as_index=True)
    .count()["Fecha"]
    .unstack("Modalidad cita")
)
df_tf_g0.fillna(0, inplace=True)
df_tf_g0["Terapias_totales"] = (
    df_tf_g0["Alta del Programa"] + df_tf_g0["SEGUIMIENTO PRESENCIAL"]
)
terapia_df = df_tf_g0.groupby(["Terapias_totales"], as_index=False).sum()

terapia_tot = px.bar(
    terapia_df,
    x="Terapias_totales",
    y=["Alta del Programa", "SEGUIMIENTO PRESENCIAL"],
    barmode="group",
)
