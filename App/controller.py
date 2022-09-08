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

from atexit import register
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
    control["model"] = model.newCatalog()
    return control
 



# Funciones para la carga de datos

def loadTitlesDefault(catalog):
    register = 0
    all_registers={}
    uuid= 0
    print(catalog)
    for service in catalog: #service toma el valor de amazon, hulu, etc
        if service != "general":
            individual_register = 0    
            platform = catalog[service]
            file = cf.data_dir + service + "_titles-utf8-small.csv"
            input_file = csv.DictReader(open(file, encoding='utf-8'))
            for content in input_file: #content toma el valor de cada diccionario "cada línea del archivo"
                model.addContent(platform, content, service, uuid)
                model.addContent(catalog["general"], content, service, uuid)
                uuid += 1
            register += model.platformSize(platform)
            individual_register += model.platformSize(platform)
            all_registers[service] = individual_register
    return register, all_registers

def loadDataDefault(control):
    catalog = control['model']
    register, all_registers = loadTitlesDefault(catalog)
    return register, all_registers


def loadTitles(catalog, sampleSize):
    sample = str(sampleSize) + "pct"
    if sampleSize == 100:
        sample = "large"
    register = 0
    all_registers={}
    uuid= 0
    for service in catalog: #service toma el valor de amazon, hulu, etc
        
        if service != "general":
            individual_register = 0    
            platform = catalog[service]
            file = cf.data_dir + service + "_titles-utf8-" + sample + ".csv"
            input_file = csv.DictReader(open(file, encoding='utf-8'))
            for content in input_file: #content toma el valor de cada diccionario "cada línea del archivo"
                model.addContent(platform, content, service, uuid)
                model.addContent(catalog["general"], content, service, uuid)
                uuid += 1
            register += model.platformSize(platform)
            individual_register += model.platformSize(platform)
            all_registers[service] = individual_register
    return register, all_registers

def loadData(control, sampleSize):
    catalog = control["model"]
    register, all_registers = loadTitles(catalog, sampleSize)
    
    return register, all_registers


def firstAndLast(catalog, num):
    return model.firstAndLast(catalog, num)


# Funciones de ordenamiento
def choosingSorts(control, orderType):
    return model.choosingSorts(control["model"], orderType)

control = newController()
data = loadData(control, 50)


def sortCatalog(control, order):
    catalog = control["model"]
    return model.sortCatalog(catalog, order)
# Funciones de consulta sobre el catálogo
