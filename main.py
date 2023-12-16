import streamlit as st
import os
import psycopg2
import logging

# Title of the App
st.title("User Profile")

# Form for user input
with st.form("User Form"):
    username = st.text_input("Enter your username")
    email = st.text_input("Enter your email")
    hobbies = st.text_area("What are your hobbies?")
    submitted = st.form_submit_button("Submit")


def create_connection():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
        )
        # This is the service name defined in docker-compose.ym   )
        print("Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
        connection = None
    return connection


# Connect to the database
# conn = create_connection()
# Display entered information
if submitted:
    st.write("Your username is: ", username)
    st.write("Your email is: ", email)
    st.write("Your hobbies are: ", hobbies)

    # Insert the user data into the database
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users_info (username, email, hobbies) VALUES (%s, %s, %s)",
                (username, email, hobbies),
            )
            connection.commit()
            st.success("Data successfully saved to the database")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            logging.error(f"Unhandled exception: {e}")
        # except psycopg2.Error as e:
        # st.error(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

st.image(
    "./smile.jpeg",
    caption="User Profile" " width=200",
)
