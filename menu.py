#! /usr/bin/env python3
from anotador import Anotador
import sys
class Menu:
    '''Mostrar un menÃƒÂº y responder a las opciones'''
    def __init__(self):
        self.anotador = Anotador()
        self.opciones= {
            "1": self.mostrar_notas,
            "2": self.buscar_notas,
            "3": self.agregar_nota,
            "4": self.modificar_nota,
            "5": self.salir
        }

    def mostrar_menu(self):
        print("""
MenÃƒÂº del anotador:
1. Mostrar todas las notas
2. Buscar Notas
3. Agregar Nota
4. Modificar Nota
5. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opciÃƒÂ³n: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opciÃƒÂ³n vÃƒÂ¡lida".format(opcion))

    def mostrar_notas(self, notas=None):
        '''Si recibe como parÃƒÂ¡metro una lista de notas, muestra id, texto y
        etiquetas de esas notas. Si no recibe el parÃƒÂ¡metro, muestra id, texto
        y etiquetas de todas las notas'''
        #TODO: Construir este mÃƒÂ©todo, borrar el siguiente renglÃƒÂ³n:
        if notas:
            for nota in notas:
                print("ID: "+str(nota.id))
                print("TEXTO: "+nota.texto)
                print("ETIQUETAS: "+nota.etiquetas)
        else:
            for nota in self.anotador.notas:
                print("ID: "+ str(nota.id))
                print("TEXTO: "+nota.texto)
                print("ETIQUETAS: "+nota.etiquetas)


    def buscar_notas(self):
        filtro = input("Buscar: ")
        notas = self.anotador.buscar(filtro)
        if notas:
            self.mostrar_notas(notas)
        else:
            print("Ninguna nota coincide con la bÃƒÂºsqueda")

    def agregar_nota(self):
        '''Solicita un texto al usuario y agrega una nueva nota con ese texto'''
        #TODO: Construir este mÃƒÂ©todo, borrar el siguiente renglÃƒÂ³n:
        texto=input("ingresar el texto:")
        self.anotador.nueva_nota(texto)

    def modificar_nota(self):
        id = input("Ingrese el id de la nota a modificar: ")
        texto = input("Ingrese el texto de la nota: ")
        etiquetas = input("Ingrese las etiquetas: ")
        if texto:
            self.anotador.modificar_nota(id, texto)
        if etiquetas:
            self.anotador.modificar_etiquetas(id, etiquetas)

    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del cÃƒÂ³digo estÃƒÂ¡ fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro mÃƒÂ³dulo, sino ejecutado directamente), entonces llamamos al mÃƒÂ©todo
# ejecutar().
if __name__ == "__main__":
    Menu().ejecutar()
