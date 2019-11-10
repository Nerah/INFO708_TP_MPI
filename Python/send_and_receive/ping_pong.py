from mpi4py import MPI
import sys

def main():

    # Le nombre d'echanges entre les processus.
    PING_PONG_LIMIT = 10

    # MPI_COMM_WORLD => le communicateur par defaut.
    comm = MPI.COMM_WORLD
    
    """
     * Determine le rang donne du processus appelant dans
     * le communicateur donne et donne le resultat a la variable myRank.
    """
    world_rank = comm.Get_rank()
    """
     * Determine le nombre de processus associes au
     * communicateur donne et donne le resultat a la variable nbTask.
    """
    world_size = comm.Get_size()

    # On s'attend a ce qu'il y ait au moins 2 processus.
    if world_size != 2:
        sys.stderr.write("World size must be two for {0}".format(sys.argv[0]))

        # Termine l'execution MPI et retourne un erreur.
        comm.abort()

    ping_pong_count = 0
    partner_rank = (world_rank + 1) % 2

    while ping_pong_count < PING_PONG_LIMIT:
        if world_rank == ping_pong_count % 2:
            # Incremente la valeur avant de l'envoyer.
            ping_pong_count += 1
            comm.send(ping_pong_count, dest=partner_rank)
            print("{0} sent and incremented ping_pong_count {1} to {2}".format(world_rank, ping_pong_count, partner_rank))
        else:
            ping_pong_count = comm.recv(source=partner_rank)
            print("{0} sent and incremented ping_pong_count {1} to {2}".format(world_rank, ping_pong_count, partner_rank))
    
    # Termine l'execution de l'environnement MPI.
    MPI.Finalize()

if __name__ == '__main__':
    main()
