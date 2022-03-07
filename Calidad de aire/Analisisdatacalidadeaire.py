# -*- coding: utf-8 -*-
"""
Spyder Editor
Autor: Santiago Sánchez Ramírez

Este programa genera un histograma de un archivo .csv de la base de datos de los sensores de calidad de aire de Siata,
filtrando por calidad y obteniendo su mediana y media. Con estos últimos datos se realiza también un histograma
para observar su distribución
"""
#A continuación importo las librerías
import glob   #Con esta librería realizo la lectura de todos los archivos dentro de mi directorio
import pandas as pd  #Con esta librería manipulo las bases de datos
import matplotlib.pyplot as plot   #Con esta librería grafico
from numpy import median, mean    #Con esta librería manipulo matemáticamento los datos

bases = glob.glob("*.csv")  #En el directorio importo los archvos .csv
listas_medias = []  #Creo la lista donde voy a alojar los valores de las medias
listas_medianas = []    #Creo la lista donde voy a alojar los valores de las medias

#Con este ciclo voy a recorrer cada archivo de bases de datos de PM2.5
for i in range(0,len(bases), 1):
    lista = pd.read_csv(bases[i], sep=",")  #parametrizo las bases de datos que voy a usar
    df_mask = lista["calidad_pm25"]==1  #Creo un filttro para las medidas de buena calidad (Calidad = 1)
    listafiltrada = lista[df_mask]  #Creo una variable nueva para este filtro
    mediana = median(listafiltrada["pm25"]) #Obtengo la mediana de la columna de humedad de la lista que estoy leyendo
    media = mean(listafiltrada["pm25"]) #Obtengo la media de la columna de humedad de la lista que estoy leyendo
    print("para la estación ", bases[i], "la media es: ", media, "y la mediana: ", mediana) #Muestro la infromación
    listas_medias.append(media)
    listas_medianas.append(mediana)
    
    plot.hist(x=listafiltrada["pm25"], bins = 100, range=(0,100))
    plot.xlabel('PM2.5')  #Eje coordenado 
    plot.ylabel('Frecuencia') #Eje ordenado
    plot.suptitle(bases[i]) #Muestro el nombre de la base de datos
    plot.text(65, 40, "La media es: ")
    plot.text(90, 40, round(media, 3)) 
    plot.text(65, 30, "La mediana es: ")
    plot.text(90, 30, round(mediana, 3))#Muestro el valor de la mediana
    plot.show() #Muestro gráficamente lo anterior
    
print(listas_medias, listas_medianas)

plot.hist(listas_medias, bins = None, range=(15,35))
plot.xlabel('MEDIAS PM2.5')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medias") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior

plot.hist(listas_medianas, bins=None, range=(15,35))
plot.xlabel('MEDIANAS PM2.5')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medianas") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior
  
#Con este ciclo voy a recorrer cada archivo de bases de datos de PM10
for i in range(0,len(bases), 1):
    lista = pd.read_csv(bases[i], sep=",")  #parametrizo las bases de datos que voy a usar
    df_mask = lista["calidad_pm10"]==1  #Creo un filttro para las medidas de buena calidad (Calidad = 1)
    listafiltrada = lista[df_mask]  #Creo una variable nueva para este filtro
    mediana = median(listafiltrada["pm10"]) #Obtengo la mediana de la columna de humedad de la lista que estoy leyendo
    media = mean(listafiltrada["pm10"]) #Obtengo la media de la columna de humedad de la lista que estoy leyendo
    print("para la estación ", bases[i], "la media es: ", media, "y la mediana: ", mediana) #Muestro la infromación
    listas_medias.append(media)
    listas_medianas.append(mediana)
    
    plot.hist(x=listafiltrada["pm10"], bins = 100, range=(0,100))
    plot.xlabel('PM10')  #Eje coordenado 
    plot.ylabel('Frecuencia') #Eje ordenado
    plot.suptitle(bases[i]) #Muestro el nombre de la base de datos
    plot.text(65, 23, "La media es: ")
    plot.text(90, 23, round(media, 3)) 
    plot.text(65, 20, "La mediana es: ")
    plot.text(90, 20, round(mediana, 3))#Muestro el valor de la mediana
    plot.show() #Muestro gráficamente lo anterior
    
print(listas_medias, listas_medianas)

plot.hist(listas_medias, bins = None, range=(0,40))
plot.xlabel('MEDIAS PM10')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medias") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior

plot.hist(listas_medianas, bins = None, range=(0,40))
plot.xlabel('MEDIANAS PM10')  #Eje coordenado 
plot.ylabel('Frecuencia') #Eje ordenado
plot.suptitle("Medianas") #Muestro el nombre de la base de datos
plot.show() #Muestro gráficamente lo anterior
  







