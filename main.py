import os

from ClaseCola import Cola

if __name__=='__main__':

    cola = Cola()

    def menu():
        print("                                             ")
        print("---------------------------------------------")
        print("MENU - SHUCOS DE GUATEMALA")
        print("1. Ordenar un shuco")
        print("2. Salir")
        print("---------------------------------------------")
        respuesta = input("Ingrese una opcion: ")

        if respuesta=='1':
            print("Ingresa un nombre a tu pedido:")
            nombrepedido=input()
            print("Bienvenido " + nombrepedido + "!")
            return menu()
                

        elif respuesta=='2':
            exit()


    menu()