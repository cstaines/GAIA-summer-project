#This program takes the stars sampled in 'starseed.py'
#and the planet parameters generated in 'planetseed.py'
#and produces configuration files ready for Hannu's code to run
from math import log
import numpy as np

#Get star & planet data
with open("seeds/RECONS_stars.txt", "r") as f1:
    stars = np.loadtxt(f1)

with open("seeds/RECONS_planet_parameters.txt", "r") as f2:
    planets = np.loadtxt(f2)

#Compute log of period (days), log of mass ratio, and the planetary parameters calculated earlier
for l in xrange(30):
    with open("config_files/RECONS_config_file_{0}.cfg".format(l + 1), "w") as fout:
        fout.write("[observations]\nn_obs = 50\n[system]\n")
        fout.write("name = RECONS_gaia_test_{0}\n".format(l + 1))
        fout.write("n_planets = 1\nplanet = ")
        config_array = np.array([log(365.25*planets[l][0]), log((9.542e-4)*planets[l][1]/stars[l][1]),
                    planets[l][2], planets[l][3], planets[l][4], planets[l][5], planets[l][6]])
        np.savetxt(fout, config_array.reshape(1, 7), fmt = "%.2f")
                
        
        
                

