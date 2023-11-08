import json
import pika

def send(data, body):
    message = {
        'properties': {
            'headers': {
                'x-delay-retries': 0,
                'x-retries-count': 0,
                'x-retries-limit': 5
            },
            'content_type': 'text/plain',
            'delivery_mode': 1
        },
        'body': {
            'order_delivery_id': 105,
            'storage_date': '20.12.2024'
        }
    }

    params = pika.ConnectionParameters(host=data['host'], port=data['port'],
                    credentials=pika.PlainCredentials(username=data['username'], password=data['password']))
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=data['queue'], durable=True)
    channel.basic_publish(exchange='', routing_key=data['queue'],
                          body=json.dumps(message['body']).encode(),
                          properties=pika.BasicProperties(**message['properties']))
