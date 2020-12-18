# Guide to contributing to the BioSimulators platform

We enthusiastically welcome contributions to BioSimulators! This document describes how developers can contribute the BioSimulators platform (e.g., web application, REST API, database, test suite). Information for simulation software tool developers about contributing containerized simulation tools is available at https://biosimulators.org/help.

## Coordinating contributions

Before getting started, please contact the lead developers at [info@biosimulators.org](mailto:info@biosimulators.org) to coordinate your planned contributions with other ongoing efforts. Please also use GitHub issues to announce your plans to the community so that other developers can provide input into your plans and coordinate their own work. As the development community grows, we will institute additional infrastructure as needed such as a leadership committee and regular online meetings.

## Project organization

The project is organized into multiple repositories, each which includes its own Guide to Contributing:
- The [Biosimulations repository](https://github.com/biosimulations/Biosimulations) contains the descriptions of the BioSimulators standards for simulation tools, as well as the code for the web application, REST API, and database.
- The [BioSimulators utils repository](https://github.com/biosimulators/Biosimulators_utils) contains utilities for building standardized command-line interfaces for biosimulation tools.
- The [BioSimulators test suite repository](https://github.com/biosimulators/Biosimulators_test_suite) contains the code for testing containerized simulation tools.
- This repository is a central place for users to submit issues about BioSimulators. 
- In particular, these GitHub issues are the vehicle for simulation software developers to contribute containerized simulation to the BioSimulators registry.
- This repository also contains a workflow for validating containerized simulation tools and committing them to the BioSimulators registry.

## Submitting changes

Please use GitHub pull requests to submit changes. Each request should include a brief description of the new and/or modified features. Upon each pull request, GitHub will trigger actions to execute all of the tests. Pull requests will be approved once all tests are passing and the pull request is reviewed by one of the lead developers.

## Deploying new versions

The workflow in this repository for validating and committing containerized simulation tools will automatically be deployed once it is merged into the main `dev` branch.

