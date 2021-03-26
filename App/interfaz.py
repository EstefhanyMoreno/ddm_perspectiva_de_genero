# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import Info

df_sac= pd.read_csv('../factores_calidad_vida/ss_edu_per.csv')
df_ns= pd.read_csv('../factores_calidad_vida/Near Children Support-Near Doctor Support-Near Work Support-Near Money Support-Age Range-Sex.csv')
df_f15= pd.read_csv('../factores_calidad_vida/Female Population Older 15 With Children-Schooling Years Range-Job Situation.csv')
df_sec= pd.read_csv('../factores_calidad_vida/City Perception at Home-City Perception at Work-City Perception Streets-City Perception at Public Transport-Age Range-Sex.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors = {
#     'background': '#F9EBEA',
#     'text': '#34495E',
#     'actived_nav':'#FA8072',
#     'disabled_nav':'#FADBD8',
#     'footer': '#212F3D'
# }

colors = {
    'background': '#E0D9F5',
    'text': '#484554',
    'actived_nav':'#70A1EE',
    'disabled_nav':'#9282EC',
    'footer': '#BEE5D9'
}

Info.fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
Info.fig1.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
Info.fig10.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})


app.layout = html.Div(style={'backgroundColor': colors['background'],'width': 'min(95%, 1200px)','margin': '0 auto'}, children=[

    html.Div(
        style={'background-image': 'url(assets/generologo.png)', 'background-size': 'cover', 'background-repeat': 'no-repeat', 'background-position': 'center center','textAlign': 'center', 'color': '#494454' },
        children=[
                html.H1(
                    style={'textAlign': 'center','font-weight': '700','padding': '5rem', 'margin':'0'},
                    children='Información sobre la Mujer en México'
                )

            
        ]
    ),

    dcc.Tabs(
        style={'font-family': 'Arial', 'font-size': '150%', '-webkit-box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)','-moz-box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)','box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)', 'margin-bottom': '2rem'},
        children=[
        dcc.Tab(
                label='Calidad de Vida',
                selected_style={'background-color': colors['actived_nav'],'color':'#FDFEFE','border':'none'},
                style={'background-color': colors['disabled_nav'],'border':'none'},
                children=[
                html.H3(
                    style={'textAlign': 'center'},
                            children='Estatus socioeconómico por grado acádemico'
                    ),
                html.Div(
                    style={'flex': '0 0 calc( 50% - 1rem )'},
                    children=[
                    html.Label('Rango de edad'),
                    dcc.Dropdown(
                    id = 'range_age_dd',
                    options= [{'label': i, 'value': i} for i in df_sac['Age Range'].unique()],
                    value='30 to 34 years')
                        ]),
                html.Div(
                style={'flex': '0 0 calc( 50% - 1rem )'},
                children=[
                html.Label('Grado Acádemico'),
                dcc.Dropdown(
                    id = 'academic_dd',
                    options= [{'label': i, 'value': i} for i in df_sac['Academic Degree'].unique()],
                    value='Master Degree'),
                dcc.Graph(
                    id='status_edu',
                            figure={})
                ]),
                html.H3(
                            style={'textAlign': 'center'},
                            children='Acceso a apoyos'),
                html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'ncs_dd',
                                options= [{'label': i, 'value': i} for i in df_ns['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='nc_s',
                                    figure={}
                                )
                                ]),
                                
                                html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'nds_dd',
                                options= [{'label': i, 'value': i} for i in df_ns['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='nd_s',
                                    figure={}
                                )

                        ])
                        ]),
                html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'nws_dd',
                                options= [{'label': i, 'value': i} for i in df_ns['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='nw_s',
                                    figure={}
                                )
                                ]),
                                
                                html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'nms_dd',
                                options= [{'label': i, 'value': i} for i in df_ns['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='nm_s',
                                    figure={}
                                )

                        ])
                        ]), #Cierra div general 2 y 2
                html.H3(
                    style={'textAlign': 'center'},
                            children='Estatus laboral de mujeres mayores a 15 años con hijos por años de estudio'
                    ),
                html.Div(
                    style={'flex': '0 0 calc( 50% - 1rem )'},
                    children=[
                    html.Label('Años de estudio'),
                    dcc.Dropdown(
                    id = 'sy_dd',
                    options= [{'label': i, 'value': i} for i in df_f15['Schooling Years Range'].unique()],
                    value='0 a 3 Años de Escolaridad'),
                    dcc.Graph(
                        id='f15_g',
                        figure={}
                        )
                        ]),

                html.H3(
                            style={'textAlign': 'center'},
                            children='Percepción de Seguridad en la Ciudad'
                    ),
                html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'sh_dd',
                                options= [{'label': i, 'value': i} for i in df_sec['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='sh_g',
                                    figure={}
                                )
                                ]),
                                
                                html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'sw_dd',
                                options= [{'label': i, 'value': i} for i in df_sec['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='sw_g',
                                    figure={}
                                )

                        ])
                        ]),
                html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'ss_dd',
                                options= [{'label': i, 'value': i} for i in df_sec['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='ss_g',
                                    figure={}
                                )
                                ]),
                                
                                html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.Label('Rango de Edad'),
                                dcc.Dropdown(
                                id = 'st_dd',
                                options= [{'label': i, 'value': i} for i in df_sec['Age Range'].unique()],
                                value='45 to 49 years'),
                                dcc.Graph(style={'height': '40rem'},
                                    id='st_g',
                                    figure={}
                                )

                        ])
                        ]), #Cierra div general 2 y 2
               
                ]),

            dcc.Tab(
                label='Educación',
                selected_style={'background-color': colors['actived_nav'],'color':'#FDFEFE','border':'none'},
                style={'background-color': colors['disabled_nav'],'border':'none'},
                children=[
                    html.H3(
                                style={'textAlign': 'center'},
                                children='Aréa de Estudios por Género'
                                ),
                            html.Div(style={'margin-left': '2rem', 'width': '40%' },children=[
                                html.Div(
                                    style={'display': 'flex', 'justify-content': 'space-between'},
                                    children=[
                                        html.Div(
                                            style={'flex': '0 0 calc( 50% - 1rem )'},
                                            children=[
                                                html.Label('Año'),
                                                dcc.Dropdown(
                                                    id = 'edu_area_per_año',
                                                    options= [{'label': i, 'value': i} for i in Info.edo['Year'].unique()],
                                                    value=2020,
                                                    )

                                            ]),


                                ]),
                            
                            ]),

                            dcc.Graph(
                            id='educacion_grf',
                            figure={}
                            ),
                            

                            html.H3(
                                style={'textAlign': 'center'},
                                children='Mujeres y Hombres por grado de estudio'
                                ),
                            html.Div(style={'margin-left': '2rem', 'width': '40%' },children=[
                                html.Div(
                                    style={'display': 'flex', 'justify-content': 'space-between'},
                                    children=[
                                        html.Div(
                                            style={'flex': '0 0 calc( 50% - 1rem )'},
                                            children=[
                                                html.Label('Grado Acádemico'),
                                                dcc.Dropdown(
                                                    id = 'Grado_drop',
                                                    options= [{'label': i, 'value': i} for i in Info.df2['Grado'].unique()],
                                                    value='Primaria',
                                                    )

                                            ]),


                                ]),
                            
                            ]),
            
                            dcc.Graph(
                                    id='Grado_grf',
                                    figure={}
                                ),

                            html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                        children='Status de estudios universitarios'
                                    ),
                                html.Div(style={'margin': '0 auto','width':'90%'},children=[
                                    html.Label('Año'),
                                    dcc.Dropdown(
                                        id = 'status_gen_escolar_año',
                                        options= [{'label': i, 'value': i} for i in Info.edo['Year'].unique()],
                                        value=2020,
                                        )
                                ]),

                                dcc.Graph(
                                    id='status_gen_escolar_grf',
                                    figure={}
                                    )
                            ]),

                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                    children='Composición del dataframe'
                                ),
                                html.Div(style={'margin': '0 auto','width':'90%'},children=[
                                    html.Label('Año'),
                                    dcc.Dropdown(
                                        id = 'edu_confor_per_año',
                                        options= [{'label': i, 'value': i} for i in Info.edo['Year'].unique()],
                                        value=2020,
                                        )
                                ]),

                                dcc.Graph(
                                    id='edu_confor_grf',
                                    figure={}
                                    )
                            ])
                        ])

                            

                ]),    
                        
#-------------------------------------------------------------------------------------
            dcc.Tab(
                label='Empleo',
                selected_style={'background-color': colors['actived_nav'],'color':'#FDFEFE','border':'none'},
                style={'background-color': colors['disabled_nav'],'border':'none'},
                        children=[
                            html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                        children='Diferencia Laboral'
                                    ),
                                dcc.Graph(style={'height': '40rem'},
                                    id='fig_pob_total',
                                    figure=Info.fig
                                ),

                                ]),
                                
                                html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                    children='Diferencia Salarial'
                                ),
                                dcc.Graph(style={'height': '40rem'},
                                    id='fig_pob_total_sal',
                                    figure=Info.fig1
                                

                            )

                            ])

                                

                        ]), #Cierra Div


                        html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                        children='Ocupación Laboral'
                                    ),
                                html.Div(style={'margin': '0 auto','width':'90%'},children=[
                                    html.Label('Clasificación de trabajos'),
                                    dcc.Dropdown(
                                        id = 'pob_total_atv_clas_dopdown',
                                        options= [{'label': i, 'value': i} for i in Info.Data_Worker_Act['Clasificación de trabajos'].unique()],
                                        value='Empleo Formal',
                                        )
                                ]),

                                dcc.Graph(
                                    id='pob_total_atv_clas',
                                    figure={}
                                    )
                            ]),

                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                    children='Salario'
                                ),
                                html.Div(style={'margin': '0 auto','width':'90%'},children=[
                                    html.Label('Clasificación de trabajos'),
                                    dcc.Dropdown(
                                        id = 'sal_pob_total_atv_clas_dopdown',
                                        options= [{'label': i, 'value': i} for i in Info.Data_Worker_Act['Clasificación de trabajos'].unique()],
                                        value='Empleo Formal',
                                        )
                                ]),

                                dcc.Graph(
                                    id='sal_pob_total_atv_clas',
                                    figure={}
                                    )
                            ])
                        ]),



                        html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                        children='Ocupación en el Sector Tecnológico'
                                    ),
                                html.Div(
                                    style={'display': 'flex', 'justify-content': 'space-between'},
                                    children=[
                                        html.Div(
                                            style={'flex': '0 0 calc( 30% - 1rem )'},
                                            children=[
                                                html.Label('Estado'),
                                                dcc.Dropdown(
                                                    id = 'com_pob_act_dropdown_est',
                                                    options= [{'label': i, 'value': i} for i in Info.Data_Sec['Estado'].unique()],
                                                    value='mexico',
                                                    )

                                            ]),
                                        html.Div(
                                            style={'flex': '0 0 calc( 70% - 1rem )'},
                                            children=[
                                                html.Label('Ocupacion'),
                                                dcc.Dropdown(
                                                    id = 'com_pob_act_dropdown_ocu',
                                                    options= [{'label': i, 'value': i} for i in Info.Data_Sec['Ocupacion'].unique()],
                                                    value='Coordinadores y Jefes de Área en Informática',
                                                    )
                                            ]),


                                ]),
                                
                                dcc.Graph(
                                    id='ocup_ambos_graf',
                                    figure={}
                                ),

                                html.P(
                                    children='   Se puede observar que, aunque estas ocupaciones se encuentren dentro del sector servicios profesionales, científicos y técnicos; en ellas existe una brecha muy marcada en cuanto a la ocupación por género. También podemos notar como la pandemia influyo en estas ocupaciones laborales.'
                                )

                            ]),

                            html.Div(
                                style={'flex': '0 0 calc( 50% - 1rem )'},
                                children=[
                                html.H3(
                                    style={'textAlign': 'center'},
                                    children='Distribución en el Sector Tecnológico'
                                ),

                                html.Div(
                                    style={'display': 'flex', 'justify-content': 'space-between'},
                                    children=[
                                        html.Div(
                                            style={'flex': '0 0 calc( 30% - 1rem )'},
                                            children=[
                                                html.Label('Año'),
                                                dcc.Dropdown(
                                                    id = 'des_anlsoft_drop_año',
                                                    options= [{'label': i, 'value': i} for i in Info.Data_Sec['Año'].unique()],
                                                    value=2020
                                                    )

                                            ]),
                                        html.Div(
                                            style={'flex': '0 0 calc( 70% - 1rem )'},
                                            children=[
                                                html.Label('Ocupacion'),
                                                dcc.Dropdown(
                                                    id = 'des_anlsoft_drop_ocu',
                                                    options= [{'label': i, 'value': i} for i in Info.Data_Sec['Ocupacion'].unique()],
                                                    value='Coordinadores y Jefes de Área en Informática',
                                                    )
                                            ]),


                                ]),
                                
                                dcc.Graph(
                                    id='distr_edad_personal_graf',
                                    figure={}
                                ),


                                

                            ])

                        ]),

                        html.H3(
                            style={'textAlign': 'center'},
                            children='Densidad Laboral de la Población por Edades'
                        ),
                        html.Div(style={'margin-left': '2rem', 'margin-top':'5rem', 'width': '40%' },children=[
                            html.Div(
                            style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                                html.Div(
                                    style={'flex': '0 0 calc( 50% - 1rem )'},
                                    children=[
                                        html.Label('Año'),
                                        dcc.Dropdown(
                                            id = 'sal_ed_ocu_sex_per_año',
                                            options= [{'label': i, 'value': i} for i in Info.Data_Sec['Año'].unique()],
                                            value=2020,
                                        )
                                    ]),
                                html.Div(
                                    style={'flex': '0 0 calc( 50% - 1rem )'},
                                    children=[
                                        html.Label('Estado'),
                                        dcc.Dropdown(
                                            id = 'sal_ed_ocu_sex_per_edo',
                                            options= [{'label': i, 'value': i} for i in Info.Data_Sec['Estado'].unique()],
                                            value='mexico',
                                            )
                                    ])
                            ]),
                        ]),


                        dcc.Graph(
                            id='sal_ed_ocu_sex_per_grf',
                            figure={}
                            ),
                        html.Div(
                            children=[

                                
                                dcc.Graph(
                                    id='graf_map_mex',
                                    figure=Info.fig10
                                    ) 

                                ])
                               
                    ])




                 #Cierra tab
                

       ])])




#2
#___________________________________________________________________________________________________
@app.callback(
    Output('pob_total_atv_clas', 'figure'),
    Input('pob_total_atv_clas_dopdown','value'))

def clas_Estado(value):
    fig2 = Info.clas_Estado(value)
    fig2.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})

    return fig2


#4
@app.callback(
    Output('sal_pob_total_atv_clas', 'figure'),
    Input('sal_pob_total_atv_clas_dopdown','value'))

def estado_Salario(value):
    fig4 = Info.estado_Salario(value)
    fig4.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})

    return fig4

#6
@app.callback(
    Output('ocup_ambos_graf', 'figure'),
    Input('com_pob_act_dropdown_est','value'),
    Input('com_pob_act_dropdown_ocu','value'))

def ocupacion_ambos(estado, ocupacion):
    fig6 = Info.ocupacion_ambos(estado, ocupacion)
    fig6.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})

    return fig6

#7
@app.callback(
    Output('distr_edad_personal_graf', 'figure'),
    Input('des_anlsoft_drop_año','value'),
    Input('des_anlsoft_drop_ocu','value'))

def distr_edad_personal(año, ocup):
    fig7 = Info.distr_edad_personal(año, ocup)
    fig7.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig7

#9 sal_ed_ocu_sex_per_grf
@app.callback(
    Output('sal_ed_ocu_sex_per_grf', 'figure'),
    Input('sal_ed_ocu_sex_per_año','value'),
    Input('sal_ed_ocu_sex_per_edo','value'))

def graffig(año, estado):
    fig9 = Info.graffig(año, estado)
    fig9.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig9

@app.callback(
    Output('status_edu', 'figure'),
    Input('range_age_dd', 'value'),
    Input('academic_dd', 'value'))

def grafica_rango_edad(age_range, academic_degree):
    dff=df_sac[(df_sac['Age Range']==age_range)&(df_sac['Academic Degree']==academic_degree)]
    fig10 = px.bar(dff, x='Socioeconomic Status', y='Population', color='Sex',barmode='group')
    fig10.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig10

@app.callback(
    Output('nc_s', 'figure'),
    Input('ncs_dd', 'value'))

def near_cs(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Mujer')]
    fig11 = px.pie(dff, values='Population', names='Near Children Support', title=f"Acceso a apoyos infántiles para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig11.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig11

@app.callback(
    Output('nd_s', 'figure'),
    Input('nds_dd', 'value'))

def near_ds(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Mujer')]
    fig12 = px.pie(dff, values='Population', names='Near Doctor Support', title=f"Acceso a apoyos médicos para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig12.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig12

@app.callback(
    Output('nw_s', 'figure'),
    Input('nws_dd', 'value'))

def near_ws(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='Near Work Support', title=f"Acceso a apoyos laborales para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('nm_s', 'figure'),
    Input('nms_dd', 'value'))

def near_ms(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='Near Money Support', title=f"Acceso a apoyos monetarios para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('f15_g', 'figure'),
    Input('sy_dd', 'value'))

def child_school(s_years):
    dff= df_f15[df_f15['Schooling Years Range']==s_years]
    fig = px.bar(dff, y='Workforce', x='Female Population Older 15 With Children', color='Job Situation', barmode='group')
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('sh_g', 'figure'),
    Input('sh_dd', 'value'))

def seg_home(age_range):
    dff=df_sec[(df_sec['Age Range']== age_range)&(df_sec['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='City Perception at Home', title=f"Desde de casa para mujeres entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('sw_g', 'figure'),
    Input('sw_dd', 'value'))

def seg_work(age_range):
    dff=df_sec[(df_sec['Age Range']== age_range)&(df_sec['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='City Perception at Work', title=f"Desde el trabajo para mujeres entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('ss_g', 'figure'),
    Input('ss_dd', 'value'))

def seg_streets(age_range):
    dff=df_sec[(df_sec['Age Range']== age_range)&(df_sec['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='City Perception Streets', title=f"En las calles para mujeres entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

@app.callback(
    Output('st_g', 'figure'),
    Input('st_dd', 'value'))

def seg_trans(age_range):
    dff=df_sec[(df_sec['Age Range']== age_range)&(df_sec['Sex']=='Mujer')]
    fig = px.pie(dff, values='Population', names='City Perception at Public Transport', title=f"Desde el transporte público para mujeres entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig

#20 educacion_grf
@app.callback(
    Output('educacion_grf', 'figure'),
    Input('edu_area_per_año','value'))

def area_genero(año):
    fig20 = Info.area_genero(año)
    fig20.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig20

#22 status_gen_escolar
@app.callback(
    Output('status_gen_escolar_grf', 'figure'),
    Input('status_gen_escolar_año','value'))

def status_gen_escolar(año):
    fig21 = Info.status_gen_escolar(año)
    fig21.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig21

#21 educacion
@app.callback(
    Output('edu_confor_grf', 'figure'),
    Input('edu_confor_per_año','value'))

def conformacion(año):
    fig22 = Info.conformacion(año)
    fig22.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig22


#23 Grado
@app.callback(
    Output('Grado_grf', 'figure'),
    Input('Grado_drop','value'))

def Grado(value):
    fig23 = Info.Grado(value)
    fig23.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig23
#________________________________________________________________________________________________________
if __name__ == '__main__':
    app.run_server(debug=True)
