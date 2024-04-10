import mysql.connector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Application Name')
parser.add_argument('--type', help='Application Type')

def add_data_to_table(data):
    try:
        # Establishing a connection to the MySQL database
        connection = mysql.connector.connect(
            host="3.149.245.33",
            user="jenkins",
            password="jenkins",
            database="freq_infra"
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to insert data into the table
        insert_query = "INSERT INTO app (name, type) VALUES (%s, %s)"

        # Inserting data into the table
        cursor.execute(insert_query, data)

        # Commit your changes in the database
        connection.commit()
        print("Applicaton added successfully")

    except mysql.connector.Error as error:
        print(f"Failed to application: {error}")

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

args = parser.parse_args()
if args.name:
    if args.type:
        data_to_insert = (args.name, args.type)  
        add_data_to_table(data_to_insert)
    else:
        print("Application type not provided.")
else:
    print("Application name not provided.")
