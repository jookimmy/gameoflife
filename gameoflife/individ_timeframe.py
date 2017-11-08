import numpy as np
import matplotlib.pyplot as plt

pentadecathlon = np.zeros( ( 24,24 ) )
pentadecathlon[ 10:20,10 ] = 1
pentadecathlon[ 12, 9 ] = 1
pentadecathlon[ 12,10 ] = 0
pentadecathlon[ 12,11 ] = 1
pentadecathlon[ 17, 9 ] = 1
pentadecathlon[ 17,10 ] = 0
pentadecathlon[ 17,11 ] = 1

pd_time = np.zeros((24,24))
evoln = pentadecathlon[ : ]
nt = 30
for t in range(nt):
    evoln = evolve(evoln)    # evolve the system forward in `evoln`
    pd_time += evoln
plt.imshow( pd_time )
plt.show()