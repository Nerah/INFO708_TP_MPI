# MPI-2

## Pour bien débuter avec C++

### Introduction

Dépendance LINUX à télécharger pour compiler du C++ utilisant MPI:
> `sudo apt install libopenmpi-dev`

Accéder au dossier premier_programme_c++:
> `cd premier_programme_c++_mpi`

Compiler un programme MPI:
> `mpiCC -o main main.cpp`

Lancer l'exécutable:
> `./main`

### Automatisation

Nous avons un fichier [run.py](run.py) dans la racine du projet.
Il a pour objectif de générer la commande mpirun, qui lance
un programme MPI dans un environnement composé d'un communicateur
et de ses processus. Il s'occupe également de générer les exécutables des programmes, and utilisant la commande make.
Il est donc nécessaire de créer un makefile dans chacun de nos dossiers. On précise l'emplacement et le nom de l'exécutable pour chacun de nos programmes MPI dans le dictionnaire "programs".

#### Exemple avec un programme C++

On va reprendre l'exemple du programme [ping_pong](C++\send_and_receive).

- On a créé un fichier [ping_pong.cpp](C++\send_and_receive\ping_pong.cpp).
- On a créé un [makefile](C++\send_and_receive\makefile).
- On a ajouté les informations associées à ce dossier dans [run.py](run.py), dans programs.
- On exécute [run.py](run.py): `./run.py ping_pong`