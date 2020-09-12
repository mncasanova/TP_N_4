#! /usr/bin/env python3
from nota import Nota
class Anotador:
    '''Representa una colecciÃ³n de Notas que se pueden etiquetar, modificar, y
    buscar'''

    def __init__(self):
        '''Inicializa el anotador con una lista vacÃ­a de Notas'''
        self.notas = []

    def nueva_nota(self, texto, etiquetas = ''):
        '''Crea una nueva nota y la agrega a la lista de notas'''
        #TODO: Construir este mÃ©todo.

        nota= Nota(texto, etiquetas)
        self.notas.append(nota)
    def _buscar_por_id(self,id_nota):
        '''Buscar la nota con el id dado'''
        #El "_" al comienzo del nombre del mÃ©todo significa que se pretende que
        #este mÃ©todo sea "privado", es decir, que no se utilice desde fuera de
        #este archivo.

        #TODO: Construir este metodo:
        #Debe retornar la nota con el id dado, o None si no existe dicha nota.

        for nota in self.notas:
            if id_nota == str(nota.id):
                return nota

        return None

    def modificar_nota(self, id_nota, texto):
        '''Busca la nota con el id dado y modifica el texto'''
        # (Este mÃ©todo ya estÃ¡ hecho)
        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.texto = texto
            return True
        return False

    def modificar_etiquetas(self, id_nota, etiquetas):
        '''Busca la nota con el id dado y modifica las etiquetas'''
        #TODO: Construir este metodo, parecido al anterior.

        nota = self._buscar_por_id(id_nota)
        if nota:
            nota.etiquetas = etiquetas
            return True
        return False


    def buscar(self, filtro):
        '''Retorna una lista de todas las notas que coincidan con el filtro
        dado, en el texto o en las etiquetas'''
        #TODO: Construir este metodo. Tener en cuenta que puede retornar una
        # lista vacÃ­a

        resultados=[]
        for nota in self.notas:
            if nota.coincide(filtro):
                resultados.append(nota)

        return resultados