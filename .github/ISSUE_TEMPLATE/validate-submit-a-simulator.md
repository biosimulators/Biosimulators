---
name: Validate or contribute a simulator
about: Validate or contribute a containerized simulation tool, another version of the tool, or update a version of the tool.
title: ''
labels: 'Validate/submit simulator'
assignees: ''

---

## Instructions

Please use this issue to validate or contribute a containerized simulation tool, another version of the tool, or update a version of the tool. Specifically, edit the YAML syntax between the `---` below and then click the `Submit new issue` button.

Instructions for containerizing simulation tools and examples are available at https://biosimulators.org/help.

## Pre-submission checklist

**Is your containerized simulation tool compliant with BioSimulators' conventions?**

- [ ] The container provides a [BioSimulators-compliant command-line interface](https://biosimulators.org/help) that supports the [COMBINE/OMEX archive](https://combinearchive.org/) and [SED-ML](https://sed-ml.org) formats
- [ ] The `ENTRYPOINT` of the container is set to this command-line interface
- [ ] The specifications of the simulator follow the [BioSimulators format](https://api.biosimulators.org)
- [ ] Any additional ontology terms necessary to describe your simulator have been approved
     - [ ] Modeling frameworks: [SBO](https://sourceforge.net/p/sbo/term-request/)
     - [ ] Algorithms and their parameters: [KiSAO](https://sourceforge.net/p/kisao/feature-requests/new/)
     - [ ] Modeling formats: [EDAM](https://github.com/edamontology/edamontology/issues/new/choose)
     - [ ] Licenses: [SPDX](https://tools.spdx.org/app/submit_new_license/)
- [ ] Optional, the source code for the simulation tool is publicly available
- [ ] Optional, the simulation tool is available through a software repository such as CRAN or PyPI
- [ ] Optional, examples, tutorials, and documentation for the simulation tool are publicly available
- [ ] Optional, the simulation tool is registered with [bio.tools](https://bio.tools/)
- [ ] Optional, the container uses [labels to provide Open Containers Initiative-compliant metadata](https://biosimulators.org/help)
- [ ] Optional, the container uses [labels to provide BioContainers-compliant metadata](https://biosimulators.org/help)
- [ ] Optional, the container is registered with [BioContainers](https://biocontainers.pro/)

## Submission

**What is the id, version, and URL of the specifications of your simulation tool? Should BioSimulators validate your Docker image? Should BioSimulators save your simulator to the BioSimulators registry?**
Please follow the YAML template below.

---
id: tellurium
version: 2.1.6
specificationsUrl: https://raw.githubusercontent.com/biosimulators/Biosimulators_tellurium/2.1.6/biosimulators.json
validateImage: true
commitSimulator: true

---

## Post-submission approval workflow

Once you submit this issue, BioSimulators will use the following workflow to validate, approve, and optionally commit your simulator to the BioSimulators database:

1. An issue will be created with the label `Validate/submit simulator`.
2. An automated action will review your submission:
   1. Retrieve the specifications of your simulator.
   2. Validate these specifications.
   3. Check if you have permissions to submit this simulator.
      - If no simulator has been submitted with this id, a GitHub team will be created to manage permissions to edited the specifications of your simulator and you will be added as a maintainer of this team. This will enable you to add collaborators to this team at https://github.com/orgs/biosimulators/teams/simulator-developers/teams.
      - If your simulator is already in the BioSimulators registry, the action will check that you are member of the team which owns that simulator. If you are not a member, you will not be allowed to edit the specifications of the simulator. In that case, you will need to request membership to the team for your simulator.
   4. Optionally, validate the containerized simulator specified in your specifications.
3. If the validation fails, any errors will be posted to this issue. After fixing these issues, please edit the first block of this issue to re-initiate the automated validation.
4. If the validation succeeds, the `Validated` label will be added to the issue.
5. The submission of the first version of your simulator will be reviewed by the BioSimulators Team.
   1. If there are any concerns about your submission, the BioSimulators Team will use this issue to communicate them to you.
   2. The BioSimulators Team will work with you to resolve these concerns.
6. Once your simulator is approved, the BioSimulators Team will add the label `Approved` to this issue. 
7. If requested, the simulator will automatically be committed to the BioSimulators database and the issue will automatically be closed.


## Re-submission change list

If you need to revise your simulator to pass the validation, please use this section to briefly describe the changes that you made.
