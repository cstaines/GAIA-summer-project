#This program computes the autocorrelation of each parameter
#in the .fits files for the 0 planet case
#, to see if the MCMC chain samples can be treated as
#independent

#Run this in the directory containing the .fits files

import pyfits as pf
import numpy as np
import matplotlib.pyplot as plt

def plot_autos(inp_array, name, ind):
    plt.subplot(2, 2, ind+1)
    plt.plot(inp_array[name])
    plt.title(name)
    plt.show()
    
    
autocorrs = []

for i in xrange(30):
    hdus = pf.open('RECONS_0_planets/RECONS_gaia_test_{0}.fits'.format(i+1))
    names = hdus[1].columns.names
    cols = [hdus[1].data.field(col) for col in names]
    cat = np.rec.fromarrays(cols, names=names)

    for col, i in zip(names, range(len(names))):
        autocorrs.append(np.correlate(cat[col], cat[col], mode='full'))
        if i < 4:
            plt.figure(0)
            plt.suptitle('Autocorrelations')
            plot_autos(cat, col, i)
        else:
            plt.figure(1)
            plt.suptitle('Autocorrelations')
            plot_autos(cat, col, i-4)


            
        
        
        


        


    
    
    
    
    
    
    

