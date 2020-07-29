# coding=utf-8

import datetime

now = datetime.datetime.now()

import plotly.express as px

from .database.db import runQuery

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
