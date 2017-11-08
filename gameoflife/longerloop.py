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

pd_list = [pentadecathlon]
nt = 30
for t in range(0,nt ):
    evolved = evolve(pd_list[-1])     # evolve the simulation and append it to `pd_list`
    pd_list.append(evolved)
    plt.imshow( pd_list[ -1 ] )
plt.show()