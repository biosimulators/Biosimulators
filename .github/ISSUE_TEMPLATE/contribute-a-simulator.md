---
name: Contribute a simulator or another version of a simulator
about: Contribute a containerized simulation tool, contribute another version of a simulation tool, or update a version of a simulation tool.
title: ''
labels: 'Submit simulator'
assignees: ''

---

## Instructions

Please use this issue to contribute a containerized simulation tool, contribute another version of a simulation tool, or update a version of a simulation tool. 

Instructions for containerizing simulation tools and examples are available at https://biosimulators.org/help.

After you submit this issue, we will review your simulation tool and discuss any necessary changes here. Once approved, we will add your simulation tool to the BioSimulators registry and it will be advertised on the BioSimulators web application.

## Pre-submission checklist

**Is your containerized simulation tool compliant with BioSimulators' conventions?**

- [ ] The container provides a [BioSimulators-compliant command-line interface](https://biosimulators.org/help) that supports the [COMBINE/OMEX archive](https://combinearchive.org/) and [SED-ML](https://sed-ml.org) formats
- [ ] The entrypoint of the container is set to this command-line interface
- [ ] The specifications of the simulator follow the [BioSimulators format](https://api.biosimulators.org)
- [ ] Optional, the source code for the simulation tool is publicly available
- [ ] Optional, the simulation tool is available through a software repository such as CRAN or PyPI
- [ ] Optional, examples, tutorials, and documentation for the simulation tool are publicly available
- [ ] Optional, the simulation tool is registered with [bio.tools](https://bio.tools/)
- [ ] Optional, the container uses [labels to provide BioContainers-compliant metadata](https://biosimulators.org/help)
- [ ] Optional, the container is registered with [BioContainers](https://biocontainers.pro/)

## Submission

**What is the name, version, and URL of the specifications of your simulation tool?**
Please follow the template YAML syntax below.

---
name: COPASI
version: 4.27.214
specUrl: https://github.com/biosimulators/Biosimulators_COPASI/blob/master/properties.json

---
