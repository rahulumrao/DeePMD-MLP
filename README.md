# DeePMD-MLP
## [Molecular Dynamics with DeePMD](https://github.com/deepmodeling/deepmd-kit) [<a href="https://tutorials.deepmodeling.com/en/latest/" style="color:orange">DeepModeling Tutorial!</a>]

#### Required Libraries : [numpy](https://pypi.org/project/numpy/), [pandas](https://pandas.pydata.org/), [deepmd](https://github.com/deepmodeling/deepmd-kit),[dpdata](https://github.com/deepmodeling/dpdata), [ase](https://pypi.org/project/ase/), [matplotlib](https://pypi.org/project/matplotlib/)

This is a tutorial for the `DeePMD`package, a Machine Learning Interatomic Potential (MLP) model for interatomic potential energy and force field and to perform molecular dynamics (MD).
<br>

In-general, steps to build MLPs usually require three main steps: <br>
1. Data generation      `[00.data]`
2. Training             `[01.train]`
3. Molecular dynamics   `[02.lmp]`

<br>
For data generation, we will be using the [VASP](https://www.vasp.at/") package. \

Here, I will not go into the details for generating the initial configuration. However, there are several ways to do that. A straightforward approach involves performing a classical MD simulation to obtain random configurations. Subsequently, <i>ab-initio</i> calculations are performed to compute the potential energy and corresponding forces (in this case, we will be using VASP). \

The output configurations are stored in the folder inside the `00.data` directory.

<div class="alert alert-block alert-info">
    <span style="font-size: 1.2em; color: green;"> <b>Note:</b> Energies and forces for these configurations are obtained using PBE functional. </span>
</div>

## Author:
Rahul Verma \
Dept. of Chemical and Biomolecular Engineering \
North Carolina State University, Raleigh, NC, USA \
Email: rverma7@ncsu.edu
