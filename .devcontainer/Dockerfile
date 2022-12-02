# See here for image contents:
FROM mcr.microsoft.com/devcontainers/python:3.8
WORKDIR /workspaces/app

ARG WORKSPACE_FOLDER="/workspaces/app"
VOLUME $WORKSPACE_FOLDER/.venv

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*
