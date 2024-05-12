#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# constantes que se van a utilizar.
Lsol= 3.828e26 
Msol= 1 #en la biblioteca de exoplanetas que nos dio el profe estaba en masas solares.
G = 6.672e-11
Rsol=7e5
# crea la clase estrella.
class Estrella(object):
   
    def __init__(self,nombre,masa,radio,temperatura,distancia,vx,vy):
       
        self.nombre = nombre
        self._masa =  masa
        self._radio = radio
        self._temperatura = temperatura
        self._distancia = distancia
        self._movimiento = np.array([vx,vy])
# funcion de la  luminsidad con la formula dada en clases.
    def Luminosidad (self):
        LM=float(4*np.pi*(self._radio**2)*self._temperatura)
        if LM > 0:
            return LM
        else:
            return 'faltan datos para calcular la funcion'
        
        
# funcion de la luminosidad de la secuencia principal con la formula dada en clases.  
    def Luminosidad_principal(self):
        LM_P=float(Lsol*((self._masa/Msol)**3.5))
        if LM_P > 0:
            return LM_P
        else:
            return 'faltan datos para calcular la funcion'

        