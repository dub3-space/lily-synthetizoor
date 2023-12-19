# syntax=docker/dockerfile:1
# This one is good for linux/arm64/v8

ARG PYTHON_VERSION=3.10.8
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app


# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN apt-get update && apt-get install -y  gcc \
    rustc \
    curl \
    libsndfile1-dev \
    g++ 

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y 

# # Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"
  
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


# Copy the source code into the container.
COPY /src /app
COPY /model /app/model

# Run the application.
ENTRYPOINT ["python", "app.py"]
