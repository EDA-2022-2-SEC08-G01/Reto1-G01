"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
#import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    control = controller.newController()
    return control

    
def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar películas estrenadas en un periodo de tiempo")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Consultar contenido donde participa un actor")
    print("5- Consultar contenido por un género específico")
    print("6- Consultar contenido producido en un país")
    print("7- Consultar contenido con un director involucrado")
    print("8- Listar el TOP x de los géneros con más contenido")
    print("9- Listar el TOP x de los actores con más participaciones en contenido")
    print("0- Salir")



#catalog = None


def loadData(control):
    register = controller.loadData(control)
    return register

control = newController()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        register = loadData(control)
        print('Títulos cargados: ' + str(register))
        
        

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
