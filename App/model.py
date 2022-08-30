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


from doctest import ELLIPSIS_MARKER
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog ={
        'titles': None,
        'directors': None
    }
    catalog['titles'] = lt.newList('ARRAY_LIST')
    catalog['directors'] = lt.newList('SINGLE_LINKED', cmpfunction=comparedirector)
    return catalog 


# Funciones para agregar informacion al catalogo
def addTitle(catalog, title):
    
    lt.addLast(catalog['titles'], title)
    directors = title["director"].split(",")
    for director in directors:
        addTitleDirector(catalog, director.strip(), title)
    return catalog

def addTitleDirector(catalog, directorname, title):
    directors = catalog["directors"]
    
    posdirector = lt.isPresent(directors, directorname)
    if posdirector > 0:
        director = lt.getElement(directors, posdirector)
    else:
        director = newDirector(directorname)
        lt.addLast(directors, director)
  
    
    lt.addLast(director['titles'], title)
    return catalog 
# Funciones para creacion de datos

def newDirector(name):
    director = {'name': '', 'titles': None, "average_rating": 0}
    director['name'] = name
    director['titles'] = lt.newList("ARRAY_LIST")
    return director
    
# Funciones de consulta



def titlesSize(catalog):
    return lt.size(catalog['titles'])

def directorsSize(catalog):
    return lt.size(catalog['directors'])

# Funciones utilizadas para comparar elementos dentro de una lista

# funciones para comparar elementos dentro de algoritmos de ordenamientos
def compareyear(title1, title2):
    return (int(title1["release_year"]) > int(title2["release_year"]))

def comparedirector(directorname1, director):
    if directorname1.lower() == director["name"].lower():
        return 0
    elif directorname1.lower() > director["name"].lower():
        return 1
    return -1
# Funciones de ordenamiento
def sortTitles(catalog):
    sa.sort(catalog["titles"], compareyear)