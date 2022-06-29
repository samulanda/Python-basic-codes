# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 07:30:33 2018

@author: landazabals
"""

#Funcion que crea una lista 2D con unas dimenciones especificadas a partir de una lista 1D. Si no hay 
#suficientes elementos en la lista 1D de entrada, se rellenan los elementos faltantes con None

#Function that creates a 2D list with given dimensions from a 1D list. If there is not enough #elements in the 1D list, the 2D list will fill the missing elements with "None"

def one_to_2D(A, fil, col):#def de funcion que acepta una lista unidimencional (A) y las dimenciones de la 
                           #lista 2D deseados a traves del valor fil (para filas) y col (para columnas)
                           
    rest=abs(fil-col)#factor necesario para colocar los elementos correctamente en la lista 2D
    
    if len(A)<(fil*col):#cuando no existen suficientes elementos en A para cumplir las dimenciones requeridas
                        #de fil*col
        for n in range(0,((fil*col)-len(A))):#lo que viene se realizara tantas veces como la resta entre 
                                             #fil*col - la longitud de A,
            A.append(None)#se rellena con None la lista A, hasta que tenga una longitud=fil*col

    if col>=fil:#si son mas o igual numero de columnas que de filas requeridas para la lista 2D
        lista=[]#lista 2D a llenar con los elementos de A
        for f in range(0,fil):#f tomando la cantidad de filas requeridas
            Fila=[]#listas a llenar, para cada fila, con la cantidad de columnas requeridas
            for c in range(f*(fil+rest),col+f*(fil+rest)):#tomando los elementos en A que representaran las 
                                                          #columnas en la lista 2D. ej si A=[2,4,3,1,5,6]
                                                          #fil=2 col=3, c tomara para f=0 el 2, 4 y 3. luego
                                                          #para f=1 tomara el 1,5,6
                Fila.append(A[c])#llenado de cada fila con las columnas c
            lista.append(Fila)#llenado de la lista 2D con las filas de arriba

        return(lista)

    else:
        lista=[]
        for f in range(0,fil):
            Fila=[]
            for c in range(f*(fil-rest),col+f*(fil-rest)):#el factor "rest" se resta
                Fila.append(A[c])
            lista.append(Fila)

        return(lista)
