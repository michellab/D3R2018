# Instructions for reproducing D3R2018 run

## Software

* [Sire](https://siremol.org/), [feature-mapping](https://github.com/michellab/Sire/tree/feature-mapping) branch
* [BioSimSpace](https://biosimspace.org), [feature-freenrg](https://github.com/michellab/BioSimSpace/tree/feature-freenrg) branch
* [AmberTools18](http://ambermd.org/AmberTools.php)
* [GROMACS 2018](http://manual.gromacs.org/documentation)
* [CUDA Toolkit 9.0](https://developer.nvidia.com/cuda-90-download-archive)
* [OpenMM betacuda90](https://anaconda.org/omnia/openmm/files)

## Installation

In the following we assume that Sire is installed to `$HOME/sire.app`.

### Download and install Sire

```bash
git clone https://github.com/michellab/Sire
cd Sire
git checkout feature-mapping
./compile_sire.sh
```

### Update OpenMM version

```bash
$HOME/sire.app/bin/conda install -c omnia/label/betacuda90 openmm
```

### Recompile Sire for updated OpenMM library

```bash
cd Sire
./compile_sire.sh
```

If you experience errors, then delete the `build/corelib` and `build/wrappers`
directories:

```bash
rm -rf build/corelib
rm -rf build/wrappers
```

### Install BioSimSpace

```bash
git clone https://github.com/michellab/BioSimSpace
cd BioSimSpace/python
git checkout feature-freenrg
$HOME/sire.app/bin/python setup.py install
```

### Install additional software

Install [AmberTools18](http://ambermd.org/AmberTools.php) and
[GROMACS 2018](http://manual.gromacs.org/documentation) as per
their online instructions.

## Running the simulations

### Clone the D3R2018 repository

```bash
git clone https://github.com/michellab/D3R2018
cd D3R2018/CatS/BSS
```

### Update templates

Update the paths in `template.slm` and `analyse_data.sh` to match your
software environment, i.e. the location of `Sire`, `AMBERHOME`, `GMRX`,
etc. You'll also need to update the Slurm directives appropriately for
your cluster.

### Submit

Submit forward and reverse binding free energy simulations for the full
network.

```bash
./submit.sh ligand_pairs.txt
```

### Analysis

```bash
./analyse_data.sh
```
