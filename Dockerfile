FROM python:latest

LABEL version "0.0.1" \
      maintainer "Aniruddha Pandey <anirudh.pandev@gmail.com>"

WORKDIR /app

ENV EMAIL anirudh.pandev@gmail.com
ENV GITHUB_USERNAME pandevim
ENV PYTHONUNBUFFERED=1

# Use Bash as default
SHELL ["/bin/bash", "-c"]

# Root privelage
USER root

# Install dependencies
RUN apt-get update -y && apt-get install --no-install-recommends -y \
		build-essential \
		python3-lxml \
		graphviz

# Install packages
RUN pip install lxml graphviz

CMD ["/bin/bash"]