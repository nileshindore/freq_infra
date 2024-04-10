import mysql.connector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Region Name')

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
        insert_query = "INSERT INTO region (name) VALUES (%s)"

        # Inserting data into the table
        cursor.execute(insert_query, data)

        # Commit your changes in the database
        connection.commit()
        print("Region added successfully")

    except mysql.connector.Error as error:
        print(f"Failed to add region : {error}")

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

args = parser.parse_args()
if args.name:
    data_to_insert = (args.name,)
    add_data_to_table(data_to_insert)
else:
    print("Region name not provided.")
