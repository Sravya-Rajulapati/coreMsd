# Use an official Python runtime as the base image
FROM python:3.10.4-buster

# Set the working directory in the container
WORKDIR /opt/project

# Expose port 8000
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV MSDSETTINGS_IN_DOCKER true

# Install dependencies
RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.4.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

# Copy project files
COPY ["README.rst", "Makefile", "./"]
COPY msd msd
COPY local local

# Set up the entrypoint
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
