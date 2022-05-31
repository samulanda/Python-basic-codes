# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 13:13:01 2018

@author: Samuel
"""

#Funcion que toma un archivo de texto con las notas de alunos de una materia completa, quices, asignaciones
#midterm y examen final y crea un diccionario con el nombre de cada alumno y si paso o no la materia, 
#tomando ciertos criterios:- Los quices son 6 quices, se retiran los dos con peores notas y el promedio de
#los restantes equivale al 25% de la nota.- Las asignaciones son 4, se retira la de peor nota y el promedio
#de las 3 restantes equivalen al 25%.- El mindertm y el final valen 25% cada una. - El alumno pasa con >=60%

def my_final_grade_calculation(file_name):#funcion que acepta un archivo de texto
    abrir=open(file_name,'r')#abrir el archivo
    arch=abrir.readlines()#crear una lista 2D cuyas filas son cadenas de caracteres de las lineas del archivo
    abrir.close()#cerrar el archivo de texto

    #Crear listas cuyos elementos son los nombres y notas:
    notas=[]#lista 2D a llenar con las notas de cada alumno
    nombres=[]#lista a llenar con los nombres de los alumnos
    for line in arch:#line tomando cada fila compuesta por un str completo
        line=line.replace(' ','')#eliminar los espacios de las cadenas
        line=line.replace('\n','')#eliminar los saltos de lineas de las cadenas
        alumno=line.split(',')#crear listas usando las "," como separadores para
                              #cada cadena
        nombres.append(alumno[0])#llenado de la lista de nombres, con el primer elemento de cada fila
        alumno_int=[]#Lista con las notas de los alumnos transformadas de str a int
        for n in alumno[1:]:#tomar cada elemento de la fila 'alumno' sin el primero
            alumno_int.append(int(n))#llenar la fila alumno_int con los elementos de 'alumno' transf en int
        notas.append(alumno_int)#llenado de la lista 2D con las filas 'alumno_int'
        
    #Crear lista 2D solo con las notas de los quices por alumno:
    Quices=[]#lista 2D a llenar
    for fila in notas:#filas de la lista 2D 'notas' con solo todas las notas por alumno
        Quiz=[]#fila a llenar y colocar en la lista 2D 'Quices'
        for n in fila[:6]:#tomando solo las notas de los quices que van de la primera a la 6ta en 'notas'
            Quiz.append(n)#llenado de las filas con las notas de los quices
            Quiz.sort()#ordenar de forma creciente las notas, para mas adelante retirar las 2 peores
        Quices.append(Quiz)#agregar las filas a la lista 2D

    #Crear una lista con el promedio de las notas de los quices al 25%:
    Quices_25=[]#lista a llenar
    for fila in Quices:#tomar cada fila de la lista 2D Quices
        Q_fila=(((sum(fila[2:]))/4)*0.25)#sumar todos los quices, menos los dos primeros (peores notas)
                                         #promediarlos entre 4 y sacarles el 25%
        Quices_25.append(Q_fila)#llenado de la lista con el promedio de los quices al 25%

    #Crear lista 2D solo con las notas de las asignaciones por alumno:
    Asignaciones=[]
    for fila in notas:
        Asignacion=[]
        for n in fila[6:10]:#tomando solo las notas de los asig que van de la 6ta a la 10ma en 'notas'
            Asignacion.append(n)
            Asignacion.sort()
        Asignaciones.append(Asignacion)
        
    #Crear una lista con el promedio de las notas de las asignaciones al 25%:
    Asignaciones_25=[]
    for fila in Asignaciones:
        A_fila=(((sum(fila[1:]))/3)*0.25)#sumar todas las asig, menos la primera (peor nota)
                                         #promediarlas entre 3 y sacarles el 25%
        Asignaciones_25.append(A_fila)

    #Crear la lista con las notas del midterm llevadas al 25%:
    midterm_25=[]#lista a llenar
    for fila in notas:#las filas de la lista 2D notas
        midterm_25.append(fila[-2]*0.25)#tomar solo el penultimo, con la nota del midterm para cada alumno
                                        #sacarle el 25% y agregarla a la lista midterm_25

    #Crear la lista con las notas del final llevadas al 25%:
    final_25=[]#lista a llenar
    for fila in notas:#las filas de la lista 2D notas
        final_25.append(fila[-1]*0.25)#tomar solo el ultimo, con la nota del final para cada alumno
                                      #sacarle el 25% y agregarla a la lista final_25

    #Crear una lista con el porcentaje total sacado por cada alumno:
    totales=[]#lista a llenar
    for i in range(0,len(nombres)):#indices segun el numero de alumnos
        total=Quices_25[i]+Asignaciones_25[i]+midterm_25[i]+final_25[i]#sumar los porcentajes de cada 
                                                                       #evaluacion para cada alumno
        totales.append(total)#el procentaje total de cada alumno se agrega a la lista 'totales'

    #Crear lista con la condicion de si paso o no cada alumno:
    si_no_paso=[]#lista a llenar
    for n in totales:#tomar el porcentaje total sacado por alumno de la lista 'totales'
        if n>=60:#si la nota de alumno n actual es mayor o igual a 60
            si_no_paso.append('pass')#se agrega 'pass' a la lista
        else:#si la nota de alumno n actual es menor a 60
            si_no_paso.append('fail')#se agrega 'fail' a la lista

    #Creacion del diccionario con cada alumno y si paso o no la materia:
    dic={}#diccionario a llenar
    for n in range(0,len(nombres)):#indice con la cantidad de alumnos
        dic[nombres[n]]=si_no_paso[n]#al key nombres[n] se le asigna el value ni_no_paso[n], al nombre se le
                                     #asigna 'pass' o 'fail'

    return(dic)