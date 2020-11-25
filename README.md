![Logo](https://raw.githubusercontent.com/biosimulations/Biosimulations/dev/biosimulations/libs/shared/assets/src/assets/images/biosimulators-logo/logo-white.svg)

# BioSimulators

More comprehensive and more predictive models have the potential to advance biology, bioengineering, and medicine. Building more predictive models will likely require the collaborative efforts of many investigators. This requires teams to be able to share and reuse model components and simulations. Despite extensive efforts to develop standards such as [COMBINE/OMEX](https://combinearchive.org/), [SBML](http://sbml.org), and [SED-ML](https://sed-ml.org), it remains difficult to reuse many models and simulations. One challenge to reusing models and simulations is the diverse array of incompatible modeling formats and simulation tools.

[BioSimulators](https://biosimulators.org) addresses this challenge by providing is a registry of simulation tools, many of which provide consistent interfaces. These standardized simulation tools make it easier to find and run simulations. These standardized simulation tools build upon BioSimulators' standard for command-line interfaces for simulation tools, standard structure for Docker images of simulation tools, and format for capturing the capabilities (e.g., supporting modeling frameworks, simulation algorithms, modeling formats) of a simulation tool.

The BioSimulators website provides a web application for browsing this registry. This website provides links to the individual simulators and their containers. Instructions for using the containers are available at https://biosimulators.org/help. Information about how to containerize a simulation tool and submit it to the registry is also available at https://biosimulators.org/help.

[runBioSimulations](https://run.biosimulations.org) provides a simple web application for using the containerized simulation tools in the BioSimulators registry to execute simulations. This makes it easy to run a broad range of simulations without having to install any software. [BioSimulations](https://biosimulations.org) provides a platform for sharing modeling studies, modifying published studies, and executing published studies using runBioSimulations.

This repository serves several function:
- This repository is a central place for users to contribute and discuss issues related to BioSimulators. 
- This repository is a central place for simulation software developers to submit simulation tools to the BioSimulators registry. 
- This repository contains code for automated verification of the capabilities of containerized simulation tools.

The code for the BioSimulators web application, REST API, and database is in the [Biosimulations repository](https://github.com/biosimulations/Biosimulations). The code for verifying the capabilities and accuracy of containerized simulation tools is in the [Biosimulators_test_suite repository](https://github.com/biosimulators/Biosimulators_test_suite).

## Getting started

### Users

We recommend that users use the hosted versions of BioSimulators at https://biosimulators.org.

### Simulation software developers

Information about how to containerize a simulation tool and information about how to submit simulation tools to the registry is available at https://biosimulators.org/help. We encourage developers to containerize their tools. However, BioSimulators also acccepts simulation tools that don't support BioSimulators' standards.

### Developers

We welcome contributions to BioSimulators! Please see the [Guide to Contributing](CONTRIBUTING.md) for information about how to get started.

## License

This package is released under the [MIT license](LICENSE).

## Development team

This package was developed by the [Karr Lab](https://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York and the [Center for Cell Analysis and Modeling](https://health.uconn.edu/cell-analysis-modeling/) at the University of Connecticut Health Center as part of the [Center for Reproducible Biomodeling Modeling](https://reproduciblebiomodels.org).

- [Bilal Shaikh](https://www.bshaikh.com)
- [Jonathan Karr](https://www.karrlab.org)
- Akhil Marupilla
- [Mike Wilson](https://www.linkedin.com/in/mike-wilson-08b3324/)
- [Ion Moraru](https://facultydirectory.uchc.edu/profile?profileId=Moraru-Ion)

## Funding

This package was developed with support from the National Institute for Bioimaging and Bioengineering (award P41EB023912).

## Questions and comments

Please contact us at [info@biosimulators.org](mailto:info@biosimulators.org) with any questions or comments.
