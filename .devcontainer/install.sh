#!/bin/bash

sudo chgrp vscode /workspaces/app/.venv
sudo chown vscode /workspaces/app/.venv

git config --global --add safe.directory /workspaces/app
git config --global core.autocrlf true

sudo apt-get update
sudo apt-get install vim -y

python3 -m venv /workspaces/app/.venv
PATH="/workspaces/app/.venv/bin:$PATH"

source /workspaces/app/.venv/bin/activate
pip install --upgrade pip

#install requirements
pip install -r /workspaces/app/.devcontainer/requirements-dev.txt
pip install -r /workspaces/app/requirements.txt