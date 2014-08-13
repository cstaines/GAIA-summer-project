#This program produces configuration files for 30 stars,
#randomly chosen from the RECONS catalogue, with S/N > 100.

#This program is divided into three sections.
#1. Get the 30 stars

import numpy as np
from math import pi, log, floor


#Set the number of stars desired
num_stars = 30

#Seed random number generator
np.random.seed(0)

#Load all of the stars in the RECONS list
with open("sorted_lists/RECONS_sorted_list_period500.txt", "r") as R:
    stars = np.loadtxt(R)

#Identify stars in the list that have S/N < 100
too_low = 0
    
for line in stars[::-1]:
    if line[-1] < 100.0:
        too_low += 1
    else:
        break

#Choose 30 random stars now that we know which stars have S/N > 100
indices = np.random.randint(too_low, size = num_stars)

chosen_stars = []

for i in xrange(num_stars):
    chosen_stars.append(stars[indices[i]])

#2. Get the planetary parameters.
#Create a random number of planets, sampled from a Gaussian distribution, from each star.
#If the result is negative then give that star 0 planets instead
    
dist = np.random.normal(1.0, 2.0, num_stars).astype(int)
n_planets = np.where(dist < 0, np.zeros(num_stars, int), dist) 

           
#Fill an array of the desired size with random numbers between 0 and 1
#These will become the planet parameters
params = np.random.rand(sum(n_planets), 7)

#3. Save the parameters to config files.
for l in xrange(num_stars):
    with open("config_files_2/RECONS_config_file_{0}.cfg".format(l + 1), "w") as fout:
        fout.write("[observations]\nn_obs = 50\n[system]\n")
        fout.write("name = RECONS_gaia_test_{0}\n".format(l + 1))
        #Print stellar distance, stellar mass,
        #astrometric noise and number of planets.
        #Get astrometric noise by dividing signal by signal-to-noise ratio
        fout.write("distance = {0}\n".format(chosen_stars[l][2]))
        fout.write("mass = {0}\n".format(chosen_stars[l][1]))
        fout.write("am_noise = {0}\n".format(1e-6*chosen_stars[l][-2]/chosen_stars[l][-1]))
        fout.write("n_planets = {0}\n".format(n_planets[l]))
        for m in xrange(n_planets[l]):
            fout.write("planet_{0} = ".format(m + 1))
            np.savetxt(fout, np.array([log(365.25*(2 + 3*params[l+m][0])),
                              log(9.542e-4*((0.5 + 1.5*params[l+m][0])/chosen_stars[l][1])),
                              params[l+m][2], 2*pi*params[l+m][3], 2*pi*params[l+m][4],
                              pi*params[l+m][5], 2*pi*params[l+m][6]]).reshape(1, 7), fmt = "%.2f")
        
    








    
