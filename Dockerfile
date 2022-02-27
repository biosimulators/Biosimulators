#############
### base ###
#############
FROM ghcr.io/biosimulators/biosimulators-base:latest

LABEL \
    org.opencontainers.image.title="BioSimulators" \
    org.opencontainers.image.description="Docker image with one Python environment with the validated simulation tools registered BioSimulators" \
    org.opencontainers.image.url="https://biosimulators.org/" \
    org.opencontainers.image.documentation="https://docs.biosimulations.org/" \
    org.opencontainers.image.source="https://github.com/biosimulators/Biosimulators" \
    org.opencontainers.image.authors="BioSimulators Team <info@biosimulators.org>" \
    org.opencontainers.image.vendor="BioSimulators Team"

###################################
# setup pipenv, ports

# Copy over dependency list
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# install pipenv and set up environment
RUN pip install pipenv \
    && pipenv install --system --deploy

# set up matplotlib font manager
RUN python -c "import matplotlib.font_manager"

# install assimulo because pipenv fails to install it
ARG ASSIMULO_VERSION=3.2.9
RUN pip install git+https://github.com/modelon-community/Assimulo.git@Assimulo-${ASSIMULO_VERSION}

CMD /bin/bash /xvfb-startup.sh ipython
