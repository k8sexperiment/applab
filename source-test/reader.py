from flask import Flask
import mysql.connector
import os
import socket
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def count_rows():
    # Connect to the database
    cnx = mysql.connector.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), database=os.getenv('DB_NAME'))
    cursor = cnx.cursor()

    # Count the rows
    query = ("SELECT COUNT(*) FROM test")
    cursor.execute(query)

    # Get the count
    count = cursor.fetchone()[0]

    cursor.close()
    cnx.close()

    return {'count': count, 'pod': socket.gethostname()}

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    app.run(host='0.0.0.0', port=8080)
