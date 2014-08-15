#This program computes the autocorrelation of each parameter
#in the .fits files for the 0 planet case,
#to see if the MCMC chain samples can be treated as
#independent

#Run this in the directory containing the .fits files

import pyfits as pf
import numpy as np
import matplotlib.pyplot as plt
from math import floor

#Show figure on-screen if true; otherwise save as pdf (time-consuming)
show = True

for i in xrange(30):
    hdus = pf.open('RECONS_0_planets/RECONS_gaia_test_{0}.fits'.format(i+1))
    names = hdus[1].columns.names
    cols = [hdus[1].data.field(col) for col in names]
    cat = np.rec.fromarrays(cols, names=names)

    j = 0
    autocorrs = []
    
    for col in names:
        autocorrs.append(np.correlate(cat[col], cat[col], mode='full'))

        if j % 4 == 0:
            plt.figure(1+int(floor(j/4)))
            plt.suptitle('Autocorrelations')
            
        plt.subplot(2, 2, 1+(j%4))
        plt.plot(autocorrs[-1])
        plt.xticks([0, 80000, 160000])
        plt.title(col)

        if j in [3, 7, 8]:
            if show:
                plt.show()
            else:
                plt.savefig('autocorrelations/star{0}/autocorrs_{1}.ps'.format(i+1, 1+int(floor(j/4))))
        
        j += 1


            
        
        
        


        


    
    
    
    
    
    
    

