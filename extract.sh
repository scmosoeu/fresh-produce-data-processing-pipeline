#!/bin/bash

COMMODITY=$1

python message_broker/producer.py $COMMODITY
python message_broker/consumer.py 

echo 'Exiting script'
