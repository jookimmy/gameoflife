import numpy as np
def evolve( array ):
    nx,ny = len(array),len(array)  # the shape of the input array

    neighbor_array = np.zeros(shape=(nx,ny))  # should be zeros the same size as the input array
    evolved_array = np.zeros(shape=(nx,ny),dtype = np.int64)  # should be zeros the same size as the input array, dtype of np.int64

    for ix in range( 0,nx ):    # loop over all x-values
        for iy in range(0,ny):          # loop over all y-values
            lx,rx = ix-1,ix+1   # define the left and right neighbor indices
            uy,dy = iy+1,iy-1        # define the top and bottom neighbor indices
            lx %= nx            # normalize the indices to fall in [0,nx)
            rx %= nx            # do this for the other three neighbor indices
            uy %= ny
            dy %= ny

            # include all eight neighboring cells in an array and sum it up
            neighbors = [ array[ lx,iy ],array[ rx,iy ],array[ ix,uy ],array[ix,dy],array[lx,uy],array[lx,dy],array[rx,uy],array[rx,dy]]
            neighbor_array[ ix,iy ] = sum( neighbors )

            # handle the case where the current cell is alive and has two neighbors
            if array[ ix,iy ] > 0 and neighbor_array[ ix,iy ] == 2:
                evolved_array[ ix,iy ] = 1
            # handle the case where the current cell has three neighbors
            elif array[ix,iy] >= 0 and neighbor_array[ix,iy] == 3
                evolved_array[ ix,iy ] = 1
            # otherwise the cell is dead
            elif array[ ix,iy] and neighbor_array[ix,iy] > 3
                evolved_array[ ix,iy ] = 0

    return evolved_array