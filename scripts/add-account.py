import mysql.connector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', help='Account id')
parser.add_argument('--alias', help='Account alias')
parser.add_argument('--env', help='Environment to which account belogs')

def add_data_to_table(data):
    try:
        # Establishing a connection to the MySQL database
        connection = mysql.connector.connect(
            host="3.139.240.69",
            user="jenkins",
            password="jenkins",
            database="freq_infra"
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to insert data into the table
        insert_query = "INSERT INTO account (account_id, alias, env) VALUES (%s, %s, %s)"

        # Inserting data into the table
        cursor.execute(insert_query, data)

        # Commit your changes in the database
        connection.commit()
        print("Account added successfully")

    except mysql.connector.Error as error:
        print(f"Failed to add account : {error}")

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

args = parser.parse_args()
if args.id:
    if args.alias:
        if args.env:
            data_to_insert = (args.id, args.alias, args.env)  
            add_data_to_table(data_to_insert)
        else:
            print("Environment not provided.")
    else:
        print("Account alias name not provided.")
else:
    print("Account id not provided.")
