#This function generates and plots the autocorrelation function
#for each parameter, for each star, for the 0 planet MCMC.

import pandas.tools.plotting as ptp
import matplotlib.pyplot as plt
import pyfits as pf
import numpy as np

#I was going to use oas.planetsearch's load_results function,
#but it doesn't keep the header names...

for i in xrange(30):
    
    #Open the .fits file and store the data as a numpy array
    #All lines except for the third below are from the aforementioned load_results function
    hdus = pf.open('RECONS_0_planets/RECONS_gaia_test_{0}.fits'.format(i+1))
    hdu = hdus[1]
    names = hdu.columns.names[1:]
    npop = hdu.header['pop_size']
    npar = hdu.header['tfields'] - 1

    #Get the parameters
    ch = np.array([hdu.data[c] for c in hdu.columns.names[1:]]).T.reshape([npop, -1, npar])

    hdus.close()

    #4000 walkers - choose every 200th
    wlkrs  = ch[::200]
    counter = 0 #Might be a bit quicker than using 'index' function

    #Plot the autocorrelation of each column and save
    for l in wlkrs:
        for j in xrange(8):
            plt.figure()
            plt.suptitle('Autocorrelation function of '+names[j]+', walker {0}, RECONS star{1}'.format(counter+1, i+1))
            ptp.autocorrelation_plot(l[:,j])
            plt.savefig('autocorrelations/star{0}/walker{1}/autocorr_'.format(i+1,counter+1)+names[j]+'.pdf')
            plt.close()
        counter += 20

