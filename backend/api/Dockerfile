
# Use an official Python runtime as a parent image
FROM python:3.7

# Copy the current directory contents into the container at /app
COPY . /code 

# Set the working directory to /app
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install poetry
RUN poetry run pip install --upgrade pip
RUN poetry install --no-interaction

# RUN pip install -r requirements.txt
# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD poetry run python ./api/main.py

