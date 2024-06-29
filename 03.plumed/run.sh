#!/bin/bash

export PATH="/rs1/researchers/w/wjpfaend/rahul/MLP/package_nequip/gsl-2.7/bin:$PATH"
export LD_LIBRARY_PATH="/rs1/researchers/w/wjpfaend/rahul/MLP/package_nequip/gsl-2.7/lib:$LD_LIBRARY_PATH"

for dir in $(seq 4.2 -0.1 3.8)
do

mkdir $dir 

cd $dir
echo $dir $o_dir
cp ../files/input.lammps .

if [[ "$dir" == "3.6" ]]; then
    cp "../files/restart.lmp" .
fi


if [[ "$dir" != "3.6" ]]; then
    cp "../$o_dir/restart.data" .
fi

mv restart.data restart.lmp

cat << EOF > plumed.dat
# PLUMED FILE
# -------------------------------------
# 		UNITS
# -------------------------------------
UNITS LENGTH=A ENERGY=kcal/mol
#
d1: DISTANCE ATOMS=1,4
d2: DISTANCE ATOMS=2,1
d3: DISTANCE ATOMS=3,2
d4: DISTANCE ATOMS=4,3
#
# Activate Umbrella Sampling in distance (butadiene)
# with kapps equal to 0.4au/Bohr (224.1 kcal/mol/Ang^2), distance equal Angstrom
#

rest: RESTRAINT ARG=d1 KAPPA=896.4 AT=$dir

FLUSH STRIDE=100

PRINT ARG=d1,d2,d3,d4,rest.bias STRIDE=100 FILE=COLVAR


EOF

o_dir=$dir
mpirun -np 3 lmp_mpi -i input.lammps

cd ../

done


