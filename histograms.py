#This script takes the planetary parameters for the cases of 1 or more
#planets, and generates a histogram for each parameter.

import matplotlib.pyplot as plt
import pyfits as pf
import numpy as np

max_planets = 3 #Highest number of planets in .fits file

for i in xrange(30):

    #Open the files
    hdus = pf.open('RECONS_gaia_tests/RECONS_gaia_test_{0}.fits'.format(i+1))
    
    for n_planets in range(1, max_planets+1): #Run until all n_planets processed
        hdu = hdus[n_planets+1]

        #Create the list that tells which fields to use
        names = hdu.columns.names[9:]

        #Plot the histograms
        for c in names:
            plt.figure()
            plt.suptitle('Histogram of '+c+', star {0}, {1} planet(s)'.format(i+1, n_planets))
            plt.hist(np.array(hdu.data[c]), 20, normed = True)
            plt.xlabel(c)
            plt.ylabel('Sample probability')
            plt.savefig('histograms/star{0}/n_planets{1}/histogram_'.format(i+1, n_planets)+c+'.pdf')
            plt.close()

    hdus.close()
            
                             

