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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
        style={'font-family': 'Arial', 'font-size': '150%'},
        #, '-webkit-box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)','-moz-box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)','box-shadow': '0px 5px 9px 0px rgba(250,128,114,1)', 'margin-bottom': '2rem'},
        children=[

            dcc.Tab(
                label='Educación',
                selected_style={'background-color': colors['actived_nav'],'color':colors['text'],'border':'none'},
                style={'background-color': colors['disabled_nav'],'border':'none'},
                children=[

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

                                

                        ]),


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
                               
                    ]),
        dcc.Tab(
            label='Calidad de Vida',
            selected_style={'background-color': colors['actived_nav'],'color':'#FDFEFE','border':'none'},
            style={'background-color': colors['disabled_nav'],'border':'none'},
            children=[
            # html.H3(
            #     style={'textAlign': 'center'},
            #     children='Estatus socioeconómico por grado acádemico'),
            # html.Div(
            #     style={'flex': '0 0 calc( 50% - 1rem )'},
            #     children=[
            #     html.Label('Rango de edad'),
            #     dcc.Dropdown(
            #     id = 'range_age_dd',
            #     options= [{'label': i, 'value': i} for i in df_sac['Age Range'].unique()],
            #     value='30 to 34 years')
            #             ]),
            #     dcc.Graph(
            #         id='status_edu',
            #         figure={})
                    ]),

    dcc.Tab(
        label='Propuesta',
        selected_style={'background-color': colors['actived_nav'],'color':'#FDFEFE','border':'none'},
        style={'background-color': colors['disabled_nav'],'border':'none'},
        children=[
         ])
#------------------------------------------------------------------------------------
#2
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
    Output('nc_support', 'figure'),
    Input('ncs_edad', 'value'))

def near_cs(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Female')]
    fig11 = px.pie(dff, values='Population', names='Near Children Support', title=f"Acceso a apoyos infantiles para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    #fig11.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig11

@app.callback(
    Output('nd_support', 'figure'),
    Input('nds_edad', 'value'))

def near_ds(age_range):
    dff=df_ns[(df_ns['Age Range']== age_range)&(df_ns['Sex']=='Female')]
    fig12 = px.pie(dff, values='Population', names='Near Doctor Support', title=f"Acceso a apoyos médicos para mujeres de entre {age_range.split()[0]} y {age_range.split()[-2]} años")
    #fig12.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'],title={'x':0.5,'xanchor': 'center'})
    return fig12
#_________________________________________________________________________________________
if __name__ == '__main__':
    app.run_server(debug=True)
