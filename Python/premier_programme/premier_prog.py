from mpi4py import MPI

def main():

    # MPI_COMM_WORLD => le communicateur par defaut.
    comm = MPI.COMM_WORLD
    
    """
     * Determine le rang donne du processus appelant dans
     * le communicateur donne et donne le resultat a la variable myRank.
    """
    rank = comm.Get_rank()
    """
     * Determine le nombre de processus associes au
     * communicateur donne et donne le resultat a la variable nbTask.
    """
    size = comm.Get_size()
    print("I am task " + str(rank) + " out of " + str(size))


if __name__ == '__main__':
    main()
