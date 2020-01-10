from mpi4py import MPI
import time
import random

class Feu:
    nom = ""
    couleur = ""
    def __init__(self,nom,couleur):
        self._nom = nom
        self._couleur = couleur

    def get_nom(self): 
        return self._nom 
      
     
    def set_nom(self, x): 
        self._nom = x

    def get_couleur(self): 
        return self._couleur
      
    def set_couleur(self, x): 
        self._couleur = x 


feu1  = Feu("feu1","rouge")

feu2  = Feu("feu2","vert")

listeVoiture1 = ["voiture 1", "voiture 2", "moto 1", "voiture 3", "voiture 4", "voiture 5", "moto2", "voiture 6"]
listeVoiture2 = ["voiture 1", "voiture 2", "voiture 3"]


def main():

    comm = MPI.COMM_WORLD


    rank = comm.Get_rank()

    if rank == 0:
        print("le feu : " + feu1.get_nom() + " et de couleurs :  " + feu1.get_couleur())
        print("le feu : " + feu2.get_nom() + " et de couleurs :  " + feu2.get_couleur())
        time.sleep(5)

        while 1 :
            req1 = comm.isend(1, dest=2, tag=11)  # feu 2 orange
            req1.wait()
            time.sleep(2)
            req1 = comm.isend(0, dest=2, tag=11)  # feu 2 rouge
            req1.wait()
            time.sleep(1)
            req = comm.isend(2, dest=1, tag=11) #feu 1 vert
            req.wait()
            time.sleep(1)

            req = comm.isend(1, dest=3, tag=1) #voiture 1
            req.wait()
            time.sleep(3)

            req = comm.isend(1, dest=3, tag=1) #voiture 1
            req.wait()
            time.sleep(2)

            req = comm.isend(1, dest=3, tag=1) #voiture 1
            req.wait()
            time.sleep(1)




            req =comm.isend(1, dest=1, tag=11) #feu 1 orange
            req.wait()

            time.sleep(1)

            req = comm.isend(1, dest=3, tag=1) #voiture 1
            req.wait()

            time.sleep(2)
            req = comm.isend(0, dest=1, tag=11) #feu1 rouge
            req.wait()

            time.sleep(1)

            req1 = comm.isend(2, dest=2, tag=11)  # feu 2 vert
            req1.wait()
            time.sleep(1)

            req = comm.isend(1, dest=4, tag=2)  # voiture 1
            req.wait()
            time.sleep(3)

            req = comm.isend(1, dest=4, tag=2)  # voiture 1
            req.wait()
            time.sleep(2)

            req = comm.isend(1, dest=4, tag=2)  # voiture 1
            req.wait()
            time.sleep(1)



        
    if rank == 1:
        while 1:
            req = comm.irecv(source=0, tag=11)
            data = req.wait()

            if data == 0:
                feu1.set_couleur("rouge")
                print(feu1.get_nom() + " couleurs :  " + feu1.get_couleur())

                req = comm.isend(0, dest=3, tag=3)  # feu 2 vert
                req.wait()

            if data == 1:
                feu1.set_couleur("orange")
                print(feu1.get_nom() + " couleurs :  " + feu1.get_couleur())

            if data == 2:
                feu1.set_couleur("vert")
                print(feu1.get_nom() + " couleurs :  " + feu1.get_couleur())
                req = comm.isend(1, dest=3, tag=3)  # feu 2 vert
                req.wait()

        print( "fin")


    if rank == 2:
        while 1:
            req = comm.irecv(source=0, tag=11)
            data = req.wait()
            if data == 0:
                feu2.set_couleur("rouge")
            if data == 1:
                feu2.set_couleur("orange")
            if data == 2:
                feu2.set_couleur("vert")
            print(feu2.get_nom() + " couleurs :  " + feu2.get_couleur())

    if rank == 3:
        while 1:
            req = comm.irecv(source=0, tag=1)
            data = req.wait()
            if len(listeVoiture1)!=0:
                print(" le vehicule ,feu 1 " + listeVoiture1[0] + " passe ")
                del listeVoiture1[0]
            else :
                print("pas de voiture au feu")

    if rank == 4:
        while 1:
            req = comm.irecv(source=0, tag=2)
            data = req.wait()
            if len(listeVoiture2) != 0:
                print("le vehicule ,feu 2 " + listeVoiture2[0] + " passe ")
                del listeVoiture2[0]
            else:
                print("pas de voiture au feu2")

    '''if rank == 5:
        i = 7;
        j = 4;
        while 1:
            listeVoiture1.append("voiture " + str(i))
            print("la voiture , voiture " + str(i) + " arrive au feu 1")
            time.sleep(i)
            i = i + 1
            listeVoiture2.append("voiture " + str(j))
            print("la voiture , voiture " + str(j) + " arrive au feu 2")

            time.sleep(j)
            j = j + 1
        '''
    MPI.Finalize()

if __name__ == '__main__':
    main()
