#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

int main ( int argc , char * argv[] )
{
    int nbTask ;
    int myRank;

    // Initialise l'environnement d'exécution MPI.
    MPI_Init ( &argc , &argv ) ;

    /*
     * Détermine le nombre de processus associés au
     * communicateur donné et donne le résultat à la variable nbTask.
     * 
     * MPI_COMM_WORLD => le communicateur par défaut.
     * Source: https://www.codingame.com/playgrounds/349/introduction-to-mpi/mpi_comm_world-size-and-ranks
     */
    MPI_Comm_size( MPI_COMM_WORLD, &nbTask ) ;
    /*
     * Détermine le rang donné du processus appelant dans
     * le communicateur donné et donne le résultat à la variable myRank.
     * 
     * MPI_COMM_WORLD => le communicateur par défaut.
     * Source: https://www.codingame.com/playgrounds/349/introduction-to-mpi/mpi_comm_world-size-and-ranks
     */
    MPI_Comm_rank( MPI_COMM_WORLD, &myRank) ;

    printf( "I am task %d out o f %d\n", myRank, nbTask ) ;
    
    // Termine l'exécution de l'environnement MPI.
    MPI_Finalize();
    
    return 0;
}