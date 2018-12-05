from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import components
from os.path import dirname, join
from bokeh.layouts import layout, widgetbox
from bokeh.models import ColumnDataSource, Div
from bokeh.models.widgets import Slider, Select, TextInput
from bokeh.io import curdoc
from bokeh.core.properties import value
from bokeh.transform import dodge, cumsum
from bokeh.palettes import Category20c
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.sampledata.iris import flowers
from math import pi
import numpy as np
import pandas as pd
#Create your views here.



def index(request):
    return render(request,"index.html")

def ModeloNegocio(request):
    return render(request,"ModeloNegocio.html")

def Consulta(request):
    return render(request,"Consulta.html")

def Dashboard(request):

#figura1
    # Declaramos una variable que se llama datos y hacemos el llamado del archivo csv
    datos=pd.read_csv("/home/jacosta/Escritorio/ProyectoDiplomado/aplicacion1/ESTADISTICAS_EN_EDUCACION_BASICA_POR_MUNICIPIO.csv",header=0)
    # utilizamos el groupby para sumos los datos de las columnas
    g = datos.groupby('ANO')["DESERCION"].sum()
    x = [i for i in range(2011,2018,1)]
    y = [g[anio] for anio in x]

    # Creamos un nuevo gráfico con un titulo y dos ejes (x e y)
    plot = figure(plot_height=350,plot_width=405, x_axis_label='Año', y_axis_label='Desercion')

    # Agregamos la linea con los datos
    plot.line(x,y, legend="f(x)", line_width=2)

    # Se declaran los componentes con los que van hacer llamados en el html
    script, div = components(plot,CDN)

 #figura2
    # Preparamos los datos


    datos1=pd.read_csv("/home/jacosta/Escritorio/ProyectoDiplomado/aplicacion1/PISA.csv",header=0)
    materias=(datos1['Clasificacion'])
    anios=(datos1['ano'])
    resultado=(datos1['resultado'])
    materias1=np.asarray(materias)
    materias2=sorted(list(set(materias1)))
    anios1=np.asarray(anios)
    anios2=sorted(list(set(anios)))
    resultado1=np.asarray(resultado)
    #print (materias2)
    #print (anios2)
    #print (resultado1[0])

    years = ['2006', '2009', '2012', '2015']

    data = {'fruits' : materias2,
            2006   : [resultado1[0], resultado1[4], resultado1[8]],
            2009   : [resultado1[1], resultado1[5], resultado1[9]],
            2012   : [resultado1[2], resultado1[6], resultado1[10]],
        2015   : [resultado1[3], resultado1[7], resultado1[11]]}

    palette = ["#c9d9d3", "#718dbf", "#e84d60"]

    # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
    x = [ (fruit, year) for fruit in materias2 for year in years ]
    counts = sum(zip(data[2006], data[2009], data[2012], data[2015]), ()) # like an hstack

    source = ColumnDataSource(data=dict(x=x, counts=counts))

    plot = figure(x_range=FactorRange(*x),plot_height=345,plot_width=405,
            toolbar_location=None, tools="")

    plot.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
        fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))

    plot.line(x=["Ciencias", "Lectura", "Matematicas"], y=[388, 413, 403, 425], color="black", line_width=2)

    plot.y_range.start = 0
    plot.x_range.range_padding = 0.1
    plot.xaxis.major_label_orientation = 1
    plot.xgrid.grid_line_color = None

        # Se declaran los componentes con los que van hacer llamados en el html
    script2, div2 = components(plot,CDN)
#figura3
    # Preparamos los datos

    datos3=pd.read_csv("/home/jacosta/Escritorio/ProyectoDiplomado/aplicacion1/Graduados.csv",header=0)
    Continente=(datos3['Continente'])
    Cantidad_Graduados=(datos3['Cantidad_Graduados'])
    g = datos3.groupby('Continente')["Cantidad_Graduados"].sum()
    g1=np.asarray(g)
    #print(g1)
    x = {
    'Africa': g1[0],
    'America': g1[1],
    'Asia': g1[2],
    'Europa': g1[3],
    'Oceania': g1[4]
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=450, plot_width=405, toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None


    script3, div3 = components(p,CDN)
#figura4
    # Preparamos los datos

    datos4=pd.read_csv("/home/jacosta/Escritorio/ProyectoDiplomado/aplicacion1/PIB.csv",header=0)

    PIB_Educacion=(datos4['PIB_Educacion'])
    Graduados_Universidad=(datos4['Graduados_Universidad'])
  
    pib=np.asarray(PIB_Educacion)
    graduados=np.asarray(Graduados_Universidad)
   
    p = figure(plot_height=440,plot_width=405)
    p.circle(pib,graduados, size=5, color="navy", alpha=0.5)

    script4, div4 = components(p,CDN)
#figura5
    # Declaramos una variable que se llama datos y hacemos el llamado del archivo csv
    datos=pd.read_csv("/home/jacosta/Escritorio/ProyectoDiplomado/aplicacion1/ESTADISTICAS_EN_EDUCACION_BASICA_POR_MUNICIPIO.csv",header=0)
    # utilizamos el groupby para sumos los datos de las columnas
    g = datos.groupby('ANO')["POBLACION_5_16"].sum()
    x = [i for i in range(2011,2018,1)]
    y = [g[anio] for anio in x]

    # Creamos un nuevo gráfico con un titulo y dos ejes (x e y)
    plot = figure(plot_height=350,plot_width=405,x_axis_label='Año', y_axis_label='Analfabetismo')

    # Agregamos la linea con los datos
    plot.line(x,y, legend="f(x)", line_width=2)

    # Se declaran los componentes con los que van hacer llamados en el html
    script5, div5 = components(plot,CDN)



    return render(request,"Dashboard.html",{"script":script,"div":div,"script2":script2,"div2":div2,"script3":script3,"div3":div3,"script4":script4,"div4":div4,"script5":script5,"div5":div5})

