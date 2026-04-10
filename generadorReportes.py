import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from transformaciones import (

    datosOrdenados,
    ventas_mayores_500,
    ventas_300_tallaM,
    ventas_vendedores_serna_saldarriaga,
    ventas_febrero,
    ventas_kevin_villegas,
    ventas_agrupadas,
    ventas_talla


)

#Peparar el espacio donde voy a guardar los reportes grafica
CARPETA_REPORTES="reportes"
CARPETA_GRAFICAS=os.path.join(CARPETA_REPORTES,"graficas")
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

#Crear el reporte de los datos, un reporte estara conformado por un docuemnto HTML que carga graficas
## Crear un html
## Crear imagenes
def dataFrame_convertir_html(dataFrame):

    if isinstance(dataFrame, pd.Series):
        dataFrame=dataFrame.reset_index()
    
    return dataFrame.to_html(
        classes="table table-striped table-hover table-bordered table-sm",
        border=0
    )


##Primera grafica (graficar el comportamiento del filtro ) GRAFICANDO AGRUPACIONES
plt.figure(figsize=(15,8))
ventas_agrupadas.plot(kind="bar", color="#264D25")
plt.title("Total de ventas por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Total vendido en pesos")
plt.xticks(rotation=45)
plt.savefig(os.path.join(CARPETA_GRAFICAS,"ventas_por_vendedor.png"))
plt.close()

##Segunda Grafica (Grafica del total de venats por talla)
plt.figure(figsize=(10,5))
ventas_talla.plot(kind="bar", color="#39254D")
plt.title("Total de ventas por talla")
plt.xlabel("Talla")
plt.ylabel("Total vendido en pesos")
plt.savefig(os.path.join(CARPETA_GRAFICAS,"ventas_por_talla.png"))
plt.close()

##Tercera grafica (Grafica que muestre el total de ventas por mes)


## Cuarta grafica grafica de tortas (Participacion procentual de cada vendedor en las ventas de la tienda)
colores_torta={
    "#264D25",
    "#39254D",
    "#5C8A2B",
    "#7B0E15",
    "#4AB5D5",
    "#C13B89",
    "#C9E24C",
    "#B2672E",
    "#43F10E",
    "#EEAF80"

}
plt.figure(figsize=(15,15))
ventas_agrupadas.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=colores_torta
)
plt.title("Participacion porcentual de cada vendedor")
plt.savefig(os.path.join(CARPETA_GRAFICAS,"tortas_vendedor.png"))

## RUTINA PARA CREAR UN DOCUEMNTO HTML QUE GUARDE IMAGENES
documento_html=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reportes de analitica</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    </head>
    <body>

        <section class="container">
            <section class="row">
                <section class="col-12">
                    <h1>REPORTE DE DATOS ASOCIADOS A LAS VENTAS</h1>
                    <hr>
                    <p>
                        Utilizando PANDAS este es el reporte de ventas de la tienda chevignion sandiego
                    </p>
                </section>
            </section>
        </section>

        <section class="container">
            <section class="row">
                <section class="col-12">
                    <div class="card p-5 shadow border">

                        <h3>Total vendido  por cada vendedor</h3>
                        <hr>
                        <p>La grafica presenta las ventas de la tienda por vendedor, permitiendo comparar el rendimiento de cada uno de nuestros empleados</p>
                        {dataFrame_convertir_html(ventas_agrupadas)}
                        <br>
                        <img src="graficas/ventas_por_vendedor.png" alt="foto" class="img-fluid">
                        <br>
                        <img src="graficas/tortas_vendedor.png" alt="foto" class="img-fluid">
                        

                    </div>
                </section>
            </section>
        </section>
        
    </body>
    </html>

"""



#RUTINA PARA ALMACENAR EL HTML GENERADO EN LA RAIZ DE NEUSTRO PROYECTO
RUTA_REPORTE=os.path.join(CARPETA_REPORTES,"reporte.html")

with open(RUTA_REPORTE, "w", encoding="utf-8") as archivo:
    archivo.write(documento_html)
