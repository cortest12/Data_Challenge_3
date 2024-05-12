#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# crea la clase Sistema Planetario
class SistemaPlanetario(object):
    def __init__(self,lista_planetas):
        self.lista_planetas = lista_planetas
# funcion que devuelve el numero de planetas que hay dentro del sistema planetario.       
    def N_de_planetas(self):
        return int(len(self.lista_planetas))
# funcion que ordena los exoplanetas por el radio semi mayor de la orbita, usando .sort para ordenar junto con una funcion lambda,    
    def Lista_pl_ordenada(self):
        self.lista_planetas.sort(key=lambda Exoplaneta: Exoplaneta._radio_mayor)
        nombres_ordenados = [Exoplaneta._nombre_pl for Exoplaneta in self.lista_planetas]
        return nombres_ordenados

