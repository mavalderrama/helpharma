import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from .database.db import runQuery

sabana_df = runQuery("select * from sabana_df")

sabana_df = sabana_df.astype(
    {
        "fecha_consulta": "datetime64",
        "fecha_nacimiento": "datetime64",
        "id": int,
        "pasi": float,
        # "resultado_total": float,
        "dlqi": float,
        "bsa": float,
    }
)

sabana_df.dropna(subset=["fecha_consulta"], inplace=True)

sabana_df["pasi_rt"] = sabana_df[["pasi"]]

# sabana_df["delta_date"] = sabana_df.groupby("id")["fecha_consulta"].diff(1)
# sabana_df["delta_date_int"] = sabana_df.delta_date.dt.days.fillna(0).astype(int)
# sabana_df["days_acum"] = sabana_df.groupby("id")["delta_date_int"].cumsum()
# sabana_df["weeks_acum"] = round(sabana_df["days_acum"] / 7, 0).astype(int)

sabana_df["weeks_acum"] = 0
sabana_df = sabana_df.sort_values(by=["fecha_consulta"], ascending=True)

# for name, group in sabana_df.groupby("id"):
#     index = group.index
#     sabana_df.loc[index, "weeks_acum"] = (
#         sabana_df.loc[index, "fecha_consulta"].dt.to_period("W").diff(1)
#     )
# sabana_df.dropna(subset=["weeks_acum"], inplace=True)
# sabana_df["weeks_acum"] = sabana_df["weeks_acum"].apply(lambda x: x.n)
# for name, group in sabana_df.groupby("id"):
#     index = group.index
#     sabana_df.loc[index, "weeks_acum"] = sabana_df.loc[index, "weeks_acum"].cumsum()


def plot_indicator(indicator, id_pat=[], time_axe="weeks"):

    df_indicator = (
        sabana_df[
            [
                "id",
                "fecha_consulta",
                "weeks_acum",  # llave y semanas acumuladas
                "sexo_paciente",
                "fecha_nacimiento",
                "diagnostico_principal",
                "imc",  # variables generales
                indicator,
            ]
        ].copy()
        # .groupby(["id", "fecha_consulta"])
        # .last()
    )

    df_indicator.dropna(subset=[indicator], inplace=True)
    df_indicator = df_indicator.reset_index()

    if type(id_pat) is list:
        df_indicator = df_indicator[df_indicator["id"].isin(id_pat)]
    else:
        df_indicator = df_indicator[df_indicator["id"].isin([id_pat])]

    df_indicator["weeks_acum"] = df_indicator["fecha_consulta"].dt.to_period("W").diff()

    df_indicator.dropna(subset=["weeks_acum"], inplace=True)
    print("indi", df_indicator.shape)

    df_indicator["weeks_acum"] = df_indicator["weeks_acum"].apply(lambda x: x.n)

    df_indicator["weeks_acum"] = df_indicator["weeks_acum"].cumsum()

    if len(id_pat) == 0 and time_axe == "date":
        fig = px.line(df_indicator, x="fecha_consulta", y=indicator, color="id")
        fig.update_layout(plot_bgcolor="whitesmoke")
        # fig.show()
        return fig

    elif len(id_pat) != 0 and time_axe == "date":
        df_indicator = df_indicator[df_indicator.id == id_pat]
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=df_indicator["fecha_consulta"],
                y=df_indicator[indicator],
                mode="lines+markers",
                name=id_pat,
            )
        )
        fig.update_layout(
            xaxis_title="date",
            yaxis_title=str(indicator),
            showlegend=True,
            plot_bgcolor="whitesmoke",
        )
        # fig.show()
        return fig

    elif len(id_pat) == 0 and time_axe == "weeks":
        fig = px.line(df_indicator, x="weeks_acum", y=indicator, color="id")
        fig.update_layout(plot_bgcolor="whitesmoke")
        # fig.show()
        return fig

    elif len(id_pat) != 0 and time_axe == "weeks":
        df_indicator = df_indicator[df_indicator["id"].isin([id_pat])]
        print(df_indicator.shape)
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=df_indicator["weeks_acum"],
                y=df_indicator[indicator],
                mode="lines+markers",
                name=id_pat,
            )
        )
        fig.update_layout(
            xaxis_title="weeks_acum",
            yaxis_title=str(indicator),
            showlegend=True,
            plot_bgcolor="whitesmoke",
        )
        # fig.show()
        return fig
