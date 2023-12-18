FROM python:3.10.10-buster


RUN apt-get update && apt-get install -y rustc \
    curl \
    libsndfile1-dev

# need rust for a library
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y 

# # Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app


COPY /src /app
COPY /model /app/model
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "app.py"]
