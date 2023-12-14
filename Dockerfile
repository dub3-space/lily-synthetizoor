
FROM python:3.10.10-buster


### We make sure that we have authorizations to write on /tmp
RUN chmod 777 -R /tmp && chmod o+t -R /tmp 

# Copy the current directory contents into the container
COPY ./src /app

#tun the app
ENTRYPOINT ["python3", "/app/app.py"]













