#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# crea la clase Sistema jerarquico.
class SistemaJerarquico(object):
    def __init__(self,lista_estrellas):
        self.lista_estrellas = lista_estrellas
# funcion que imprime los nombres de las estrellas seguidos de la lista ordenada de letras del alfabeto.     
    def Lista_alfabeto(self):
        alfabeto='ABCDEFGHIJKLMNÑOPQRSTWXYZ'
        for i in range(len(self.lista_estrellas)):
            estrella_letra = self.lista_estrellas[i]+alfabeto[i]
        return str(estrella_letra)
# funcion que devuelve la lista de estrellas ordenada por masa.
    def Lista_ordenada(self):
        self.lista_estrellas.sort(key=lambda Estrella: Estrella._masa)
        nombre_estrellas = [Estrella.nombre for Estrella in self.lista_estrellas]
        return nombre_estrellas
        

