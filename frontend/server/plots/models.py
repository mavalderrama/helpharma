import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .database.db import runQuery

sabana_df = runQuery("select * from sabana_df")

sabana_df=sabana_df.astype({"fecha_consulta":'datetime64',"fecha_nacimiento":'datetime64'})

sabana_df['pasi_rt']= sabana_df[["pasi", "resultado_total"]].max(axis=1)

sabana_df['delta_date'] = sabana_df.groupby('id')['fecha_consulta'].diff(1)
sabana_df['delta_date_int'] = sabana_df.delta_date.dt.days.fillna(0).astype(int)
sabana_df['days_acum'] = sabana_df.groupby('id')['delta_date_int'].cumsum()
sabana_df['weeks_acum'] = round(sabana_df['days_acum']/7,0).astype(int)

def plot_indicator (indicator, id_pat=[],time_axe='weeks'):

    df_indicator = sabana_df[['id','fecha_consulta','weeks_acum',#llave y semanas acumuladas
                              'sexo_paciente','fecha_nacimiento','diagnostico_principal','imc', #variables generales
                              indicator
                             ]].copy().groupby(['id','fecha_consulta']).last()
    df_indicator.dropna(subset=[indicator],inplace=True)
    df_indicator_ = df_indicator.reset_index()
    
    if len(id_pat)==0 and time_axe=='date':
        fig = px.line(df_indicator_, x="fecha_consulta", y=indicator, color='id')
        fig.update_layout(plot_bgcolor="whitesmoke")
        #fig.show()
        return fig
    
    elif len(id_pat)!=0 and time_axe=='date':
        df_indicator_ = df_indicator_[df_indicator_.id==id_pat]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_indicator_['fecha_consulta'],
                                 y=df_indicator_[indicator],
                                 mode='lines+markers',name=id_pat,))
        fig.update_layout(xaxis_title='date',
                          yaxis_title=str(indicator),
                          showlegend=True,
                          plot_bgcolor="whitesmoke")
        #fig.show()
        return fig
    
    elif len(id_pat)==0 and time_axe=='weeks':
        fig = px.line(df_indicator_, x="weeks_acum", y=indicator, color='id')
        fig.update_layout(plot_bgcolor="whitesmoke")
        #fig.show()
        return fig
    
    elif len(id_pat)!=0 and time_axe=='weeks':
        df_indicator_ = df_indicator_[df_indicator_.id==id_pat]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_indicator_['weeks_acum'],
                                 y=df_indicator_[indicator],
                                 mode='lines+markers',name=id_pat,))
        fig.update_layout(xaxis_title='weeks_acum',
                          yaxis_title=str(indicator),
                          showlegend=True,
                          plot_bgcolor="whitesmoke")
        #fig.show()
        return fig


