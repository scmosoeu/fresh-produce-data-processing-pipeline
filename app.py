from message_broker import consumer, producer


consumed_msg = consumer.retrieve_message()
print('Consumed msg:', consumed_msg)

receive_msg = producer.send_message('apples')
print('Received msg:', receive_msg)