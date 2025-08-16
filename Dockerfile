# Use the official Python image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install --no-cache-dir pipenv \
    && pipenv install --system --deploy

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Set the default command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
