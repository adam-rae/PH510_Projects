#!/usr/bin/env python3
"""
Module for the calculation of pi by an integration process. Making use of
multi-core parallelisation for improvements in timing.

MIT License

Copyright (c) 2025 Adam John Rae

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD

nworkers = comm.Get_size()

# samples
N = 100000000
delta = 1/(N - nworkers)
#1 point per worker is removed to account for the removed final points in line 64

def integrand(x):
    """
    The function we are integrating.

    Parameters
    ----------
    x : float
        The value at which the function is evaluated.

    Returns
    -------
    float
        f(x) = 4.0 / (1.0 + x*x)

    """
    return 4.0 / (1.0 + x*x)

# integral
integral = np.array(0.0, dtype=np.float64)

#Initialising
rank = comm.Get_rank()
WORKER_SUM = 0
startTime = time.time()

for x_var in np.linspace(rank/nworkers, (rank+1)/nworkers, int(N/nworkers))[:-1]:
    WORKER_SUM += integrand(x_var + delta/2) * delta

message = np.array(WORKER_SUM, dtype=np.float64)

#Allreduce method
comm.Allreduce(message, integral, MPI.SUM)

endTime = time.time()

if rank == 0:
    print(f"Pi value for {nworkers} cores: %.15f" % integral)
    print("Time:", endTime-startTime)
