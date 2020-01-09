from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
data = 0;
if rank == 0:
    data = {'a': 1, 'b': 3.14}
    data2 = {'a': 2, 'b': 6.14}
    data3 = {'a': 3, 'b': 9.14}
    data4 = {'a': 4, 'b': 12.14}
    comm.isend(data, dest=1, tag=11)
    comm.isend(data2, dest=2, tag=11)
    comm.isend(data3, dest=3, tag=11)
    req = comm.isend(data4, dest=4, tag=11)

    req.wait()
    print("fin envoie")
else:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print("mon processus est ")
    print(rank)
    print(data)
   
