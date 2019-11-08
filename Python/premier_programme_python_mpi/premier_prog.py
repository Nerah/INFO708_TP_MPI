from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD  #comunicateur avec des valeurs par default
    rank = comm.Get_rank()
    size = comm.Get_size()
    print("hello from " + str(rank) + " in " + str(size))


if __name__ == '__main__':
    main()
