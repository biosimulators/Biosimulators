#############
### base ###
#############
FROM ghcr.io/biosimulators/biosimulators-base:latest

LABEL \
    org.opencontainers.image.title="BioSimulators" \
    org.opencontainers.image.description="Docker image with one Python environment with the validated simulation tools registered BioSimulators" \
    org.opencontainers.image.url="https://biosimulators.org/" \
    org.opencontainers.image.documentation="https://biosimulators.org/help" \
    org.opencontainers.image.source="https://github.com/biosimulators/Biosimulators" \
    org.opencontainers.image.authors="BioSimulators Team <info@biosimulators.org>" \
    org.opencontainers.image.vendor="BioSimulators Team"

###################################
# setup pipenv, ports

# Copy over dependency list
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

# install environment
RUN pipenv sync

# force reinstall of matplotlib due to inconsistent version
RUN pipenv run pip uninstall -y matplotlib \
    && pipenv run pip install "matplotlib==3.2.0" \
    && pipenv run python -c "import matplotlib.font_manager"

# install assimulo because pipenv fails to install it
ARG ASSIMULO_VERSION=3.2.5
RUN pipenv run pip install git+https://github.com/modelon-community/Assimulo.git@Assimulo-${ASSIMULO_VERSION}
