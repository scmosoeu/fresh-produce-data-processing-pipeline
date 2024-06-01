import pika

# Connecting to a broker on our local machine, hence 'localhost'
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# creating a que to which messages will be delivered
# To ensure that the queue will survive a RabbitMQ node restart, specified 'durable'
channel.queue_declare(queue='letterbox', durable=True)

# Everything needs to go through an exchange
message = "apples"

# default exchange is identified by an empty string
# routing_key specifies exactly which queue the message should go
# Specified persistent delivery_mode
channel.basic_publish(
    exchange='', 
    routing_key='letterbox', 
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent)
)

print(f"sent message: {message}")

connection.close()