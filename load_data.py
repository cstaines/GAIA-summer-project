#Contains a function with which to load data and get the field names
#Borrows heavily from oas.planetsearch

import pyfits as pf

def ldwn(fname, nplanets): #Load data with names
    hdul = pf.open(fname, nplanets)
    hdu = hdul[nplanets+1]
    names = hdu.columns.names[1:]
    npop = hdu.header['pop_size']
    npar = hdu.header['tfields'] - 1
    ll = hdu.data['lnprob'].reshape([npop,-1])
    ch = np.array([hdu.data[c] for c in names]).T.reshape([npop, -1, npar])
    hdul.close()
    return names, ll, ch
    
    
