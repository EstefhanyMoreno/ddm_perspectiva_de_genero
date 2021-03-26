import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import requests
import re
import json
import requests
import numpy as np

TA = pd.read_csv(r'C:\Users\Milexis\Desktop\Nueva carpeta\Evolucion-de-la-poblacion-economicamente-activa-en-Mexico.csv')
TA.drop(['Nation ID', 'Quarter', 'Nation', 'Time', 'Sex ID'], axis =1, inplace=True)
TA.columns = ['Año', 'Sexo', 'Workforce', 'Workforce Total', 'porcentaje']

def percent(x):
    return int(x*100)
TA['porcentaje'] = TA['porcentaje'].apply(percent)
fig = px.line(TA, x="Año", y="porcentaje", color='Sexo', title = 'Población Total activa en México')

#Importo las coordenadas de los estados
cord = pd.read_csv(r'C:\Users\Milexis\Desktop\Nueva carpeta\new.txt')
cord.drop('Estado', axis = 1, inplace = True)

Data_Worker_Act = pd.read_csv(r'C:\Users\Milexis\Desktop\Nueva carpeta\Data_Worker_Act.csv')

#1
df_salario_total = pd.pivot_table(Data_Worker_Act, 
                    index = ['Año','Sexo',], 
                    values = 'Salario Mensual', aggfunc = np.mean, fill_value =0).unstack().fillna(0)
df_salario_total.columns = ['Hombre', 'Mujer']
fig1 = px.line(data_frame=df_salario_total, title = 'Población Total activa en México')


#2
def clas_Estado(value):
    dff = Data_Worker_Act[(Data_Worker_Act['Clasificación de trabajos']== value)]
    dff = dff.groupby(['Año', 'Sexo']).agg({'Personal': sum, 'Salario Mensual': np.mean})
    dff.reset_index(inplace=True)
    
    fig2 = px.line(data_frame=dff,
        x="Año",
        y='Personal',
        color='Sexo', title = 'Población Total activa en los Estados de México')
    return fig2

#4
def estado_Salario(clas):
    df4 = Data_Worker_Act[(Data_Worker_Act['Clasificación de trabajos']== clas)]
    df4 = df4.groupby(['Año', 'Sexo']).agg({'Personal': sum, 'Salario Mensual': np.mean})
    df4.reset_index(inplace=True)
    fig4 = px.line(data_frame=df4,
        x="Año",
        y='Salario Mensual',
        color="Sexo", title = 'Población Total activa en los Estados de México')
    return fig4


    
#____________________________________________________________________________________________________________________
req_sec = requests.get('https://api.datamexico.org/tesseract/cubes/inegi_enoe/aggregate.jsonrecords?captions%5B%5D=Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity+ES&captions%5B%5D=Sex.Sex.Sex.Sex+ES&captions%5B%5D=Geography+Code.Geography.State.State+slug+ES&captions%5B%5D=Occupation+Actual+Job.Occupation.Occupation.Occupation+ES&cuts%5B%5D=Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.2&cuts%5B%5D=Occupation+Actual+Job.Occupation.Occupation.1621%2C1629%2C2271%2C2272%2C2543%2C2640%2C2651%2C3113%2C3232&cuts%5B%5D=Geography+Code.Geography.State.1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32&cuts%5B%5D=Sex.Sex.Sex.1%2C2&drilldowns%5B%5D=Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity.Classification+of+Formal+and+Informal+Jobs+of+the+First+Activity&drilldowns%5B%5D=Date.Date.Year&drilldowns%5B%5D=Sex.Sex.Sex&drilldowns%5B%5D=Geography+Code.Geography.State&drilldowns%5B%5D=Occupation+Actual+Job.Occupation.Occupation&drilldowns%5B%5D=Age+Group.Age+Group.Age&measures%5B%5D=Workforce&measures%5B%5D=Monthly+Wage&parents=false&sparse=false')
req_sec = req_sec.json()
Data_Sec = pd.DataFrame(req_sec['data'])
def quit(string):
    string = string[:-3]
    return string.replace('-',' ')
Data_Sec['State'] = Data_Sec['State'].apply(quit)
Data_Sec.drop(['Sex ID', 'Classification of Formal and Informal Jobs of the First Activity ID',
               'Classification of Formal and Informal Jobs of the First Activity',
              'Occupation ID'], axis= 1, inplace = True)
Data_Sec.columns = ['Año', 'Sexo', 'ID Estado', 'Estado', 'Ocupacion', 'Edad', 'Personal',
                    'Salario Mensual']

def acomodarOcu(string):
    if string == 'Desarrolladores y Analistas de Software y Multimedia':
        return 'Desarrolladores y Anls de Soft. y Multimedia'
    if string == 'Supervisores de Técnicos Eléctricos, en Electrónica y de Equipos en Telecomunicaciones y Electromecánicos':
        return 'Superv. de Electrónica, Telecomunicaciones y Electromecánicos'
    if string == 'Técnicos en la Instalación y Reparación de Redes, Equipos y en Sistemas Computacionales':
        return 'Téc. de Redes, Equipos y Sist. Computacional'
    if string == 'Otros Coordinadores y Jefes de Área en Informática, Telecomunicaciones, Transporte y en Investigación y Desarrollo Tecnológico, no Clasificados Anteriormente':
        return 'Otros Coord. y Jefes Área Informática y Desarrollo Tecn.'
    return string

Data_Sec['Ocupacion'] = Data_Sec['Ocupacion'].apply(acomodarOcu)
#_______________________________________________________________________________________________________________________

#6
def ocupacion_ambos(estado, ocupacion):
    ocup_ambos = Data_Sec[(Data_Sec['Estado']== estado) &(Data_Sec['Ocupacion']== ocupacion)]
    ocup_ambos = ocup_ambos[['Año','Sexo', 'Personal', 'Salario Mensual']]
    fig6 = px.bar(ocup_ambos, x="Año", y="Personal", color='Sexo', title='Comportamiento de Población Act. por Ocupaciones de TI', barmode= 'group')
    return fig6

#7
def distr_edad_personal(año, ocup):
    dist = Data_Sec[(Data_Sec['Año']== año) & (Data_Sec['Ocupacion']== ocup)]
    dist = dist[['Edad', 'Sexo', 'Personal']]
    fig7 = px.scatter(dist, x='Edad', y='Personal', color='Sexo', title='Dist. Edades en Población Act. por Ocupaciones de TI')
    return fig7




#9
def graffig(año, estado):
    filt = Data_Sec[(Data_Sec['Año']== año)&(Data_Sec['Estado']== estado)]
    filt = filt[[ 'Edad','Ocupacion','Sexo', 'Personal', 'Salario Mensual']]
    fig9 = px.scatter(filt, x="Edad", y="Personal", size="Salario Mensual", color="Ocupacion",
                 hover_name="Sexo", size_max=60, title='Población activa en las diferentes ocupaciones laborales.')
    return fig9

#10
mapa= Data_Sec[(Data_Sec['Sexo']== 'Mujer')]
mapa = mapa.groupby(['Estado']).agg({'Personal': sum})
mapa.reset_index(inplace=True)
def mayus(string):
    return string.title()

mapa['Estado'] = mapa['Estado'].apply(mayus)

def edo(string):
    if string == 'Ciudad De Mexico':
        return 'Ciudad De Mexico'
    if string == 'Coahuila De Zaragoza':
        return 'Coahuila'
    if string == 'Michoacan De Ocampo':
        return 'Michoacán'
    if string == 'Veracruz De Ignacio De La Llave':
        return 'Veracruz'
    if string == 'Nuevo Leon':
        return 'Nuevo León'
    if string == 'Queretaro':
        return 'Querétaro'
    if string == 'San Luis Potosi':
        return 'San Luis Potosí'
    if string == 'Yucatan':
        return 'Yucatán'
    return string

mapa['Estado'] = mapa['Estado'].apply(edo)

repo_url = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json' #Archivo GeoJSON
mx_regions_geo = requests.get(repo_url).json()

fig10 = px.choropleth(data_frame=mapa, 
                    geojson=mx_regions_geo, 
                    locations='Estado', # nombre de la columna del Dataframe
                    featureidkey='properties.name',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
                    color='Personal', #El color depende de las cantidades
                    color_continuous_scale="burg", #greens
                    #scope="north america"
                   )
fig10.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")


fig10.update_layout(
    title_text = 'Poblacion Activa Mujeres en México',
    font=dict(
        family="arial",
        size=20,
        color="#34495E"
    ))