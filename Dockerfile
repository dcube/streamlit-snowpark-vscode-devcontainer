FROM python:3.8

# Expose port 8501 to access docker in browser
EXPOSE 8501

# Setup the working directory
WORKDIR /app

#Update and install codec
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

# Install libraries
COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy and execute code
COPY src .
CMD streamlit run home.py
