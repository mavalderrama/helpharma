import plotly.express as px

from .database.db import runQuery

nutricion_full_df = runQuery("select * from nutricion_y_dietetica_df")

nutricion_full_df["semestre"] = nutricion_full_df["mes"].apply(
    lambda x: 0 if x < 7 else 1
)

nutricion_anno_df = nutricion_full_df.groupby(["anno"]).sum().reset_index()


### Desnutricion

nutricion_desnutricion_df = nutricion_anno_df[
    [
        "anno",
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
    ]
]

nutricion_desnutricion_fig = px.bar(
    nutricion_desnutricion_df,
    x="anno",
    y=[
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
    barmode="group",
)

# Otros sintomas

nutricion_sintomas_df = nutricion_anno_df[
    [
        "anno",
        "diabetes_controlada",
        "dislipidema_colesterol_total_>200_tg_>150",
        "sindrome_metabolico",
    ]
]

nutricion_sintomas_fig = px.bar(
    nutricion_desnutricion_df,
    x="anno",
    y=[
        "diabetes_controlada",
        "dislipidema_colesterol_total_>200_tg_>150",
        "sindrome_metabolico",
    ],
    barmode="group",
)

# Otros sintomas
# nutricion_frecuencias = df_nutricion.groupby(["anno", "semestre", "frecuencia_cita"])["frecuencia_cita"].count()
# nutricion_frecuencias.rename()
