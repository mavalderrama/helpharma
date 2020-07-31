import pandas as pd
import plotly.express as px

from .database.db import runQuery

nutricion_full_df = runQuery("select * from nutricion_y_dietetica_df")

nutricion_full_df["semestre"] = nutricion_full_df["mes"].apply(
    lambda x: 0 if x < 7 else 1
)

nutricion_anno_df = nutricion_full_df.groupby(["anno"]).sum().reset_index()

### Desnutricion

desnutricion_df = (
    nutricion_full_df[~nutricion_full_df["desnutricion_imc_<_18_5"].isnull()][
        ["id", "fecha", "desnutricion_imc_<_18_5"]
    ]
    .sort_values(["id", "fecha"], ascending=False)
    .drop_duplicates(["id"])["desnutricion_imc_<_18_5"]
    .astype("float")
)
desnutricion_sum = desnutricion_df.sum()

### Sobrepeso

obesidad_df = (
    nutricion_full_df[
        ~nutricion_full_df["obesidad_imc_>30_sin_medicamento_de_ajuste"].isnull()
    ][["id", "fecha", "obesidad_imc_>30_sin_medicamento_de_ajuste"]]
    .sort_values(["id", "fecha"], ascending=False)
    .drop_duplicates(["id"])["obesidad_imc_>30_sin_medicamento_de_ajuste"]
    .astype("float")
)
obesidad_sum = obesidad_df.sum()

### Nutricion

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

# Medicamentos distribucion
medicamentos_str = """medicamento_acido_folico
medicamento_acido_folico/mometasona
medicamento_acido_retinoico
medicamento_acido_salicilico/betametasona
medicamento_acido_salicilico/mometasona
medicamento_acitretin
medicamento_adalimumab
medicamento_alquitran_de_hulla
medicamento_anticonceptivos
medicamento_bemerin
medicamento_betametasona
medicamento_calcipotriol
medicamento_calcipotriol+esteroide
medicamento_cefalexina
medicamento_certolizumab
medicamento_cetirizina
medicamento_ciclopirox
medicamento_ciclosporina
medicamento_clindamicina
medicamento_clindamicina/rifampicina
medicamento_clobetazol
medicamento_clorfeniramina
medicamento_clotrimazol
medicamento_dapsona
medicamento_deflazacort
medicamento_dermacortine
medicamento_dermovate
medicamento_desonida
medicamento_dicloxacilina
medicamento_difenhidramina
medicamento_diprosalic
medicamento_doxiciclina
medicamento_eritromicina
medicamento_espironolactona
medicamento_etanercept
medicamento_etoricoxib
medicamento_fototerapia_uv_a
medicamento_fototerapia_uv_b
medicamento_fototerapia_uva_1
medicamento_golimumab
medicamento_guselkumab
medicamento_hidrocortizona
medicamento_infiltraciones
medicamento_infliximab
medicamento_isoniazida
medicamento_isotretinoina
medicamento_ixekinumab
medicamento_ketoconazol
medicamento_leflunomida
medicamento_metotrexate
medicamento_mometasona
medicamento_mupirocina
medicamento_piridoxina
medicamento_prednisolona
medicamento_quimiofototerapia
medicamento_ranitidina
medicamento_rifampicina
medicamento_secukinumab
medicamento_soridem
medicamento_sulfasalazina
medicamento_tacrolimus
medicamento_tazaroteno
medicamento_tetraciclina_clorhidrato
medicamento_tofacitinib
medicamento_trimetoprim/sulfametoxazol
medicamento_urea_granulada
medicamento_ustekinumab
medicamento_vancomicina"""
medicamentos = medicamentos_str.split("\n")

# medicamentos_columns = 'id,' + ','.join(medicamentos)
medicamentos_columns = '"id","' + '","'.join(medicamentos) + '"'
df_medicamentos = runQuery(f"select {medicamentos_columns} from sabana_df")

meds_array = []
values_array = []
for i in range(0, len(medicamentos)):
    meds_array.append(medicamentos[i])
    values_array.append(
        df_medicamentos[
            (~df_medicamentos[medicamentos[i]].isnull())
            & (df_medicamentos[medicamentos[i]] > 0)
        ]
        .sort_values(["id"], ascending=False)
        .drop_duplicates(["id"])[medicamentos[i]]
        .sum()
    )  # [full_medicamentos] #.head() #.drop_duplicates(["id"]) #.isnull().sum()
df_medicamentos = pd.DataFrame(
    {"medicamentos": meds_array, "cantidad_personas": values_array}
)
medicamentos_distribucion_fig = px.pie(
    df_medicamentos,
    values="cantidad_personas",
    names="medicamentos",
    title="Distribución de Medicamentos",
)
