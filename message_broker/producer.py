import pika

# Connecting to a broker on our local machine, hence 'localhost'
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# creating a que to which messages will be delivered
channel.queue_declare(queue='letterbox')

# Everything needs to go through an exchange
message = "apples"

# default exchange is identified by an empty string
# routing_key specifies exactly which queue the message should go
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message: {message}")

connection.close()