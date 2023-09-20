import os
import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


# Establish a connection to RabbitMQ server
credentials = pika.PlainCredentials(
    os.environ.get("RABBITMQ_DEFAULT_USER", ""),
    os.environ.get("RABBITMQ_DEFAULT_PASS", ""),
)
connection = pika.BlockingConnection(
    pika.ConnectionParameters("rabbitmq", credentials=credentials)
)

channel = connection.channel()

# Declare a "topic" exchange with the same name as the publisher
exchange_name = "my_topic_exchange"
channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

# Declare a unique queue for the consumer
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

# Specify the routing key for the "test" topic
routing_key = "test"

# Bind the queue to the exchange with the specified routing key
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Set up a consumer and define the callback function
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(f' [*] Waiting for messages on topic "{routing_key}". To exit, press CTRL+C')
channel.start_consuming()
