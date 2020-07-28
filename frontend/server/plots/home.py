# coding=utf-8

import plotly.express as px

from .database.db import runQuery

df = runQuery("select * from consulta_df")

patients = df["id"].unique().shape[0]

# sex = patients["sexo_paciente"].value_counts().reset_index()
