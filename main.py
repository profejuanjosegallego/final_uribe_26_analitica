import pandas as pd
from data.simuladorVentas import generar_ventas
from utils.generarCSV import generar_archivo_csv
from utils.generarJSON import generar_archivo_json


#1. Si voy a comenzar una rutina de analitica con PANDAS lo primero
#que debo hacer es crear un dataframe de los datos

#Como crear un data frame desde una fuente de datos simulados en el mismo python

lista=generar_ventas(10)
datosOrdenados=pd.DataFrame(lista) #Normlamente OJO se le entraga una LISTA

#Generando un dataset en formato CSV
#generar_archivo_csv(lista,"data/ventas_sucias.csv")#

#Generamdo un dataset en formato JSON
#generar_archivo_json(lista,"data/json_ventas.json")

#PASO PARA ANALIZAR ESTE SET DE DATOS
#1. Identificar/inspeccionar/asociar la informacion base de los datos
#print(datosOrdenados.head(7))
#print(datosOrdenados.tail())
#print(datosOrdenados.shape)
#print(datosOrdenados.columns)
#print(datosOrdenados.dtypes)
#print(datosOrdenados.info())
#print(datosOrdenados.describe())


#2. Limpiar / evaluar calidad de los datos
#QUE SE LIMPIA?
#A NOMBRE DE LAS COLUMNAS

#B TEXTOS
# -ESPACIOS
#-MAYUSCULAS/MINUSCULAS
#FORMATOS INCONSISTENTES

#C. VALORES NULOS

#D. VALORES DUPLICADOS

#E. VERIFICAR TIPO DE DATOS

#F. SE VERIFICAN LAS REGLAS DE NEGOCIO

#⏰ CONVERTIR ESTA RUTINA A UNA FUNCION GENERICA
dataFrameCopia=datosOrdenados.copy()

dataFrameCopia.columns=dataFrameCopia.columns.str.strip()
columnas_texto=["producto","talla","vendedor"]
for columna in columnas_texto:
    dataFrameCopia[columna]=dataFrameCopia[columna].astype(str).str.strip()

dataFrameCopia["producto"]=dataFrameCopia["producto"].str.title()
dataFrameCopia["vendedor"]=dataFrameCopia["vendedor"].str.title()
dataFrameCopia["talla"]=dataFrameCopia["talla"].str.upper()

dataFrameCopia.replace(["","None","nan","-"],pd.NA,inplace=True)

dataFrameCopia["precioUnitario"]=pd.to_numeric(dataFrameCopia["precioUnitario"],errors="coerce")
dataFrameCopia["cantidad"]=pd.to_numeric(dataFrameCopia["cantidad"],errors="coerce")
dataFrameCopia["total"]=pd.to_numeric(dataFrameCopia["total"],errors="coerce")

dataFrameCopia["fecha"]=pd.to_datetime(dataFrameCopia["fecha"],errors="coerce",dayfirst=False)

dataFrameCopia=dataFrameCopia.drop_duplicates()

dataFrameCopia=dataFrameCopia.dropna(subset=["producto","precioUnitario","cantidad","fecha"])

#RUTINA PARA LIMPIAR SEGUN LA REGLA DE NEGOCIO
dataFrameCopia=dataFrameCopia[dataFrameCopia["cantidad"]>0]
dataFrameCopia=dataFrameCopia[dataFrameCopia["precioUnitario"]>5000]

tallasValidas=["XS","S","M","L","XL","XXL","XXXL"]
dataFrameCopia=dataFrameCopia[dataFrameCopia["talla"].isin(tallasValidas)]

dataFrameCopia["total"]=dataFrameCopia["cantidad"]*dataFrameCopia["precioUnitario"]


print(datosOrdenados)
print("\n")
print(dataFrameCopia)