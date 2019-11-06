#!/usr/bin/python
import sys
import os
import subprocess

# Genere la commande mpirun pour lancer un programme donne

# La liste des programmes ( <executable> : (<emplacement>, <nb_processus_a_lancer>) )
programs = {
    'ping_pong': ('C++/send_and_receive', 2),
}

program_to_run = sys.argv[1] if len(sys.argv) > 1 else None
if not program_to_run in programs:
    print('Must enter program name to run. Possible programs are: {0}'.format(programs.keys()))
else:
    # Genere l'executable du programme a lancer
    with open(os.devnull, 'wb') as devnull:
        subprocess.call(
            ['cd ./{0}/ && make'.format(programs[program_to_run][0])],
            stdout=devnull, stderr=subprocess.STDOUT, shell=True)

    mpirun = os.environ.get('MPIRUN', 'mpirun')
    hosts = '' if not os.environ.get('MPI_HOSTS') else '-f {0}'.format(os.environ.get('MPI_HOSTS'))

    # Generation de la commande qui sera executee sur la console

    sys_call = '{0} --allow-run-as-root -n {1} {2} ./{3}/{4}'.format(
        mpirun, programs[program_to_run][1], hosts, programs[program_to_run][0], program_to_run)

    if len(programs[program_to_run]) > 2:
        sys_call = '{0} {1}'.format(sys_call, ' '.join(programs[program_to_run][2]))

    print(sys_call)
    subprocess.call([sys_call], shell=True)