[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD)

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

Interactive tutorials for the Python APIs for simulation tools and for BioSimulators' API are available from Binder [here](https://mybinder.org/v2/gh/biosimulators/Biosimulators_tutorials/HEAD).

### Simulation software developers

Information about how to containerize a simulation tool and information about how to submit simulation tools to the registry is available at https://biosimulators.org/help. We encourage developers to containerize their tools. However, BioSimulators also acccepts simulation tools that don't support BioSimulators' standards.

### Developers

We welcome contributions to BioSimulators! Please see the [Guide to Contributing](CONTRIBUTING.md) for information about how to get started.

## Technical documentation

Please see the links below for additional technical documentation.

* Simulation tools, format converters, SED-ML/COMBINE validator, simulator test suite, and Python utilities: https://docs.biosimulators.org
* REST API: https://api.biosimulators.org
* Web site and database: https://docs.biosimulations.org

## License

This package is released under the [MIT license](LICENSE).

## Development team

This package was developed by the [Karr Lab](https://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York and the [Center for Cell Analysis and Modeling](https://health.uconn.edu/cell-analysis-modeling/) at UConn Health as part of the [Center for Reproducible Biomodeling Modeling](https://reproduciblebiomodels.org).

- [Bilal Shaikh](https://www.bshaikh.com)
- [Jonathan Karr](https://www.karrlab.org)
- [Ion Moraru](https://facultydirectory.uchc.edu/profile?profileId=Moraru-Ion)

## Funding

This package was developed with support from the National Institute for Bioimaging and Bioengineering (award P41EB023912).

## Questions and comments

Please contact us at [info@biosimulators.org](mailto:info@biosimulators.org) with any questions or comments.
