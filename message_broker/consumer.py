import os
import pika
import requests

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_queue = os.getenv('RABBITMQ_QUEUE')
api_host = os.getenv('API_HOST')
api_port = os.getenv('API_PORT')


def on_message_received(ch, method, properties, body):
    """
    Subscribe a callback function to a queue
    """
    commodity = body.decode('utf-8')

    url = f"http://{api_host}:{api_port}/{commodity}"

    commodity_response = requests.get(url)

    res = commodity_response.json()

    print(res)


def retrieve_message() -> dict:
    """
    Retrieve a message in a que

    Returns
    --------
    dict
    """

    # Connection to a broker, can be localhost or IP address
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(rabbitmq_host)
    )
    channel = connection.channel()

    channel.queue_declare(queue=rabbitmq_queue, durable=True)

    # Tell RabbitMQ that the callback function should receive messages
    # from the queue
    channel.basic_consume(
        queue=rabbitmq_queue,
        auto_ack=True,
        on_message_callback=on_message_received
    )

    # Start consuming messages in a que
    channel.start_consuming()

    return {"Message": "Success!"}
