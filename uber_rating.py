#Uber rate finder
from __future__ import division
"""
Tengo un 4.82 de media en Uber.
Tengo 21 viajes, 1 de ellos cancelado.
Que posibles notas me han puesto y cuantos Uber he tenido?
"""

for a in range(0, 23):
    for b in range(0, 23):
        for c in range (0, 23):
            for d in range (0, 23):
                for e in range (0, 23):
                    for f in range(1, 23):
                        res = (a*0+b*1+c*2+d*3+e*4+f*5)/(b+c+d+e+f)
                        if ((a+b+c+d+e+f) == 20  or (a+b+c+d+e+f) == 21) and res >= 4.815 and res <= 4.824 and a < 5 and b == 0 and c == 0:
                            print("Ubers: " + str(a+b+c+d+e+f) + " (" + str(a) + ", " + str(b) + ", " + str(c) + ", " + str(d) + ", " + str(e) + ", " + str(f)) + ") --> " + str(res)