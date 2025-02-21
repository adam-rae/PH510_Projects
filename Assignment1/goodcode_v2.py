#!/usr/bin/env python3
import numpy as np
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD

nworkers = comm.Get_size()
# Equality; everyone works equally

# samples
N = 100000000
delta = 1/(N - nworkers) #1 point per worker is removed to account for the removed final points in line 26

# integral
integral = np.array(0.0, dtype=np.float64)

def integrand(x):
  return(4.0 / (1.0 + x*x))

#Initialising
rank = comm.Get_rank()
worker_sum = 0
startTime = time.time()

for x in np.linspace(rank/nworkers, (rank+1)/nworkers, int(N/nworkers))[:-1]:
    worker_sum += integrand(x + delta/2) * delta

message = np.array(worker_sum, dtype=np.float64)

#Allreduce method
comm.Allreduce(message, integral, MPI.SUM)

endTime = time.time()

if rank == 0:
    print("Pi value: %.15f" % integral)
    print("Time:", endTime-startTime)
