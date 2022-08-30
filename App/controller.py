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
 """

from operator import mod
import config as cf
import model
import csv
#import tabulate

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newController():
    control = {'model': None}
    control['model'] = model.newCatalog()
    return control




# Funciones para la carga de datos
def loadTitles(catalog):
    files = ["amazon_prime_titles-utf8-small.csv", "disney_plus_titles-utf8-small.csv", "hulu_titles-utf8-small.csv", "netflix_titles-utf8-small.csv"]
    """streaming_services = [
                          ['amazon',0],
                          ['disney',0],
                          ['hulu',0],
                          ['netflix',0]]"""
    """"
    if file in 
    """
    for file in range(len(files)):
        titlesfile = cf.data_dir + files[file]
        input_file = csv.DictReader(open(titlesfile, encoding="utf-8"))
        #count = 0
        for title in input_file:
            model.addTitle(catalog, title)  
            
         #   count += 1
        #streaming_services[file][1] = count
    return model.titlesSize(catalog), model.directorsSize(catalog)
    #return model.titlesSize(catalog), streaming_services

def loadData(control):
    catalog = control['model']
    titles, directors = loadTitles(catalog)
    sortTitles(catalog)
    return titles, directors



# Funciones de ordenamiento

def sortTitles(catalog):
    return model.sortTitles(catalog)

# Funciones de consulta sobre el catálogo
