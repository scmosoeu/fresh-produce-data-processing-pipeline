import argparse
import os
import pika

rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_queue = os.getenv('RABBITMQ_QUEUE')

def send_message(msg: str) -> dict:
    """
    Publish message in RabbitMQ

    Parameters
    -----------
    msg: A message to send to RabbitMQ broker

    Returns
    --------
    dict: A dictionary containing the sent message
    """

    # Connection to a broker, can be localhost or IP address
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(rabbitmq_host)
    )
    channel = connection.channel()

    # creating a que to which messages will be delivered
    # To ensure that the queue will survive a RabbitMQ node restart, specified 'durable'
    channel.queue_declare(queue=rabbitmq_queue, durable=True)

    # Publish the message onto the que
    channel.basic_publish(exchange='', routing_key=rabbitmq_queue, body=msg)

    # Close the connection to RabbitMQ
    connection.close()

    return {"Message": f"{msg}"}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Market Prices')
    parser.add_argument('commodity', type=str, help='Commodity Name')

    args = parser.parse_args()
    send_message(msg=args.commodity)
