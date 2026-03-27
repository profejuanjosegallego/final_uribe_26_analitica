import pandas as pd 
import os

def generar_archivo_csv(listaVentas,nombreArchivo):
    dataFramePanda=pd.DataFrame(listaVentas)
    dataFramePanda.to_csv(nombreArchivo,index=False, encoding="utf-8")
    print("Archivo CSV generado correctamente")