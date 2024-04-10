import mysql.connector

def add_data_to_table(data):
    try:
        # Establishing a connection to the MySQL database
        connection = mysql.connector.connect(
            host="Nileshs-MacBook-Pro.local",
            user="nilesh",
            password="nilesh",
            database="freq_infra"
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to insert data into the table
        insert_query = "INSERT INTO accounts (id, name) VALUES (%s, %s)"

        # Inserting data into the table
        cursor.execute(insert_query, data)

        # Commit your changes in the database
        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print(f"Failed to insert data into MySQL table: {error}")

    finally:
        # Closing database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage
data_to_insert = (1, "DEV-1")  # Replace with your actual data
add_data_to_table(data_to_insert)
