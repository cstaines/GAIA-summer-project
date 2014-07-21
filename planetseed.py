#This program assigns a random value
#for orbital parameters of planets
#orbiting each chosen RECONS star
import random as r
import numpy as np
from math import pi

#Have 30 stars to do this for, so initialise
#Declare number of planets
n_planets = 1
params = np.zeros((30*n_planets, 7), float)

for l in xrange(30):
    for m in xrange(n_planets):
        #Period, in years
        P = r.uniform(2.0, 5.0)

        #Planet mass, in Jupiter masses
        M_p = r.uniform(0.5, 2.0)

        #Eccentricity
        e = r.random()

        #Argument of periastron
        w = r.uniform(0, 2*pi)

        #Omega - defined to be 0 if w is 0
        omega = r.uniform(0, 2*pi) if abs(w) > 1e-6 else 0.0

        #Inclination
        i = r.uniform(0, pi)

        #Initial mean anomaly
        M0 = r.uniform(0, 2*pi)

        params[l + m] = [P, M_p, e, w, omega, i, M0]

#Save to file
with open("seeds/RECONS_planet_parameters.txt", "w") as f:
    np.savetxt(f, params)







