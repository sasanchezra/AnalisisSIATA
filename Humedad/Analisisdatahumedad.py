# -*- coding: utf-8 -*-
"""
Spyder Editor
Autor: Santiago Sánchez Ramírez

Este programa genera un histograma de un archivo .csv de la base de datos de los sensores de humedad de Siata,
filtrando por calidad y obteniendo su media y mediana. Con estos dos últimos datos tmbién se realiza un histograma
"""
#A continuación importo las librerías
import glob   #Con esta librería realizo la lectura de todos los archivos dentro de mi directorio
import pandas as pd #Con esta librería manipulo las bases de datos
import matplotlib.pyplot as plot  #Con esta librería grafico
from numpy import median, mean   #Con esta librería manipulo matemáticamento los datos

bases = glob.glob("*.csv")  #En el directorio importo los archvos .csv
listas_medias = []  #Creo la lista donde voy a alojar los valores de las medias
listas_medianas = []     #Creo la lista donde voy a alojar los valores de las medias

#Con este ciclo voy a recorrer cada archivo de bases de datos
for i in range(0, len(bases), 1):  
    lista = pd.read_csv(bases[i], sep=",")  #parametrizo las bases de datos que voy a usar
    df_mask=lista['Calidad']==1 #Creo un filttro para las medidas de buena calidad (Calidad = 1)
    listafiltrada = lista[df_mask]  #Creo una variable nueva para este filtro
    mediana = median(listafiltrada["Humedad"])  #Obtengo la mediana de la columna de humedad de la lista que estoy leyendo
    media = round(mean(listafiltrada["Humedad"]))   #Obtengo la media de la columna de humedad de la lista que estoy leyendo
    print("para la estación ", bases[i], "la media es: ", media, "y la mediana: ", mediana) #Muestro la infromación
    listas_medias.append(media) #Almaceno los datos de las medias de cada base de datos
    listas_medianas.append(mediana) #Almaceno los datos de las medianas de cada base de datos

    plot.hist(x=listafiltrada['Humedad'], bins=100, range=(0,100))  #Realizo el histograma y creo el rango
    plot.xlabel('Humedad')  #Eje coordenado 
    plot.ylabel('Frecuencia') #Eje ordenado
    plot.suptitle(bases[i]) #Muestro el nombre de la base de datos
    plot.text(0, 800, "La mediana es: ")
    plot.text(30, 800, mediana) #Muestro el valor de la mediana
    plot.show() #Muestro gráficamente lo anterior

print(listas_medias, listas_medianas)

plot.hist(listas_medias, bins = 50, range=(0,100))
plot.xlabel('MEDIAS Humedad')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medias") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior

plot.hist(listas_medianas, bins = 50, range=(0,100))
plot.xlabel('MEDIANAS Humedad')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medianas") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior


    


