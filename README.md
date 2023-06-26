[![Simulation](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

# Lesson 1 - Getting Started :)

The goal of this lesson is familiarize you with how to setup and run GridLAB-D projects on GitHub. The specific learning objectives for this lesson are the following.

1. How to setup a GitHub project using GitHub Actions to run a GridLAB-D simulation.

2. How to use caching to avoid repeating steps that are network or compute intensive.

3. How to run a GridLAB-D simulation.

4. How to save artifacts from a simulation so they can be downloaded later.

## Running GridLAB-D using GitHub Action

You will learn how to use a GridLAB-D subcommand to download a reference model, use the GridLAB-D powerflow solver to compute the voltage solution for the IEEE-123 model, and use the GridLAB-D output converters to generate a voltage profile PNG image that can be downloaded later for viewing.

To view the output, select [**Actions**](../../actions) to show the most recent simulation runs. Select the most recent run completed, download, and view the PNG image artifact named **`IEEE 123 Voltage Profile`**.

## Model Purpose

The purpose of this model is to plot IEEE-123 feeder voltage profile.

### Workflow

The gridlabd simulation is started by the [workflow file](.github/workflows/main.yml).  There are four important parts to this file

1. The [`on`](.github/workflows/main.yml#L3) step determines when the simulation is run. It currently specifies that the simulation will run when a change is made to a file on the `main` or `develop` branches, or when a file is changed on a branch that has an open pull request to the `main` or `develop` branches.

2. The [`cache`](.github/workflows/main.yml#L17) step checks to see whether the specified file(s) have been downloaded during a previous run and reuses them if possible.  In this case, the [`123.glm`](https://github.com/arras-energy/gridlabd-models/blob/master/gridlabd-4/IEEE/123.glm) file is cached to avoid downloading more often than necessary.

3. The [`run`](.github/workflows/main.yml#L28) step run the model files itself, the details of which are discussed below.

4. The [`save`](.github/workflows/main.yml#L31) step makes the specified files available for download as artifacts from the [**Actions**](../../actions) tab after the simulation is complete.

### Model

The simulation model is defined in the file [`main.glm`](main.glm).  There are three parts to this file.

1. The [`#ifmissing`](main.glm#L1) macro checks for the existence of the [`123.glm`](https://github.com/arras-energy/gridlabd-models/blob/master/gridlabd-4/IEEE/123.glm) model file. If the file is not found, then the next command [`#model`](main.glm#L2) is used to get a copy of the model from the [GridLAB-D models repository](https://github.com/arras-energy/gridlabd-models).

2. The [`#include`](main.glm#L4) macro loads the [`123.glm`](https://github.com/arras-energy/gridlabd-models/blob/master/gridlabd-4/IEEE/123.glm) model that was downloaded (or cached). This is the only model component loaded in this example.

3. The [`#output`](main.glm#L5) macro is used to generate the voltage profile PNG image.  The file generated is used to provide the artifact saved by the [`save`](.github/workflows/main.yml#L31) step in the [workflow file](.github/workflows/main.yml).

# Exercises

1. Create a new project using the [new project template](../../../.new_project).
2. Plot the voltage project of the [IEEE 37 node model](https://github.com/arras-energy/gridlabd-models/blob/master/gridlabd-4/IEEE/37.glm).

# More Information

* [Command line options](https://docs.gridlabd.us/index.html?owner=arras-energy&project=gridlabd&branch=master&folder=/Command&doc=/Command/Help.md)
* [Output converters](https://docs.gridlabd.us/index.html?owner=arras-energy&project=gridlabd&branch=master&folder=/Converters/Output&doc=/Converters/Output/Png_images.md)
* [Macros](https://docs.gridlabd.us/_page.html?owner=arras-energy&project=gridlabd&branch=master&folder=/GLM/Macro&doc=/GLM/Macro/Ifmissing.md)

# Next Lesson

* [Lesson 2 - Static Loads](../../../lesson-2)
