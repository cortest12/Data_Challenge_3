#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# crea la clase exoplaneta que hereda de la clase planeta.
class Exoplaneta(Planeta):
    def __init__(self,estrella_anfitriona,masa_pl,radio_pl,radio_mayor,inclinacion,exentricidad,argumento_periaston,metodo_de_descubrimiento,numero_estrellas,nombre_pl):
        super().__init__(estrella_anfitriona,masa_pl,radio_pl,radio_mayor,inclinacion,exentricidad,argumento_periaston)
        self._metodo_de_descubrimiento = metodo_de_descubrimiento
        self._numero_estrellas = numero_estrellas
        self._nombre_pl = nombre_pl
# funcion que devuelve el metodo de descubrimiento y si el mismo es trasito nos entrega su parametro de impacto.
    def Metodo_descubrimiento(self):
        if self._metodo_de_descubrimiento.lower() == 'primary transit':
            
            b = self._radio_mayor*np.cos(self._inclinacion)*((1-self._exentricidad**2)/(self._radio_pl*(1+self._exentricidad*np.sin(self._argumento_periaston))))
            
            if b >= 0:
                return f'El metodo de descubrimiento es transito y su parametro de impacto es:{b}.'
            else:
                return 'El metodo de descubrimiento es transito pero falta un atributo del exoplaneta para detectar el parametro de impacto'
        
        elif self._metodo_de_descubrimiento.lower() == 'radial velocity':
            
            return 'El metodo de descubrimiento es velocidad radial.'
        
        elif self._metodo_de_descubrimiento.lower() == 'imaging':
        
            return 'El metodo de descubrimiento es imagen directa.'
        
        else:
            return 'El metodo de descubrimiento no es transito, velocidad radial ni imagen directa o esta mal escrito.'
# funcion que devuelve la similitud del exoplaneta con Tatooin (dependiendo del numero de estrellas).
    def Similitud_Tatooin(self):
        if self._numero_estrellas > 1 :
            return 'Es similar a Tatooin'
        else:
            return 'No es similar a Tatooin'
# funcion que devuelve la masa del exoplaneta en masas terrestres
    def masa_en_masas_terrestres(self):
        return (self._masa_pl*317.83)

