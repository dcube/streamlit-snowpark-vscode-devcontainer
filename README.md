# streamlit-snowpark-vscode-devcontainer

# Introduction 
devcontainer for VsCode for Streamlit and Snowpark
Create a virtual env with Python 3.8, streamlit, snowpark for data Science and data exploration experiments

# Getting Started
## Pre requisites
1. Docker Desktop
2. VSCode with the Dev Containers extension

## How to use it
1. Open Docker Desktop and configure [File Sharing in Docker](https://docs.docker.com/desktop/get-started/#file-sharing) Desktop to list directories that can be mounted into Docker containers. cf. Settings->Resources->File sharing
2. Fork this project for your datalab experiment and open it with VsCode
3. Copy the .streamlit/secrets-example.toml as .streamlit/secrets.toml, edit it to fill the snowflake connection informations
4. In VsCode use the command palette (Ctrl + P) and enter >Dev containers: Rebuild and Reopen in Container

If the requirements are not correctly installed (check with the 'pip list' command), just run :
- pip install -r /workspaces/app/.devcontainer/requirements-dev.txt
- pip install -r /workspaces/app/requirements.txt

Start your streamlit experience by entering:
streamlit run ./src/main.py


This starter kit also contain:
- ./Dockerfile: to build the docker image of your streamlit magic app
- ./.azure-pipelines/pipeline_build_deploy_streamlit_app.yml: to build and push the docker image to an azure container registry with an azure devops pipeline


Please refer
- [streamlit documentation](https://docs.streamlit.io/)
- [snowpark for python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index.html)
