# How to use trame at NERSC

This repository provides material for learning how to use trame using the NERSC infrasrtucture.

## Conda environment creation

[Jupyter at NERSC: How-To Guides](https://docs.nersc.gov/services/jupyter/how-to-guides/#how-to-use-a-conda-environment-as-a-python-kernel) provide information on how to setup your custom environment.

Here is an example on how to do that for trame.

```
module load python
conda create -n trame-intro ipykernel pan3d pooch
conda activate trame-intro
python -m ipykernel install --user --name trame-intro --display-name trame-intro
```

Here is an other example with ParaView for trame

```
module load python
conda create -n trame-pv ipykernel paraview-trame-components
conda activate trame-pv
python -m ipykernel install --user --name trame-pv --display-name ParaView
```

## Topics covered

* Day 1
** Fundamentals of Interactive 3D Visualization with Jupyter
VTK/ParaView and trame Overview: An introduction to the architecture and capabilities of key visualization tools, laying the foundation for the hands-on sessions to follow. We’ll also cover how trame is getting used in material science, AI, simulation input, and more.
** Illustration of trame usage via Pan3D through XArray and Jupyter: Exploring advanced features and practical applications, this session provides a look at how Pan3D explorers and XArray can be leveraged for interactive visualizations thanks to trame.
** Coding with trame – Do It Yourself Visualizations: A practical session where participants create interactive visualizations using Python. Participants will learn the basics of trame and develop a small interactive 3D application.
** trame and Jupyter: How to enable a trame application into a Jupyter Notebook and how you can make the best of it. From cell output to dockable window to finally use it full screen using your live data from your notebook.
* Day 2
** ParaView with trame and how trame goes beyond being just a Web UI
** From VTK to ParaView with trame: This session will focus more on ParaView and how to leverage it via trame and Jupyter. The gotchas and the ParaView-Trame-Components that help create compelling applications in even fewer lines of Python.
** Open discussions with a fallback to the unexpected benefits of using trame on various projects: This session aims to open the floor to the participants and promote interactive discussions on ways to solve specific day-to-day problems. Depending on the remaining time, we will cover various unexpected benefits that we have found when using trame throughout a set of projects we’ve been involved in.

## Getting started

You need to first connect to https://jupyter.nersc.gov/hub/home

Then you can choose to run on the `[Login Node / Perlmutter]` or some dedicated resources.
