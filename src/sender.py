import pika
from pika import exceptions


def send(data, body):
    props = {
        'headers': {
            'x-delay-retries': 0,
            'x-retries-count': 0,
            'x-retries-limit': 5
        },
        'content_type': 'text/plain',
        'delivery_mode': 1
    }
    try:
        params = pika.ConnectionParameters(
            host=data['host'], port=data['port'],
            credentials=pika.PlainCredentials(username=data['username'], password=data['password'])
        )
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue=data['queue'], durable=True)
        channel.basic_publish(exchange='', routing_key=data['queue'],
                              body=data['body'].encode(),
                              properties=pika.BasicProperties(**props))
        return True, None
    except exceptions.AMQPError as e:
        return False, e
