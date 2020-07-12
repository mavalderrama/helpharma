# Import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

## Riesgo Asociado vs Consultas (1,1) ##
df_Riesgo_asociado = pd.read_excel("/helpharma/data/Riesgo asociado.xlsx")
IDs_Unicos=df_Riesgo_asociado[['ID','Resultado Total','Fecha']].copy()
IDs_Unicos=IDs_Unicos.drop_duplicates(keep="first").reset_index().sort_values('ID',ascending=True)
table=pd.pivot_table(IDs_Unicos,values='Fecha',index='ID',columns='Resultado Total',aggfunc='max')
df_IDs_Unicos=pd.DataFrame(data=table)
df_ra_g0=IDs_Unicos.groupby(['ID','Resultado Total'],as_index=True).count()['Fecha'].unstack('Resultado Total')
df_ra_g0.fillna(0,inplace=True)
df_ra_g0['Consultas_totales']=df_ra_g0['No Aplica']+df_ra_g0['Riesgo Alto']+df_ra_g0['Riesgo Intermedio']
ct=df_ra_g0.groupby(['Consultas_totales'],as_index=False).sum()

## Terapia Fisica (1,2) ##
df_Terapia_fisica = pd.read_excel("/helpharma/data/Terapia fisica.xlsx")
IDs_Unicos=df_Terapia_fisica[['id','Modalidad cita','Fecha']].copy()
IDs_Unicos=IDs_Unicos.drop_duplicates(keep="first").reset_index().sort_values('id',ascending=True)
table=pd.pivot_table(IDs_Unicos,values='Fecha',index='id',columns='Modalidad cita',aggfunc='max')
df_IDs_Unicos=pd.DataFrame(data=table)
df_tf_g0=IDs_Unicos.groupby(['id','Modalidad cita'],as_index=True).count()['Fecha'].unstack('Modalidad cita')
df_tf_g0.fillna(0,inplace=True)
df_tf_g0['Terapias_totales']=df_tf_g0['Alta del Programa']+df_tf_g0['SEGUIMIENTO PRESENCIAL']
dt=df_tf_g0.groupby(['Terapias_totales'],as_index=False).sum()

# Read style of internet (css file)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# Init my app dash and define my style CSS
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.bar(ct,
             x="Consultas_totales", 
             y=["No Aplica","Riesgo Alto","Riesgo Intermedio"], 
             barmode="group")

fog = px.bar(dt,
             x="Terapias_totales", 
             y=["Alta del Programa","SEGUIMIENTO PRESENCIAL"], 
             barmode="group")

# Define my layout
# Adding more CSS styles
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Define LAYOUT
#This use HTML tags
# html.H1 : The <h1> to <h6> tags are used to define HTML headings.
# html.Div : The <div> tag defines a division or a section in an HTML document.
#app.layout = html.Div(children=[
app.layout = html.Div(style={'backgroundColor': colors['background']},children=
 [
    html.Img(src=app.get_asset_url('Logo con corazon-01.png'),alt='helPharma-Team12',width='200'),
     html.H1(children='Biologic therapy for Psoriasis treatment | Failure estimation diagnostic decision support system'),

    html.Div(children='''
        Team 12 - DS4A_2020.
    '''),
    
    #html.Label('Multi-Select Dropdown of Risk Levels'),
    html.Div
     (className='row',
        children=
         [
            html.Div([dcc.Dropdown
            (
            id='dropdown-options',
            options=[
            {'label': 'No Aplica', 'value': 'No Aplica'},
            {'label': 'Riesgo Alto', 'value': 'Riesgo Alto'},
            {'label': 'Riesgo Intermedio', 'value': 'Riesgo Intermedio'}
            ],
            value=['No Aplica', 'Riesgo Alto', 'Riesgo Intermedio'],
            multi=True
            ),

        dcc.Graph
        (
        id='example-graph',
        animate=True,
        figure = fig
        )],className='six columns'),
    
        html.Div([dcc.Dropdown
        (
        id='dropdown-options2',
        options=[
            {'label': 'SEGUIMIENTO PRESENCIAL', 'value': 'SEGUIMIENTO PRESENCIAL'},
            {'label': 'Alta del Programa', 'value': 'Alta del Programa'}
            ],
            value=['SEGUIMIENTO PRESENCIAL', 'Alta del Programa'],
            multi=True
        ),

        dcc.Graph(
        id='example-graph2',
        animate=True,
        figure = fog
        )],className='six columns')
        ]
     )
    
 ]
)

@app.callback(
    Output(component_id='example-graph',component_property='figure'),
    [Input(component_id='dropdown-options', component_property='value')]
)
def update_figure(input_value):
    figure = px.bar(ct, 
                       x="Consultas_totales", 
                       y=input_value, 
                       barmode="group")
             
    return figure

@app.callback(
    Output(component_id='example-graph2',component_property='figure'),
    [Input(component_id='dropdown-options2', component_property='value')]
)
def update_figure(input_value):
    figure = px.bar(dt, 
                       x="Terapias_totales", 
                       y=input_value, 
                       barmode="group")
             
    return figure

# Configuring APP running as Web 
if __name__ == '__main__':
    # app.run_server(debug=True)
    if len(sys.argv) > 1:
        app.run_server(host='0.0.0.0', port=sys.argv[1])
    else:
        app.run_server(host='0.0.0.0', port=8080)
