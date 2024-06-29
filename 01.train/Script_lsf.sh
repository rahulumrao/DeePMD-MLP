#!/bin/bash
#BSUB -n 4		# number of processor
#BSUB -W 24:00		# wall clock time
#BSUB -q single_chassis	# Queue Name
#BSUB -J dp_trn_btd 	# Name of job
#BSUB -R span[hosts=1] 	# Name of job
#BSUB -o stdout.%J	# standard out
#BSUB -e stderr.%J	# standatd error

source /usr/share/Modules/init/bash
# Load module file
source activate_deepmd.sh

date

dp train input.json

date

