#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import ase
from ase.io import read, write
from ase import Atoms
import MDAnalysis as mda


prefix_path = os.getcwd()
print(prefix_path)

# Create cell vectors from A, B, C
cell = [[15.0, 0, 0],
        [0, 15.0, 0],
        [0, 0, 15.0]]

# Path to the XYZ trajectory file
trajectory_file = 'centered_structure.xyz'

# Output directory for Quantum Espresso input files
output_dir = 'poscar_files'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the trajectory
universe = mda.Universe(trajectory_file)

# Iterate over each frame
for ts in universe.trajectory:
    # Convert MDAnalysis universe to ASE atoms
    print(f"# Convert xyz to POSCAR using MDAnalysis for structure {ts}")
    atoms = Atoms(symbols=universe.atoms.names,
                  positions=universe.atoms.positions,
                  cell=cell,
                  pbc=True)
#    print(ts.frame)
    outdir = os.path.join(output_dir, str(ts.frame))
    os.mkdir(outdir)
    write(os.path.join(outdir,f"POSCAR"), atoms, format='vasp')

