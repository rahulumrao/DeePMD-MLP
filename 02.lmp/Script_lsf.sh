#!/bin/bash
#BSUB -n 12		# number of processor
#BSUB -W 02:00		# wall clock time
#BSUB -q short #single_chassis	# Queue Name
#BSUB -J Train_btd 	# Name of job
#BSUB -R span[hosts=1] 	# Name of job
#BSUB -o stdout.%J	# standard out
#BSUB -e stderr.%J	# standatd error

source /usr/share/Modules/init/bash
# Load module file
source activate_deepmd.sh

export OMP_NUM_THREADS=4

# /usr/lib64/libgsl.so.0

date

mpirun -np 3 lmp_mpi -i input.lammps 

date

