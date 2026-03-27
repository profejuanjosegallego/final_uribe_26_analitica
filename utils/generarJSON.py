import pandas as pd
import os

def generar_archivo_json(listaVentas,nombreArchivo):
    dataFramePanda=pd.DataFrame(listaVentas)
    dataFramePanda.to_json(nombreArchivo,orient="records",indent=4)
    print("Se crea el archivo json con exito!!") 