# official python version
FROM python:3.8



# Make port 8080 available to the world outside this container
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8080
# setup dependency
RUN make install
# Launch
CMD ["python", "main.py"]
