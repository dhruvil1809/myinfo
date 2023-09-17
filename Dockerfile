# Use an official Python runtime as a parent image
FROM python:3.x

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install any dependencies your project requires
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/


# Run your application using Gunicorn
CMD ["gunicorn", "info.wsgi:application", "--bind", "0.0.0.0:8000"]
