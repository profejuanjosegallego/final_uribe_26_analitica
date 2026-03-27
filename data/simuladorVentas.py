#Construir una funcion generadora de N ventas que permita crear MOCKS o datos semilla para la rutina de analisis
import random
from datetime import datetime,timedelta

def generar_ventas(numeroVentas):
    
    #Simular una lista de productos
    #Leer un excel y cargar esta lista con la info del excel
    #Consumir API
    productos=[
        {"nombre":"Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón","precio":150000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Classic Fit Cuello Nerú Manga Corta Textura Piqué Jacquard en Algodón","precio":200000,"descuento":False},
        {"nombre":"Camisa Polo de Hombre Slim Fit Cuello Nerú Manga Corta Sesgos en Contraste en Mezcla de Algodón","precio":110000,"descuento":True},
        {"nombre":"Camisa Polo de Hombre Classic Fit Manga Larga Varsity con Cierre Efecto Desgaste en Algodón","precio":205000,"descuento":False},
        {"nombre":"Camiseta Polo M/C","precio":98000,"descuento":False},
        {"nombre":"Jean de Hombre Skinny Fit Tiro Medio Lavado Oscuro Clásico con Raspones en Mezcla de Algodón Famous","precio":490000,"descuento":False},
        {"nombre":"Jean de Hombre Rider Skinny Fit Tiro Bajo Lavado Medio Rotos Detalles en Costuras en Mezcla de Algodón","precio":357000,"descuento":True},
        {"nombre":"Chaqueta de Hombre Bomber Acolchada Rombos y Gráficos Bordados en Mezcla de Algodón y Poliéster","precio":1500000,"descuento":False},
        {"nombre":"Chaqueta de Hombre Doble Faz Cuello Alto Windbreaker Bolsillo Canguro en Mezcla de Algodón y Poliéster","precio":680000,"descuento":False},
        {"nombre":"Chaqueta Tipo Trucker en Denim para Hombre","precio":820000,"descuento":False}
    ]

    #Simular una lista de tallas
    tallas=["XS","S","M","L","XL","XXL","XXXL"]

    
    #simular vendor asociado

    # *****************
    vendedores=["Pablo Serna","Angie Saldarriaga","Harold Mejia","Alderney Ramirez","Brahian Lopera","Jessica Mora","Daniel Arias","Kevin Villegas"]

    #simula la fecha
    fechaInicio=datetime(2026,1,2)

    #generar la N ventas que me esten pidiendo
    ventas=[]
    for _ in range(numeroVentas):
        producto=random.choice(productos) #como hago para agregar mas de un producto a la simulacion?
        cantidad=random.randint(1,5)
        fecha=fechaInicio+timedelta(days=random.randint(0,60))

        venta={
            "producto":producto["nombre"],
            "precioUnitario":producto["precio"],
            "talla":random.choice(tallas),
            "cantidad":cantidad,
            "vendedor":random.choice(vendedores),
            "fecha": fecha.strftime("%Y-%m-%d"),   
            "total":cantidad*producto["precio"]
        }


        #Inyectando errores de calidad en los datos
        probabilidadError=random.random()

        
        if probabilidadError<0.15:
            venta["producto"]=" "+venta["producto"]+" "
        elif probabilidadError<0.30:
            venta["vendedor"]=venta["vendedor"].upper()
        elif probabilidadError<0.40:
            venta["talla"]="medio"
        elif probabilidadError<0.50:
            venta["cantidad"]=random.choice([0,-1,None])
        elif probabilidadError<0.60:
            venta["precioUnitario"]=None
        elif probabilidadError<0.70:
            venta["fecha"]=fecha.strftime("%d/%m/Y")
        elif probabilidadError<0.8:
            venta["total"]=random.randint(1000,5000)
        elif probabilidadError<0.9:
            venta["producto"]=venta["producto"].lower()

        ventas.append(venta) #Inyectando la venta (con errores) a la lista de ventas
        
        #Inyectar Duplicados

    if len(ventas)>=50:
        ventas.append(ventas[0].copy())
        ventas.append(ventas[1].copy())



    return ventas
