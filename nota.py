#! /usr/bin/env python3
import datetime

#Guardamos en una variable la prÃƒÂ³xima id disponible:
ultima_id = 0

class Nota:
    '''Representa una nota en el anotador. Tiene texto, etiquetas (separadas
    por espacios) y se puede buscar por texto'''
    def __init__(self, texto, etiquetas=''):
        '''Inicializa la nota con un texto, y opcionalmente, con etiquetas
        separadas por espacios. AutomÃƒÂ¡ticamente define fecha de creaciÃƒÂ³n e id'''
        self.texto = texto
        self.etiquetas = etiquetas
        self.fecha_creacion = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id

    def coincide(self, filtro):
        '''Determina si la nota coincide con el filtro de bÃƒÂºsqueda. Retorna
        True si es asÃƒÂ­ y False de lo contrario

        Busca tanto en el texto como en las etiquetas y distingue mayÃƒÂºsculas de
        minÃƒÂºsculas '''

        return filtro in self.texto or filtro in self.etiquetas

        #TODO: Construir este mÃƒÂ©todo
        # Recordatorio para buscar en una cadena:
        # if {subcadena} in {cadena}:
        # Ej:
        # if 'ten' in 'entretenido':  ---> sale por True
        # if 'blabla' in 'entretenido': ---> sale por False






