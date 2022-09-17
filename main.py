import os

from ClaseCola import Cola

if __name__=='__main__':

    cola = Cola()

    def menu():
        print("                                             ")
        print("---------------------------------------------")
        print("MENU - SHUCOS DE GUATEMALA")
        print("1. Ordenar un shuco")
        print("2. Ver Cola de Ordenes")
        print("3. Recibir orden")
        print("4. Información Estudiante")
        print("5. Salir")
        print("---------------------------------------------")
        respuesta = input("Ingrese una opcion: ")

        if respuesta=='1':
            print("Ingresa un nombre a tu pedido:")
            nombrepedido=input()
            print("Bienvenido " + nombrepedido + "!")
            

   
            print("------------------------------------")
            print("             INGREDIENTES            ")
            print("1. Salchicha - 2 minutos")
            print("2. Chorizo - 3 minutos")
            print("3. Salami - 1.5 minutos")
            print("4. Longaniza - 4 minutos")
            print("5. Costilla - 6 minutos")
            print("------------------------------------")
            print("¿Qué tipo de shuco quieres ordenar?")

            shuco = input("")


            if shuco=='1':
                print("¿Quieres agregarle algún otro ingrediente?")
                shuco2 = input("")
                if shuco2 =='1':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salchicha' + ' , ' + 'Salchicha' + ' || Tiempo de preparación:  4 minutos')
                elif shuco2 == '2':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salchicha' + ' , ' + 'Chorizo' + ' || Tiempo de preparación:  5 minutos')
                elif shuco2 == '3':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salchicha' + ' , ' + 'Salami' + ' || Tiempo de preparación:  3.5 minutos')
                elif shuco2 == '4':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salchicha' + ' , ' + 'Longaniza' + ' || Tiempo de preparación:  6 minutos')
                elif shuco2 == '5':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salchicha' + ' , ' + 'Costilla' + ' || Tiempo de preparación:  8 minutos')

            elif shuco=='2':
                print("¿Quieres agregarle algún otro ingrediente?")
                shuco2 = input("")
                if shuco2 =='1':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Chorizo' + ' , ' + 'Salchicha' + ' || Tiempo de preparación:  5 minutos')
                elif shuco2 == '2':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Chorizo' + ' , ' + 'Chorizo' + ' || Tiempo de preparación:  6 minutos')
                elif shuco2 == '3':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Chorizo' + ' , ' + 'Salami' + ' || Tiempo de preparación:  4.5 minutos')
                elif shuco2 == '4':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Chorizo' + ' , ' + 'Longaniza' + ' || Tiempo de preparación: 7 minutos')
                elif shuco2 == '5':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Chorizo' + ' , ' + 'Costilla' + ' || Tiempo de preparación:  9 minutos')

            elif shuco=='3':
                print("¿Quieres agregarle algún otro ingrediente?")
                shuco2 = input("")
                if shuco2 =='1':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salami' + ' , ' + 'Salchicha' + ' || Tiempo de preparación:  3.5 minutos')
                elif shuco2 == '2':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salami' + ' , ' + 'Chorizo' + ' || Tiempo de preparación: 4.5 minutos')
                elif shuco2 == '3':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salami' + ' , ' + 'Salami' + ' || Tiempo de preparación:   3 minutos')
                elif shuco2 == '4':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salami' + ' , ' + 'Longaniza' + ' || Tiempo de preparación:  5.5 minutos')
                elif shuco2 == '5':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Salami' + ' , ' + 'Costilla' + ' || Tiempo de preparación:  7.5 minutos')

            elif shuco=='4':
                print("¿Quieres agregarle algún otro ingrediente?")
                shuco2 = input("")
                if shuco2 =='1':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Longaniza' + ' , ' + 'Salchicha' + ' || Tiempo de preparación:  6 minutos')
                elif shuco2 == '2':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Longaniza' + ' , ' + 'Chorizo' + ' || Tiempo de preparación:  7 minutos')
                elif shuco2 == '3':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Longaniza' + ' , ' + 'Salami' + ' || Tiempo de preparación:  5.5 minutos')
                elif shuco2 == '4':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Longaniza' + ' , ' + 'Longaniza' + ' || Tiempo de preparación:  8 minutos')
                elif shuco2 == '5':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Longaniza' + ' , ' + 'Costilla' + ' || Tiempo de preparación:  10 minutos')

            elif shuco=='5':
                print("¿Quieres agregarle algún otro ingrediente?")
                shuco2 = input("")
                if shuco2 =='1':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Costilla' + ' , ' + 'Salchicha' + ' || Tiempo de preparación:  8 minutos')
                elif shuco2 == '2':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Costilla' + ' , ' + 'Chorizo' + ' || Tiempo de preparación:  9 minutos')
                elif shuco2 == '3':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Costilla' + ' , ' + 'Salami' + ' || Tiempo de preparación:   7.5 minutos')
                elif shuco2 == '4':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Costilla' + ' , ' + 'Longaniza' + ' || Tiempo de preparación:  10 minutos')
                elif shuco2 == '5':
                    cola.encolar('Nombre: ' + nombrepedido + ' ||  Shuco con ingredientes:' + 'Costilla' + ' , ' + 'Costilla' + ' || Tiempo de preparación:  12 minutos')

            return menu()


        elif respuesta=='2':
            cola.imprimirCola()
            return menu()

        elif respuesta=='3':
            orden = cola.desencolar()
            print('La orden está lista para    :' + orden)
            print('¡Regrese pronto!')
            return menu()


        elif respuesta=='4':
            print("NOMBRE: Julio Alejandro Zaldaña Ríos")
            print("CARNET: 202110206")
            return menu()
        elif respuesta=='5':
            exit()


    menu()

    