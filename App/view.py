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
import controller as controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    control = controller.newController()
    return control

def chooseStructure():
    structure = int(input("Seleccione una estructura para organizar los datos (0 para SINGLE_LINKED o 1 para ARRAY_LIST): "))
    if structure == 0:
        return "SINGLE_LINKED"
    elif structure == 1:
        return "ARRAY_LIST"

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar películas estrenadas en un periodo de tiempo")
    print("3- Listar programas de televisión agregados en un periodo de tiempo")
    print("4- Consultar contenido donde participa un actor")
    print("5- Consultar contenido por un género específico")
    print("6- Consultar contenido producido en un país")
    print("7- Consultar1 contenido con un director involucrado")
    print("8- Listar el TOP x de los géneros con más contenido")
    print("9- Seleccionar tipo de lista, ordenamiento y muestra")
    print("0- Salir")


def countPlatformTable(ar):
    values = list(ar.values())
    keys = list(ar.keys())
    platforms = [[keys[0],str(values[0])],[keys[1],str(values[1])],[keys[2],str(values[2])],[keys[3],str(values[3])]]
    print(tabulate((platforms), headers= ["Service Name", "count"], tablefmt = "fancy_grid"))
    print("\n")
    
#catalog = None

def loadData(control, sampleSize):
    register = controller.loadData(control, sampleSize)
    return register

def loadDataDefault(control):
    register = controller.loadDataDefault(control)
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
        register, ar = loadDataDefault(control)
        print('Títulos cargados: ' + str(register))
        print("-"*100)
        print(countPlatformTable(ar))
        num = int(input("Ingrese el número de los primeros y últimos títulos que desea conocer: "))
        firstAndLast= controller.firstAndLast(control["model"], num)
        print(firstAndLast)
        

    elif int(inputs[0]) == 9:
        
        sampleSize = int(input("Ingrese el porcentaje de la muestra ('5', '20', '30', '50', '100'): "))
        orderType = input("Ingrese el ordenamiento a usar ('shell', 'insertion', 'selection'): ")
        register, ar = loadData(control, sampleSize)
        sorted_list, delta = controller.choosingSorts(control, orderType)
        print(delta)
        print("-"*100)
        print(len(sorted_list))
        # centinel = True
        # while centinel: 
        #     structure = int(input("Seleccione la estructura en la cual se organizarán los datos (0 para SINGLE_LINKED o 1 para ARRAY_LIST): "))
        #     if structure == 1:
        #         controller.newController('ARRAY_LIST')
        #     elif structure == 0:
        #         controller.newController('SINGLE_LINKED')
        #     else:
        #         print('Digite el numero correcto para la estructura')
        #     while centinel:
        #         order = int(input("Ingrese el tipo de ordenamiento iterativo (0 para shell, 1 para selection, 2 para insertion: "))
        #         if 0<=order<=2:
        #             controller.sortCatalog(control, order)
        #             centinel = False
        #         else:
        #             print('Digite el numero correcto para el ordenamiento')
        
        
    else:
        sys.exit(0)
sys.exit(0)
