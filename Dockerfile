# Use an official runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app


# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the app when the container launches
CMD ["streamlit", "run", "main.py"]






