import pika

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

print("started consuming")

channel.start_consuming()