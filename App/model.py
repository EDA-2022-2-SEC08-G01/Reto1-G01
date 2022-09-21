"""
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


from atexit import register
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
import pandas as pd
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
        catalog[platform] = lt.newList(structure,cmpfunction = cmpID)
        
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
        'release_year': content['release_year'],
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


def firstLastSub(sub):
    firstLast = lt.newList("ARRAY_LIST")
    
    for content in lt.iterator(sub):
        index = lt.size(sub)
        for pos in range(1,3):
            first = lt.getElement(sub, pos)
            last = lt.getElement(sub, index - pos)
            lt.addFirst(firstLast, first)
            lt.addLast(firstLast, last)
            mgs.sort(firstLast, cmpMoviesByReleaseYear)
    
    return firstLast
    
def moviesInYears(catalog, initial_year, final_year):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    all_registers = 0
    start_time = getTime()
    for content in lt.iterator(platform):
        
        if content["type"] == "Movie":
            if int(content["release_year"]) >= initial_year and int(content["release_year"]) <=final_year:
                lt.addLast(sub, content)
                all_registers += 1
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    
    return sub, all_registers,delta_time

def TvShowsInPeriod(catalog, initialDate, finalDate):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    all_registers = 0
    start_time = getTime()
    for content in lt.iterator(platform):
        if len(content["date_added"])>0:
            date_added= content["date_added"].replace("-",",")
            tupla= tuple(date_added)
            fecha= int(tupla[0]),int(tupla[1]),int(tupla[2])
            if Numbermonths(initialDate) <= fecha <= Numbermonths(finalDate):
                lt.addLast(sub, content)
                all_registers += 1
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return sub, all_registers, delta_time

def findContentByCountry(catalog, country):
    platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    all_registers = {"TV Shows": 0, "Movies": 0}
    start_time = getTime()
    for content in lt.iterator(platform):
        if content["country"].lower() == country.lower():
            
            lt.addLast(sub, content)
            if content["type"] == "TV Show":
                all_cs["TV Shows"] += 1
            elif content["type"] == "Movie":
                all_registers["Movies"] += 1 
    mgs.sort(sub, cmpByTitle)
    final = manipularlista(sub)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return all_registers, final, delta_time


def findContentByGenre(catalog, genre):
    platform = catalog["general"]
    size = lt.size(platform)
    sub = lt.newList("ARRAY_LIST")
    register_movie = 0
    register_series = 0
    start_time = getTime()
    for content in lt.iterator(platform):
        if genre.lower() in content["listed_in"].lower():
            lt.addLast(sub,content)
            if content["type"] == "TV Show":
                register_series +=1
            elif content["type"]== "Movie":
                register_movie +=1
    mgs.sort(sub, cmpByTitle)
    final = manipularlista(sub)
    
    #sizesub = lt.size(sub)
    #irst_3 = lt.subList(sub,1, 3)
    #last_3 = lt.subList(sub,sizesub-3, 3)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return (final, register_series, register_movie), delta_time


def findContentByActor(catalog, nameAutor):
    platform = catalog["general"]
    size = lt.size(platform)
    sub = lt.newList("ARRAY_LIST")
    all_cs = {"TV Shows": 0, "Movies":0}

    start_time = getTime()
    for content in lt.iterator(platform):
        if nameAutor.lower() in content["cast"].lower():
            
            lt.addLast(sub, content)
            if content["type"] == "TV Show":
                all_cs['TV Shows'] += 1
            elif content["type"] == "Movie":
                all_cs['Movies'] += 1
    mgs.sort(sub, cmpByTitle)
    final = manipularlista(sub)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return all_registers, final, delta_time
                        

def directorInvolved(catalog, director):
    #platform = catalog["general"]
    sub = lt.newList("ARRAY_LIST")
    type_cs = {"TV Shows": 0, "Movies": 0}
    service_cs = {}
    genre_cs = {}

    start_time = getTime()
    for platform in catalog:
        count_service = 0
        if platform != "general":
            for content in lt.iterator(catalog[platform]):
                directors = content["director"].lower().split(",") #en caso de haber más de un director se realiza el split
                if director.lower() in directors: #se comprueba que el director esté 
                    if content["type"] == "Movie": #se comprueba si el tipo es película o serie y se le suma uno
                        type_registers["Movies"] += 1
                    elif content["type"] == "TV Show":
                        type_registers["TV Shows"] += 1
                    count_service += 1
                    service_registers[platform] = count_service #se le suma uno al diccionario de conteo de servicios
                    listed = content["listed_in"].split(", ") #se realiza el split de los géneros por si hay más de uno
                    for genre in listed: #se itera sobre los géneros para hacer el conteo
                        if genre not in genre_registers:
                            genre_registers[genre] = 0
                            genre_registers[genre] += 1
                        else:
                            genre_registers[genre] += 1
                    lt.addLast(sub, content)
    if lt.size(sub) >= 6:
        sub = firstLastSub(sub)
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return type_registers, service_registers, genre_registers, sub, delta_time

def topGenders(catalog, top):
    ans = lt.newList("ARRAY_LIST", cmpfunction=cmpGenre)
    general = catalog["general"]
    register = {"Genre": "", "Movies": 0, "TV Shows": 0, "Netflix": 0, "Disney plus": 0, "Hulu": 0, "Amazon prime": 0, "total": 0}
    start_time = getTime()
    for content in lt.iterator(general):
        c = copy.deepcopy(register)
        listed = content["listed_in"].lower().split(",")

        
        for gender in listed:
                gender = gender.strip()
                        
                c["Genre"] = gender
                if lt.isPresent(ans, c) == 0:
                    if content["type"] == "Movie":
                        c["Movies"] += 1
                    elif content["type"] == "TV Show":
                        c["TV Shows"] += 1
                        
                    if content["streaming_service"].lower() == "netflix":
                        c["Netflix"] += 1
                    elif content["streaming_service"].lower() == "amazon_prime":
                        c["Amazon prime"] += 1
                    elif content["streaming_service"].lower() == "hulu":
                        c["Hulu"] += 1
                    elif content["streaming_service"].lower() == "disney_plus":
                        c["Disney plus"] += 1    
                    c["total"] += 1
                    lt.addLast(ans, c)
                elif lt.isPresent(ans, c) > 0:
                    
                    for gen in lt.iterator(ans):
                        if gen["Genre"].lower() == gender.lower():   
                            if content["type"] == "Movie":
                                gen["Movies"] += 1
                                
                            elif content["type"] == "TV Show":
                                gen["TV Shows"] += 1
                            
                            if content["streaming_service"].lower() == "netflix":
                                gen["Netflix"] += 1
                            elif content["streaming_service"].lower() == "amazon_prime":
                                gen["Amazon prime"] += 1
                            elif content["streaming_service"].lower() == "hulu":
                                gen["Hulu"] += 1
                            elif content["streaming_service"].lower() == "disney_plus":
                                gen["Disney plus"] += 1
                            gen["total"] += 1
    mgs.sort(ans, cmpByCount) 
    size = lt.size(ans) - 1
    sub = lt.subList(ans, size - top, top )
  
    return sub





def cmpGenre(element1, element2):
    
    if element1["Genre"] == element2["Genre"]:
        return 0
    elif element1["Genre"] > element2["Genre"]:
        return 1
    return -1

def cmpID(element1, element2):
    
    if element1["show_id"] == element2["show_id"]:
        return 0
    elif element1["show_id"] > element2["show_id"]:
        return 1
    return -1

def cmpGenre(element1, element2):
    
    if element1["Genre"] == element2["Genre"]:
        return 0
    elif element1["Genre"] > element2["Genre"]:
        return 1
    return -1

# funciones para comparar elementos dentro de algoritmos de ordenamientos

def cmpTvShowsByDateAdded(tvshow1, tvshow2):
    respuesta = False

    duration1 = tvshow1["duration"].split()
    duration2 = tvshow2["duration"].split()
    date_added1 = tvshow1["date_added"].split()
    date_added2 = tvshow2["date_added"].split()

    if len(date_added1) > 0 and len(date_added2) > 0:
        if (int(date_added1[0])> int(date_added2[0])):
            respuesta= True
        elif  (int(date_added1[0]) == int(date_added2[0])):
            if (tvshow1['title']) < (tvshow2['title']):
                respuesta = True 
            elif  (tvshow1['title']) == (tvshow2['title']):
                if len(duration1) > 0 and len(duration2) > 0:
                    if (int(duration1[0]) < int(duration2[0])):
                        respuesta = True
    return respuesta


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

    if (int(movie1['release_year']) < int(movie2['release_year'])):
            respuesta = True
    elif  (int(movie1['release_year']) == int(movie2['release_year'])):
        if (movie1['title']) < (movie2['title']):
            respuesta = True 
        elif  (movie1['title']) == (movie2['title']):
            if len(duration1) > 0 and len(duration2) > 0:
                if (int(duration1[0]) < int(duration2[0])):
                    respuesta = True
    return respuesta

def cmpByTitle(movie1, movie2):
    respuesta = False
    if movie1["title"] < movie2["title"]:
        respuesta = True
    elif movie1["title"] == movie2["title"]:
        if int(movie1["release_year"]) < int(movie2["release_year"]):
            respuesta = True
        elif int(movie1["release_year"]) == int(movie2["release_year"]):
            if movie1["director"] < movie2["director"]:
                respuesta = True
    return respuesta

def cmpByCount(genre1, genre2):
    respuesta = False
    if genre1["total"] < genre2["total"]:
        respuesta = True
    elif genre1["total"] == genre2["total"]:
        if genre1["Netflix"] < genre2["Netflix"]:
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

#Función para filtar las listas y unir, y crear un dataframe
def manipularlista(sub):
    sizesub = lt.size(sub)
    first_3 = lt.subList(sub,1, 3)
    last_3 = lt.subList(sub,sizesub-3, 3)
    listafinal =[]
    for i in lt.iterator(first_3):
        listafinal.append(i) 
    for a in lt.iterator(last_3):
        listafinal.append(a)
    df=pd.DataFrame(listafinal)
    return df
#Funciones adicionales
def Numbermonths(date):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 
    'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 
    'October': 10, 'November': 11, 'December': 12}
    date = date.replace(',', ' ')
    date = date.split(' ')

    day = date[1]
    month = date[0]
    year = date[2]

    if day < '10':
        day = int(day[1])
    return (int(year), month, day)

    
    
    



