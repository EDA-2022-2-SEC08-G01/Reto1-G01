﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from doctest import ELLIPSIS_MARKER
from tempfile import gettempdir
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import mergesort as mgs
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
import time 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(structure):
    catalog ={
        'amazon_prime': None,
        'disney_plus': None,
        'hulu': None,
        'netflix': None,
        'general': None
    }
    for platform in catalog:
        catalog[platform] = lt.newList(structure)
        #ins.sort(catalog[platform], cmpMoviesByReleaseYear)
    return catalog 


# Funciones para agregar informacion al catalogo
def addContent(platform, content, platform_name, uuid):
    """"
    platform: plataforma a la que se va agregar, ejemplo: catalog['amazon_prime']
    content: el contenido que se va a añadir, viene como un diccionario
    platform_name: nombre de la plataforma que se va a añadir
    """
    data = {
        'show_id': uuid,
        'streaming_service': platform_name,
        'type': content['type'],
        'title': content['title'],
        'director': content['director'],
        'cast': content['cast'],
        'country': content['country'],
        'date_added': content['date_added'],
        'release_year': int(content['release_year']),
        'rating': content['rating'],
        'duration': content['duration'],
        'listed_in': content['listed_in'],
        'description': content['description']
    }
    lt.addLast(platform,data)


# Funciones para creacion de datos



    
# Funciones de consulta

def firstAndLast(catalog):
    firstLast = lt.newList('ARRAY_LIST') # se crea el array donde se guardarán los primeros 3 y los últimos 3 x
    
    for service in catalog:
        if service == "general":
            line = catalog[service]
            index = lt.size(line) -1 #se guarda la última posiciónS
            for pos in range(3):
                first = lt.getElement(line, pos)
                last = lt.getElement(line, index - pos)
                lt.addFirst(firstLast, first)
                lt.addLast(firstLast, last)
    return firstLast

def findContentByCountry(catalog, country):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    all_registers = {"TV Shows": 0, "Movies": 0}
    for content in lt.iterator(platform):
        if content["country"].lower() == country.lower():
            
            lt.addLast(sub, content)
            if content["type"] == "TV Show":
                all_registers["TV Shows"] += 1
            elif content["type"] == "Movie":
                all_registers["Movies"] += 1
            
    return all_registers, sub
            
def moviesInYears(catalog, initial_year, final_year):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    all_registers = 0
    for content in lt.iterator(platform):
        
        if content["type"] == "Movie":
            if int(content["release_year"]) >= initial_year and int(content["release_year"]) <=final_year:
                lt.addLast(sub, content)
                all_registers += 1
    return sub, all_registers

def directorInvolved(catalog, director):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    type_registers = {"TV Shows": 0, "Movies": 0}
    service_registers = {}
    genre_registers = {}
    for content in lt.iterator(platform):
        directors = content["director"].lower().split(",")
        print(directors)
        if director.lower() in directors:
            listed_register = 0
            if content["type"] == "Movie":
                type_registers["Movies"] += 1
            elif content["type"] == "TV Show":
                type_registers["TV Shows"] += 1
            listed_register += 1
            genre_registers[content["listed_in"]] = listed_register
            service_registers[content["streaming_service"]] = listed_register


    return type_registers, service_registers





def platformSize(platform):
    return lt.size(platform)

# Funciones utilizadas para comparar elementos dentro de una lista

# funciones para comparar elementos dentro de algoritmos de ordenamientos
def cmpMoviesByReleaseYear(movie1, movie2):
    """
    Devuelve verdadero (True) si el release_year de movie1 son menores que los
    de movie2, en caso de que sean iguales tenga en cuenta el titulo y en caso de que
    ambos criterios sean iguales tenga en cuenta la duración, de lo contrario devuelva
    falso (False).
    Args:
    movie1: informacion de la primera pelicula que incluye sus valores 'release_year',
    ‘title’ y ‘duration’
    movie2: informacion de la segunda pelicula que incluye su valor 'release_year', 
    ‘title’ y ‘duration’
    """
    respuesta = False 
    #if movie1["type"] == "Movie" and movie2["type"] == "Movie":
    duration1 = movie1["duration"].split()
    duration2 = movie2["duration"].split()

    if ((movie1['release_year']) < (movie2['release_year'])):
            respuesta = True
    elif  ((movie1['release_year']) == (movie2['release_year'])):
        if (movie1['title']) < (movie2['title']):
            respuesta = True 
        elif  (movie1['title']) == (movie2['title']):
            if len(duration1) > 0 and len(duration2) > 0:
                if (int(duration1[0]) < int(duration2[0])):
                    respuesta = True
    return respuesta

def choosingSorts(catalog, orderType):
    platform = catalog["general"]
    size = lt.size(catalog["general"])
    sub = lt.subList(platform, 1, size)
    if orderType == "shell":
        startTime = getTime()
        sorted_list = sa.sort(sub, cmpMoviesByReleaseYear)
        endTime = getTime()
    elif orderType == "insertion":
        startTime = getTime()
        sorted_list = ins.sort(sub, cmpMoviesByReleaseYear)
        endTime = getTime()
    elif orderType == "selection":
        startTime = getTime()
        sorted_list = sel.sort(sub, cmpMoviesByReleaseYear)
        endTime = getTime()
    elif orderType == "merge":
        startTime = getTime()
        sorted_list = mgs.sort(sub, cmpMoviesByReleaseYear)
        endTime = getTime()
    elif orderType == "quick":
        startTime = getTime()
        sorted_list = qs.sort(sub, cmpMoviesByReleaseYear)
        endTime = getTime()

    delta = deltaTime(startTime, endTime)  
    return sorted_list, delta

# Funciones de ordenamiento

# Funciones para medir tiempos de ejecucion
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed