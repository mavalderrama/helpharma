# coding=utf-8

import datetime

now = datetime.datetime.now()

import plotly.express as px

from .database.db import runQuery


#### Patients

df = runQuery("select * from consulta_df")

patients = df["id"].unique().shape[0]

consultas = df.groupby(["ano", "mes"]).count().reset_index()[["mes", "id", "ano"]]

consultas = consultas[consultas["ano"].isin([now.year])]

consultas["mes"] = consultas["mes"].apply(
    lambda x: datetime.date(1900, x, 1).strftime("%B")
)

consultas_fig = px.bar(
    consultas,
    x="mes",
    y="id",
    title="Número de Consultas en {}".format(now.year),
    width=770,
    height=400,
    labels={"mes": "Meses", "id": "Consultas"},
)


# DLQI

df_indicators = runQuery("select id, fecha_consulta, dlqi, pasi, pga from sabana_df")

dlqi_set = df_indicators[~df_indicators["dlqi"].isnull()][["id", "fecha_consulta", "dlqi"]].sort_values(["id", "fecha_consulta"], ascending=False).drop_duplicates(["id"])["dlqi"].astype("float")
dlqi_count = dlqi_set.count()
dlqi_mean = dlqi_set.mean().round(2)
dlqi_std = dlqi_set.std().round(2)


# PASI

pasi_set = df_indicators[~df_indicators["pasi"].isnull()][["id", "fecha_consulta", "pasi"]].sort_values(["id", "fecha_consulta"], ascending=False).drop_duplicates(["id"])["pasi"].astype("float")
pasi_count = pasi_set.count()
pasi_mean = pasi_set.mean().round(2)
pasi_std =  pasi_set.std().round(2)


# PGA

pga_set = df_indicators[~df_indicators["pga"].isnull()][["id", "fecha_consulta", "pga"]].sort_values(["id", "fecha_consulta"], ascending=False).drop_duplicates(["id"])["pga"].astype("float")
pga_count = pga_set.count()
pga_mean = pga_set.mean().round(2)
pga_std = pga_set.std().round(2)
