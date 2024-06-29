#!/bin/bash
#BSUB -n 12		# number of processor
#BSUB -W 01:00		# wall clock time
#BSUB -q short #long #standard #single_chassis	# Queue Name
#BSUB -J dp_btd 	# Name of job
#BSUB -R span[hosts=1] 	# Name of job
#BSUB -o stdout.%J	# standard out
#BSUB -e stderr.%J	# standatd error

source /usr/share/Modules/init/bash
# Load module file
source activate_deepmd.sh
#
export PATH="/rs1/researchers/w/wjpfaend/rahul/MLP/package_nequip/gsl-2.7/bin:$PATH"
export LD_LIBRARY_PATH="/rs1/researchers/w/wjpfaend/rahul/MLP/package_nequip/gsl-2.7/lib:$LD_LIBRARY_PATH"
#
export OMP_NUM_THREADS=4

# /usr/lib64/libgsl.so.0

date

mpirun -np 3 lmp_mpi -i input.lammps 

date

