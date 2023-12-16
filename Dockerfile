FROM python:3.10.10-buster

WORKDIR /app

COPY /src /app
COPY requirements.txt /app


# RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
