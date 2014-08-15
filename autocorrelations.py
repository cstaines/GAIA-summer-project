#This function generates and plots the autocorrelation function
#for each parameter, for each star, for the 0 planet MCMC.

#Use this in the 'GAIA-summer-project' directory.

import pandas.tools.plotting as ptp
import matplotlib.pyplot as plt
import pyfits as pf
import numpy as np

for i in xrange(30):
    
    #Open the .fits file and store the data as a numpy record array
    hdus = pf.open('RECONS_0_planets/RECONS_gaia_test_{0}.fits'.format(i+1))
    names = hdus[1].columns.names
    cols = [hdus[1].data.field(col) for col in names]
    cat = np.rec.fromarrays(cols, names=names)

    #Plot the autocorrelation of each column and save
    for col in names:
        plt.figure()
        plt.suptitle('Autocorrelation function of '+col+'for RECONS star{0}'.format(i+1))
        ptp.autocorrelation_plot(cat[col])
        plt.savefig('autocorrelations/star{0}/autocorr_'.format(i+1)+col+'.pdf')

