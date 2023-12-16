# Overview
Streamlit-based web application for managing user profiles. The app allows users to enter their username, email, and hobbies, and stores this information in a PostgreSQL database. The backend setup includes Docker services for the web app, database, and PgAdmin for database management.

## Features
User interface for entering profile information (username, email, hobbies).
PostgreSQL database integration for data storage.
Docker setup including web app, database, and PgAdmin services.
Requirements
Docker
Python
PostgreSQL
Streamlit
psycopg2
Installation and Setup
Clone the Repository: Clone this repository to your local machine.

Environment Variables: Set up the following environment variables:

POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
PGADMIN_DEFAULT_EMAIL
PGADMIN_DEFAULT_PASSWORD
Docker Setup: Use Docker Compose to build and run the services defined in the docker-compose.yml file. Run docker-compose up to start the services.

Access the Application: The Streamlit app will be available at localhost:8501.

PgAdmin: Access PgAdmin at localhost:7000 for database management.

## Usage
Enter Profile Information: On the Streamlit app interface, enter your username, email, and hobbies.

Submit Data: Click on the "Submit" button to save your data to the PostgreSQL database.

View Submission: The app displays the entered information and confirms if the data was successfully saved.

## Database Interaction
The app uses psycopg2 to connect to and interact with the PostgreSQL database.
User data is stored in the users_info table.
File Structure
app.py: Main Streamlit app script.
Dockerfile: Docker configuration for the web app.
docker-compose.yml: Docker Compose file to set up and run the services.
requirements.txt: List of Python package dependencies.
Contributing
Contributions to this project are welcome. Please open an issue or pull request to suggest changes or additions.

## License
MIT

