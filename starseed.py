#This program reads the sorted RECONS list
#and chooses 30 stars at random from those with
#S/N > 100 (log10(S/N) > 2)
import random as r
import numpy as np


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

#Choose 30 random stars now that all of the stars have S/N > 100
chosen_stars = r.sample(stars[:-too_low], 30)

#Print the chosen stars to file
with open("seeds/RECONS_stars.txt", "w") as f:
    np.savetxt(f, chosen_stars)

    
