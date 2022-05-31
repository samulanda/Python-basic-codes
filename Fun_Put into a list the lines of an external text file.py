# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:20:59 2018

@author: landazabals
"""

#Funcion que lee un archivo de texto externo y crea una lista con las lineas del archivo sin espacio entre
#lineas

#Function that reads an external text file and creates a list with the lines of the file without space between lines

def list_from_file(file_name):#def de la funcion que acepta un archivo de texto externo
    # Make a connection to the file
    file_pointer = open(file_name, 'r')#se prepara el archivo "file_name" para ser leido (r) y se asigna a la
                                       #variable file_pointer
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()#lee todas las lineas del archivo y las coloca en una lista llamada "data"
                                   #pero al final de cada linea aparecera "\n" (espacio entre lineas)
    #Codigo para eliminar los espacios (\n) entre lineas
    lista=[]#lista a llenar con las lineas del archivo de texto sin espacios
    for m in range(0,len(data)):#m tomando los indices de la lista llenada con las filas del texto, es decir 
                                #m son el numero de lineas en el texto
        fila=''#cadenas a llenar con los elementos que conforman cada linea. seran las filas de la lista de
               #arriba
        for i in data[m]:#i toma cada elemento de la linea del texto actual data[m]
            if i!='\n':#solo se toman los elementos distintos de '\n' (que da el espaciado entre lineas)
                fila=fila+i#se va colocando cada elemento a la fila actual
        lista.append(fila)#cada fila terminada se va colocando a la lista
    return(lista)
            

    
