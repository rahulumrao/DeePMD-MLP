#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

dft = np.loadtxt('/Users/rverma7/My_Calc/NCSU_Work/NeQUIP/Butadiene/CP2K_RUN/restart_3/fes.dat')
dpmd = np.loadtxt('interp_free_energy.dat')
dft_min = min(dft[:,1])
dpmd_min = min(dpmd[:,1])
print(dft_min, dpmd_min)

plt.scatter(dft[:,0], (dft[:,1] - dft_min), color='r', s=12, marker='o', facecolor='none')
plt.plot(dft[:,0], (dft[:,1] - dft_min), label="DFT", color='r', lw=1.5)
plt.plot(dpmd[:,0]+0.03, (dpmd[:,1] - dpmd_min), label="DeePMD", color='b', lw=1.5)

plt.xlim(1.2,4.2)
plt.ylim(None,35.0)


plt.xlabel(r'distance ($\rm{\AA}$)', font='Helvetia, 12')
plt.ylabel(r'free energy ($\rm{kcal/mol}$)')

plt.legend()
plt.grid(ls='-.')

plt.savefig('butad_fes.jpeg', dpi=200)
