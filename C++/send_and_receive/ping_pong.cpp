
// Author: Wes Kendall
// Copyright 2011 www.mpitutorial.com
// This code is provided freely with the tutorials on mpitutorial.com. Feel
// free to modify it for your own use. Any distribution of the code must
// either provide a link to www.mpitutorial.com or keep this header intact.
//
// Un exemple  avec MPI_Send et MPI_Recv.
// Deux processus se renvoient mutuellement un nombre, l'incrémentant
// jusqu'à ce qu'il atteigne une certaine limite.
//
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

    // Le nombre d'échanges entre les processus.
    const int PING_PONG_LIMIT = 10;

    // Initialise l'environnement d'exécution MPI.
    MPI_Init(NULL, NULL);
    
    /*
     * Détermine le rang donné du processus appelant dans
     * le communicateur donné et donne le résultat à la variable myRank.
     * 
     * MPI_COMM_WORLD => le communicateur par défaut.
     * Source: https://www.codingame.com/playgrounds/349/introduction-to-mpi/mpi_comm_world-size-and-ranks
     */
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    /*
     * Détermine le nombre de processus associés au
     * communicateur donné et donne le résultat à la variable nbTask.
     * 
     * MPI_COMM_WORLD => le communicateur par défaut.
     * Source: https://www.codingame.com/playgrounds/349/introduction-to-mpi/mpi_comm_world-size-and-ranks
     */
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // On s'attend à ce qu'il y ait au moins 2 processus.
    if (world_size != 2) {
        fprintf(stderr, "World size must be two for %s\n", argv[0]);

        // Termine l'exécution de l'environnement MPI et retourne une erreur.
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    int ping_pong_count = 0;
    int partner_rank = (world_rank + 1) % 2;

    while (ping_pong_count < PING_PONG_LIMIT) {
        if (world_rank == ping_pong_count % 2) {
            // Incrémente la valeur avant de l'envoyer.
            ping_pong_count++;
            MPI_Send(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD);
            printf("%d sent and incremented ping_pong_count %d to %d\n",
                    world_rank, ping_pong_count, partner_rank);
        } else {
            MPI_Recv(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD,
                    MPI_STATUS_IGNORE);
            printf("%d received ping_pong_count %d from %d\n",
                    world_rank, ping_pong_count, partner_rank);
        }
    }
    // Termine l'exécution de l'environnement MPI.
    MPI_Finalize();
}