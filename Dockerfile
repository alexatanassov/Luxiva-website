FROM jekyll/jekyll:latest

# Install Python and virtualenv
RUN apt-get update && apt-get install -y python3 python3-venv

# Set up the Python virtual environment in the container
RUN python3 -m venv /srv/jekyll/venv
RUN /bin/bash -c "source /srv/jekyll/venv/bin/activate && pip install --upgrade pip"
