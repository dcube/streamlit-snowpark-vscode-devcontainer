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
sudo pip install --upgrade pip

#install requirements
sudo pip install --upgrade --no-deps --force-reinstall -r /workspaces/app/.devcontainer/requirements-dev.txt
sudo pip install --upgrade --no-deps --force-reinstall -r /workspaces/app/requirements.txt 
