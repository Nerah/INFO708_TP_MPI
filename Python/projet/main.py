from mpi4py import MPI
import time

class Feu:
    
    def __init__(self): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""
        self.nom = "Dupont"
        self.couleur = "rouge"

def main():

    # MPI_COMM_WORLD => le communicateur par defaut.
    comm = MPI.COMM_WORLD
    feu1  = Feu("feu1","rouge")
    feu2  = Feu2("feu2","rouge")
    """
     * Determine le rang donne du processus appelant dans
     * le communicateur donne et donne le resultat a la variable myRank.
    """
    rank = comm.Get_rank()
    if (rank == 0):        
        print ("feu 1 : vert")
        
        time.sleep(5)
        print("feu 1 : orange")
        time.sleep(2)
        print("feu 1 : rouge")
        
        print("feu 2 : vert")
        time.sleep(5)
        print("feu 2 : orange")
        time.sleep(2)
        print("feu 2 : rouge")1
        
if (rank == 1):
    print("je sui le feu 1 ")
    

if (rank == 2):
    print("je suis le feu 2")
    """
     * Determine le nombre de processus associes au
     * communicateur donne et donne le resultat a la variable nbTask.
    """
    size = comm.Get_size()

    # Termine l'execution de l'environnement MPI.
    MPI.Finalize()

if __name__ == '__main__':
    main()
