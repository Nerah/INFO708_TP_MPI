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
Il est donc nécessaire de créer un makefile dans chacun de nos dossiers. On précise l'emplacement et le nom de l'exécutable pour chacun de nos programmes MPI dans le dictionnaire "programs", pour le langage C++.

#### Exemple avec un programme C++

On va reprendre l'exemple du programme [ping_pong](C++/send_and_receive).

- On a créé un fichier [ping_pong.cpp](C++/send_and_receive/ping_pong.cpp).
- On a créé un [makefile](C++/send_and_receive/makefile).
- On a ajouté les informations associées à ce dossier dans [run.py](run.py), dans programs, pour le langage C++.
- On exécute [run.py](run.py): `./run.py c++ ping_pong`

## Pour bien débuter avec Python

### Introduction

MPI ne propose pas de commande pour compiler un programme Python dans l'environnement MPI comme avec C++. Les seules commandes à notre disposition pour exécuter un programme Python sont: mpirun et mpiexec. Ceci explique pourquoi aucun makefile n'est utilisé. Le fichier [run.py](run.py) se chargera donc simplement d'appeler mpirun.

#### Exemple avec un programme Python

On va reprendre l'exemple du programme [premier_prog](Python/premier_programme_python_mpi).

- On a créé un fichier [premier_prog.py](Python/premier_programme_python_mpi/premier_prog.py).
- On a ajouté les informations associées à ce dossier dans [run.py](run.py), dans programs, pour le langage Python.
- On exécute [run.py](run.py): `./run.py python premier_prog`