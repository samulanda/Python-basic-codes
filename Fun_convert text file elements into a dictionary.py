# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:20:59 2018

@author: landazabals
"""

#Funcion que crea un diccionarioa a partir de un archivo de texto. El archivo contiene nombres de personas y
#unas cuatro cifras (calificaciones), asociadas a cada uno de ellos. el diccionario que se genera tiene como
#keys los nombres y los values son las calificaciones

def dic_arch(test_python):#def de funcion que acepta un archivo de texto como entrada, con los nombres de 
                          #de personas y sus calificaciones en 4 cursos
    archivo= open(test_python, "r")#preparar el archivo para ser leido ("r")
    arch=archivo.readlines()#leer todas las lineas del archivo y colocarlas en una lista
    #Codigo para eliminar los espacios (\n) entre lineas
    lista=[]#lista a llenar con las lineas del archivo de texto sin espacios
    for m in range(0,len(arch)):#m tomando los indices de la lista llenada con las filas del texto, es decir 
                                #m son el numero de lineas en el texto
        fila=''#cadenas a llenar con los elementos que conforman cada linea. seran las filas de la lista de
               #arriba
        for i in arch[m]:#i toma cada elemento de la linea del texto actual data[m]
            if i!='\n':#solo se toman los elementos distintos de '\n' (que da el espaciado entre lineas)
                fila=fila+i#se va colocando cada elemento a la fila actual
        lista.append(fila)#cada fila terminada se va colocando a la lista

    #Codigo para convertir en listas, las filas de la lista generada con las lineas del archivo, que eran 
    #cadenas de caracteres
    lista_arch=[]#lista a llenar con las filas en forma de cadena de caracteres en sublistas
    for n in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        fila_list=lista[n].split(',')#convertir la cadena de caracteres en listas, separando sus elementos
                                     #con las comas que tenian las lineas del archivo
        lista_arch.append(fila_list)#llenado de la lista con las sublistas o filas

    lista_nombres=[]#lista a llenar con solo los nombres del archivo
    for l in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        lista_nombres.append(lista_arch[l][0])#llenado de la lista con solo el primer elemento de cada 
                                              #sublista o fila de la lista_arch (nombres de las personas)

    lista_1Eval=[]#lista a llenar con la nota sacada por cada persona en la 1era evaluacion
    for l in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        lista_1Eval.append(float(lista_arch[l][1]))#llenado de la lista con solo el 2do elemento de cada 
                                                   #sublista o fila de la lista_arch (notas 1er curso)
            
    lista_2Eval=[]#lista a llenar con la nota sacada por cada persona en la 2da evaluacion
    for l in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        lista_2Eval.append(float(lista_arch[l][2]))#llenado de la lista con solo el 3er elemento de cada 
                                                   #sublista o fila de la lista_arch (notas 2do curso)

    lista_3Eval=[]#lista a llenar con la nota sacada por cada persona en la 3era evaluacion
    for l in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        lista_3Eval.append(float(lista_arch[l][3]))#llenado de la lista con solo el 4to elemento de cada 
                                                   #sublista o fila de la lista_arch (notas 3er curso)

    lista_4Eval=[]#lista a llenar con la nota sacada por cada persona en la 3era evaluacion
    for l in range(0,len(arch)):#n tomando la cantidad de filas en la lista (numero de lineas del archivo)
        lista_4Eval.append(float(lista_arch[l][4]))#llenado de la lista con solo el 5to elemento de cada 
                                                   #sublista o fila de la lista_arch (notas 4to curso)

    dic={}#diccionario a llenar de la forma especificada arriba en el titulo
    for n in range(0,len(lista_nombres)):#n son los indices de la lista que contiene los nombres
        dic[lista_nombres[n]]=[lista_1Eval[n],lista_2Eval[n],lista_3Eval[n],lista_4Eval[n]]#llenado de la 
                                                                                           #lista con los keys
                                                                                           #como los nombres
                                                                                           #dic[lista_nombres[n]]
                                                                                           #y sus values:
                                                                                           #lista_1Eval[n].....
                                                                                           #para cada key n
    return(dic)

print(dic_arch('test_python.txt'))