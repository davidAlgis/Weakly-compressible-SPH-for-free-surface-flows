# Weakly Compressible Smoothed Particles Hydrodynamics (WCSPH) for free surface flow 

This project is an implementation of free surface flow dynamics with WCSPH method.

<p align="center">
<img src="./gif/demo.gif">
</p>

# Configure and build the project

This project use freeglut for rendering, to configure it just execute with Python the `freeglutConfiguration.py` script at the root of the project. Then to configure the C++ project you can use the [premake file](https://premake.github.io/download) `premake5.lua`. For example for windows system just run the following commands at the root of the project:
```
premake5 vs2019
``` 