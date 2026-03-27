import pandas as pd
from data.simuladorVentas import generar_ventas

#Tranformando datos en funcion de decisiones utiles para el negocio

#PANDAS ==> QUERIES (Condiciones logicas que permiten extraer informacion de un set datos)
datos=generar_ventas(50) #OJO estos datos estan sucios
datosOrdenados=pd.DataFrame(datos)

#1. QUERY SIMPLES 
#averiguar cuales son las ventas superiores a 500.000 pesos
ventas_mayores_500=datosOrdenados.query("total > 500000").head(5)

#2. QUERIES CON DOS CONDICIONES
#FILTRAR filas donde el total sea mayor a 300000 y la talla sea M
ventas_300_tallaM=datosOrdenados.query("total >300000 and talla == 'M' ")

#3. QUERIES CON VALORES ESPECIFICOS DE UNA COLUMNA
#Me gustaria evr las ventas de Pablo Serna o de Angie Saldarriaga
ventas_vendedores_serna_saldarriaga=datosOrdenados.query("vendedor == 'Pablo Serna' or vendedor == 'Angie Saldarriaga'")


#4. OTRAS QUERIES DEPENDIENDO DEL NEGOCIO QUE ESTOY ANALIZANDO

#Filtras las filas cuyo valor en la columna mes sea igua a 2, Recuperar las ventas de febrero

#Analizando(Transformando) FECHAS CON PANDAS
datosOrdenados["fecha"]=pd.to_datetime(datosOrdenados["fecha"],errors="coerce",dayfirst=False)
datosOrdenados["mes"]=datosOrdenados["fecha"].dt.month
#datosOrdenados["dia"]=datosOrdenados["fecha"].dt.day
#datosOrdenados["nombreDia"]=datosOrdenados["fecha"].dt.day_name()
#datosOrdenados["año"]=datosOrdenados["fecha"].dt.year
ventas_febrero=datosOrdenados.query("mes == 2")

#Queries usando variables externas
vendedor_buscado="Kevin Villegas"
ventas_kevin_villegas=datosOrdenados.query("vendedor == @vendedor_buscado")

#AGRUPANDO DATOS CON PYTHON Y PANDAS (REUNIR DOS O MAS COLUMNAS PARA EXTRAER INFORMACION)

#1. Agrupaciones simples
#aGRUPAR TODAS las filas que tengan el mismo vendedor
ventas_agrupadas=datosOrdenados.groupby("vendedor")["total"].sum().sort_values(ascending=False)

#Agrupar y mostrar ventas por talla
ventas_talla=datosOrdenados.groupby("talla")["total"].sum().sort_values(ascending=False)
print(ventas_talla)


