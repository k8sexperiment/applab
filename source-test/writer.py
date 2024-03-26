import mysql.connector
import time
import os
import logging
from prometheus_client import start_http_server, Summary
from tenacity import retry, stop_after_attempt, wait_fixed

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@retry(stop=stop_after_attempt(10), wait=wait_fixed(1))
def connect_to_db():
    return mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), database=os.getenv('DB_NAME'))

@REQUEST_TIME.time()
def process_request():
    # Connect to the database
    logging.info("Connecting to the database")
    cnx = connect_to_db()
    cursor = cnx.cursor()

    # Check if table exists and create it if not
    logging.info("Checking if table exists")
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255))")

    # Insert some data
    logging.info("Inserting data")
    add_data = ("INSERT INTO test "
                "(data) "
                "VALUES (%s)")
    data = ('test',)
    cursor.execute(add_data, data)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        process_request()
        logging.info("Data inserted")
        time.sleep(1)
