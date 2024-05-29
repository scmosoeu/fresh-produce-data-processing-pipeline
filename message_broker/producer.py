import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

# Everything needs to go through an exchange
message = "apples"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message: {message}")

connection.close()