import time
import os
import pika
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("producer")

# Establish a connection to RabbitMQ server
credentials = pika.PlainCredentials(
    os.environ.get("RABBITMQ_DEFAULT_USER", ""),
    os.environ.get("RABBITMQ_DEFAULT_PASS", ""),
)

while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbitmq", credentials=credentials)
        )
        break
    except:
        logger.warning("Producer waiting for RabbitMQ")
        time.sleep(10)

channel = connection.channel()


# Declare a "topic" exchange
exchange_name = "my_topic_exchange"
channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

# Specify the routing key for the "test" topic
routing_key = "test"

# Publish a message with the specified routing key
_message = "Hello, RabbitMQ Topic!"
counter = 0

try:
    while True:
        message = f"{counter}_{_message}"
        channel.basic_publish(
            exchange=exchange_name, routing_key=routing_key, body=message
        )
        logger.info(f"[{counter}] Sent '{message}' with routing key '{routing_key}'")
        counter += 1
        time.sleep(5)
finally:
    # Close the connection
    connection.close()
