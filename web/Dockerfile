########################################
# Stage builder
########################################
FROM python:3.10.11-slim-bullseye AS builder

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home umba
USER umba
WORKDIR /home/umba

ENV VIRTUALENV=/home/umba/venv
# TODO: export SECRET_KEY in production
# ENV echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=umba pyproject.toml constraints.txt ./
RUN python -m pip install --upgrade pip setuptools && \
    python -m pip install --no-cache-dir -c constraints.txt ".[dev]"

# Copy project src files
COPY --chown=umba src/ src/
    

# make sure log and var directories exist
# RUN mkdir -pv /var/{log,run}/gunicorn/

# TODO: unit testing
# COPY --chown=umba test/ test/

# RUN python -m pip install . -c constraints.txt && \
# RUN python -m flake8 portfolio/ && \
#     # python -m pytest test/unit/ && \
#     python -m isort portfolio/ --check && \
#     python -m black portfolio/ --check --quiet && \
#     # below is an example of how to disable false positive bugs
#     # python -m pylint portfolio/ --disable=C0114,C0116,R1705 && \
#     python -m pylint portfolio/ --disable=C0114,C0116,R1705 && \
#     python -m bandit -r portfolio/ --quiet && \
RUN python -m pip wheel --wheel-dir dist/ . -c constraints.txt


########################################
# Stage stage01
########################################

FROM python:3.10.11-slim-bullseye AS stage01

RUN apt-get update && \
    apt-get upgrade --yes

RUN useradd --create-home umba
USER umba
WORKDIR /home/umba

ENV VIRTUALENV=/home/umba/venv
# TODO: export SECRET_KEY in production
# ENV echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

# Copy app
COPY --chown=umba --from=builder /home/umba/dist/django_portfolio*.whl /home/umba
# Copy project config
COPY --chown=umba config/ config/

RUN python -m pip install --upgrade pip setuptools && \
    python -m pip install --no-cache-dir django_portfolio*.whl
