import pika
import requests


def on_message_received(ch, method, properties, body):

    commodity = body.decode('utf-8')
    response = requests.get(f"http://0.0.0.0:8000/{commodity}")

    print(f"received new message: {response.json()}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

print("started consuming")

channel.start_consuming()