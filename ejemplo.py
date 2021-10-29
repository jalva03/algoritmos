# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:09:21 2021

@author: Jerónimo Álvarez
"""

# Desplegar los números de una lista. Mostrar los números que sean 
# divisibles de 5. Si el número es mayor a 150, nos movemos al siguiente
# número. Si el número es mayor a 500, nos detenemos.

lista = [12,75,150,180,145,525,50]

for x in lista:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)