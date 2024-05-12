#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# crea la clase planeta.
class Planeta(object):
    def __init__(self,estrella_anfitriona,masa_pl,radio_pl,radio_mayor,inclinacion,exentricidad,argumento_periaston):
        
        self._estrella_anfitriona = estrella_anfitriona
        self._masa_pl = float(masa_pl)
        self._radio_pl = float(radio_pl)
        self._radio_mayor = float(radio_mayor)
        self._inclinacion = float(inclinacion)
        self._exentricidad = float(exentricidad)
        self._argumento_periaston = float(argumento_periaston)
# funcion que devuelve el periodo de rotacion kepleriana con la formula dada en clase.     
    def Periodo_de_rotacion(self):
        PR=2*np.pi*(np.sqrt((self._radio_mayor**3)/(G*self._masa_pl)))
        if PR > 0:
            return PR
        else:
            return 'faltan datos para calcular la funcion'
#funcion que devuelve la densidad planetaria
    def Densidad_planetaria(self):
        V=(4/3)*np.pi*(self._radio_pl^3)
        return self._masa_pl/V

