# official python version
FROM python:3.8

# Container working directory
WORKDIR /app
#Copy the current directory contents into the container at/app
COPY . /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# setup dependency
RUN make install
# Launch
CMD ["python", "main.py"]
