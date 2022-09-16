import os

from ClaseCola import Cola

if __name__=='__main__':

    cola = Cola()

    def menu():
        print("                                             ")
        print("---------------------------------------------")
        print("MENU - SHUCOS DE GUATEMALA")
        print("1. Ordenar un shuco")
        print("2. Información Estudiante")
        print("3. Salir")
        print("---------------------------------------------")
        respuesta = input("Ingrese una opcion: ")

        if respuesta=='1':
            print("Ingresa un nombre a tu pedido:")
            nombrepedido=input()
            print("Bienvenido " + nombrepedido + "!")
            
            
            print("------------------------------------")
            print("             INGREDIENTES            ")
            print("Salchicha - 2 minutos")
            print("Chorizo - 3 minutos")
            print("Salami - 1.5 minutos")
            print("Longaniza - 4 minutos")
            print("Costilla - 6 minutos")
            print("------------------------------------")
            print("¿Qué tipo de shuco quieres ordenar?")

            shuco = input("")

            return menu()

        elif respuesta=='2':
            print("NOMBRE: Julio Alejandro Zaldaña Ríos")
            print("CARNET: 202110206")
            return menu()
            
        elif respuesta=='3':
            exit()


    menu()