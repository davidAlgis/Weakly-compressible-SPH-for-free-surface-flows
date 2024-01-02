# Weakly Compressible Smoothed Particles Hydrodynamics (WCSPH) for free surface flow 

This project is an implementation of free surface flow dynamics with WCSPH method. A description of this method can be found in [the paper of Becker and Teschner (2008)](https://cg.informatik.uni-freiburg.de/publications/2007_SCA_SPH.pdf) and in [the paper of Clavet et al. (2005)](http://www.ligum.umontreal.ca/Clavet-2005-PVFS/pvfs.pdf).

<p align="center">
<img src="./gif/demo.gif">
</p>


# Configure and build the project

This project use freeglut for rendering, to configure it just execute with Python the `freeglutConfiguration.py` script at the root of the project. Then to configure the C++ project you can use the [premake file](https://premake.github.io/download) `premake5.lua`. For example for windows system just run the following commands at the root of the project:
```
premake5 vs2019
``` 