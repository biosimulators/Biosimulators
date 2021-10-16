[![Binder](https://mybinder.org/badge_logo.svg)](https://tutorial.biosimulators.org/)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![Logo](https://raw.githubusercontent.com/biosimulations/Biosimulations/dev/libs/shared/assets/src/assets/images/biosimulators-logo/logo-white.svg)

# BioSimulators

More comprehensive and more predictive models have the potential to advance biology, bioengineering, and medicine. Building more predictive models will likely require the collaborative efforts of many investigators. This requires teams to be able to share and reuse model components and simulations. Despite extensive efforts to develop standards such as [COMBINE/OMEX](https://combinearchive.org/), [SBML](http://sbml.org), and [SED-ML](https://sed-ml.org), it remains difficult to reuse many models and simulations. One challenge to reusing models and simulations is the diverse array of incompatible modeling formats and simulation tools.

[BioSimulators](https://biosimulators.org) addresses this challenge by providing is a registry of simulation tools, many of which provide consistent interfaces. These standardized simulation tools make it easier to find and run simulations. These standardized simulation tools build upon BioSimulators' standard for command-line interfaces for simulation tools, standard structure for Docker images of simulation tools, and format for capturing the capabilities (e.g., supporting modeling frameworks, simulation algorithms, modeling formats) of a simulation tool.

The BioSimulators website provides a web application for browsing this registry. This website provides links to the individual simulators and their containers. Instructions for using the containers are available at https://biosimulators.org/help. Information about how to containerize a simulation tool and submit it to the registry is also available at https://biosimulators.org/help.

[runBioSimulations](https://run.biosimulations.org) provides a simple web application for using the containerized simulation tools in the BioSimulators registry to execute simulations. This makes it easy to run a broad range of simulations without having to install any software. [BioSimulations](https://biosimulations.org) provides a platform for sharing modeling studies, modifying published studies, and executing published studies using runBioSimulations.

This repository serves several function:
- This repository is a central place for users to contribute and discuss issues related to BioSimulators. 
- This repository is a central place for simulation software developers to submit simulation tools to the BioSimulators registry. 
- This repository contains code for automated verification of the capabilities of containerized simulation tools.
- This repository contains a Pipenv configuration and a Dockerfile for a Docker image with a Python environment with most of the validated simulation tools and tests for this Docker image

The code for the BioSimulators web application, REST API, and database is in the [Biosimulations repository](https://github.com/biosimulations/Biosimulations). The code for verifying the capabilities and accuracy of containerized simulation tools is in the [BioSimulators test suite repository](https://github.com/biosimulators/Biosimulators_test_suite). The code for the individual simulation tools is spread across numerous repositories, including several owned by the [BioSimulators GitHub organization](https://github.com/biosimulators/).

## Getting started

### Users

We recommend that users use the hosted versions of runBioSimulations at https://run.biosimulations.org to execute simulations.

Each validated simulation tool is available as Docker image. Most of the validated simulation tools are also available as Python APIs. See https://biosimulators.org for information about the interfaces available for each tool and where they can be obtained.

A Docker image with a Python environment with APIs for most of the validated simulation tools is available at https://github.com/orgs/biosimulators/packages/container/package/biosimulators. An iPython shell for this environment can be launched by installing Docker and running the commands below. Information about using the Python APIs in the image is available at https://biosimulators.org/help.:
```
docker pull ghcr.io/biosimulators/biosimulators
docker run -it --rm ghcr.io/biosimulators/biosimulators
```

Interactive tutorials for the Python APIs for simulation tools and for BioSimulators' API are available from Binder [here](https://tutorial.biosimulators.org/).

### Simulation software developers

Information about how to containerize a simulation tool and information about how to submit simulation tools to the registry is available at https://biosimulators.org/help. We encourage developers to containerize their tools. However, BioSimulators also acccepts simulation tools that don't support BioSimulators' standards.

### Developers

We welcome contributions to BioSimulators! Please see the [Guide to Contributing](CONTRIBUTING.md) for information about how to get started.

## Technical documentation

Please see the links below for additional technical documentation.

* Simulation tools, format converters, SED-ML/COMBINE validator, simulator test suite, and Python utilities: https://docs.biosimulators.org
* REST API: https://api.biosimulators.org
* Web site and database: https://docs.biosimulations.org

## Known issues

### Installation of individual simulation tools

* Several simulation tools are not available from PyPI
    * There is an open issue to publish **LibSBMLSim** to PyPI.
    * The version of **RBApy** used by BioSimulators is a fork. This fork adds the ability to run simulation with GLPK and Gurobi, in addition to CPLEX. There is an open pull request to merge this fork. There is also an open issue to publish RBA to PyPI.
    * **BioNetGen**, **VCell** and **XPP** cannot be installed from PyPI because they are not Python packages.
    * Most simulation tools require dependencies which must be installed separately from pip. See each tool for its installation instructions.

### BioSimulators consolidated Docker image

* **OpenCOR** is not currently installed because OpenCOR is distributed as its own Python environment. A a result, OpenCOR is difficult to install into other environments, such as the consolidated BioSimulators environment. In addition, OpenCOR is also currently pinned to Python 3.7.
* **VCell** is not currently installed because limited installation instructions are available. VCell also does not provide a compatible Python API.


## Utilizing multiple simulation tools within a single Python environment

* **PySCeS** and **NEURON/NetPyNe** cannot be imported into the same Python memory. This appears to be due to using different versions of SUNDIALS. Importing both causes segmentation faults. One workaround is to import the tools in separate forks that have separate memories.
* When installing **tellurium** or **MASSpy**, as well additional tools, it may be necessary to reinstall **numpy** (1.19.3) and **matplotlib** (3.2) after all tools have been installed. Those two particular microversions of numpy and matplotlib are necessary because the latest versions of tellurium (2.2.0) and MASSpy (0.1.2) require those specific microversions. This reinstallation is necessary when pip first installs more recent versions of numpy and matplotlib, compiles packages for those versions of numpy and matplotlib, and then replaces numpy or matplotlib with the older versions of numpy and matplotlib required by tellurium and MASSpy when tellurium and MASSpy are installed to satisfy their requirements of numpy and matplotlib. This problem stems from the limited control over environments provided by pip.

## License

This package is released under the [MIT license](LICENSE).

## Development team

This package was developed by the [Karr Lab](https://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York and the [Center for Cell Analysis and Modeling](https://health.uconn.edu/cell-analysis-modeling/) at UConn Health as part of the [Center for Reproducible Biomodeling Modeling](https://reproduciblebiomodels.org) with assistance from the contributors listed [here](CONTRIBUTORS.md).

- [Bilal Shaikh](https://www.bshaikh.com)
- [Jonathan Karr](https://www.karrlab.org)
- [Ion Moraru](https://facultydirectory.uchc.edu/profile?profileId=Moraru-Ion)

## Funding

This package was developed with support from the National Institute for Bioimaging and Bioengineering (award P41EB023912).

## Questions and comments

Please contact us at [info@biosimulators.org](mailto:info@biosimulators.org) with any questions or comments.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/danv61"><img src="https://avatars.githubusercontent.com/u/29076329?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dan Vasilescu</b></sub></a><br /><a href="#tool-danv61" title="Tools">🔧</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!