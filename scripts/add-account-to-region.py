import mysql.connector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--account_id', help='Account id')
parser.add_argument('--region_id', help='Region id')

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
        insert_query = "INSERT INTO account_to_region (account_id, region_id) VALUES (%s, %s)"

        # Inserting data into the table
        cursor.execute(insert_query, data)

        # Commit your changes in the database
        connection.commit()
        print("Account_to_region added successfully")

    except mysql.connector.Error as error:
        print(f"Failed to add account_to_region : {error}")

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

args = parser.parse_args()
if args.account_id:
    if args.region_id:
        data_to_insert = (args.account_id, args.region_id)  
        add_data_to_table(data_to_insert)
    else:
        print("Region id not provided.")
else:
    print("Account id name not provided.")
