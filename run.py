#!/usr/bin/python
import sys
import os
import subprocess

# Commande: ./run.py <langage = python | c++> <programme>

# Genere la commande mpirun pour lancer un programme donne

# La liste des programmes ( <executable> : (<emplacement>, <nb_processus_a_lancer>) )
programs = {
    "c++" : {
        'premier_prog': ('C++/premier_programme', 5),
        'ping_pong': ('C++/send_and_receive', 2),
        'broadcast_prog':('C++/Broadcast',5)
    },
    "python" : {
        'premier_prog': ('Python/premier_programme', 5),
        'ping_pong': ('Python/send_and_receive', 2),
        'broadcast_prog':('Python/BroadCast', 5),
        'scattering_prog':('Python/Scattering', 5),
        'point':('Python/point_to_point', 5),
        'main':('Python/projet', 3),
        'reduction_prog':('Python/Reduction', 5),
        'gathering_prog':('Python/Gathering', 5)
    }
}

langage = sys.argv[1] if len(sys.argv) > 1 else sys.exit('Must enter langage name followed by program name to run. Possible langages are: {0}'.format(programs.keys()))
program_to_run = sys.argv[2] if len(sys.argv) > 2 else sys.exit('Must enter langage name followed by program name to run. Possible programs in {0} are: {1}'.format(langage, programs[langage].keys()))

if not langage in programs:
    print('Must enter langage name to run. Possible langages are: {0}'.format(programs.keys()))
if not program_to_run in programs[langage]:
    print('Must enter program name to run. Possible programs are: {0}'.format(programs[langage].keys()))
else:

    mpirun = os.environ.get('MPIRUN', 'mpirun')
    hosts = '' if not os.environ.get('MPI_HOSTS') else '-f {0}'.format(os.environ.get('MPI_HOSTS'))

    if langage == "c++":

        # Genere l'executable du programme a lancer
        with open(os.devnull, 'wb') as devnull:
            subprocess.call(
                ['cd ./{0}/ && make'.format(programs[langage][program_to_run][0])],
                stdout=devnull, stderr=subprocess.STDOUT, shell=True)
            print("L'executable {0} a ete genere.".format(programs[langage][program_to_run][0] + '/' + program_to_run))

        sys_call = '{0} --allow-run-as-root -n {1} {2} ./{3}/{4}'.format(
            mpirun, programs[langage][program_to_run][1], hosts, programs[langage][program_to_run][0], program_to_run)

    elif langage == "python":

        sys_call = '{0} --allow-run-as-root -n {1} {2} python ./{3}/{4}.py'.format(
            mpirun, programs[langage][program_to_run][1], hosts, programs[langage][program_to_run][0], program_to_run)

    # Lance la commande generee sur la console
    if len(programs[langage][program_to_run]) > 2:
        sys_call = '{0} {1}'.format(sys_call, ' '.join(programs[langage][program_to_run][2]))

    print(sys_call)
    subprocess.call([sys_call], shell=True)
