#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

int main ( int argc , char * argv[] )
{
    int nbTask ;
    int myRank;

    MPI_Init ( &argc , &argv ) ;

    MPI_Comm_size( MPI_COMM_WORLD, &nbTask ) ;
    MPI_Comm_rank( MPI_COMM_WORLD, &myRank) ;
    printf( "I am task %d out o f %d\n", myRank, nbTask ) ;
    MPI_Finalize();
    
    return 0;
}