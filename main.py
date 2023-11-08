from collections import defaultdict

from flet import app, Text, TextField, Page, ElevatedButton

from src import sender
from data import saver


def main(page: Page):
    def send_handler(e):
        data = {
            'host': host.value,
            'port': port.value,
            'queue': queue.value,
            'username': user.value,
            'password': password.value
        }
        saver.save_data(data)
        try:
            sender.send(data, body)
            result_message.value = 'The message is successfully sent'
        except Exception as e:
            result_message.value = (
                f'''Send event failed:
                HOST: {data['host']},
                POST: {data['port']},
                AUTH: {data['auth']['username']},
                ERROR: {e}.'''
            )
        page.update()

    saved_data = defaultdict(str, saver.read_data())
    auth = Text("Auth:", size=24)
    user = TextField(label="User", value=saved_data['username'])
    password = TextField(label="Password", value=saved_data['password'])
    body = Text("Data:", size=24)
    host = TextField(label="Host", value=saved_data['host'])
    port = TextField(label="Port", value=saved_data['port'])
    queue = TextField(label="Queue", value=saved_data['queue'])
    send_button = ElevatedButton(text="Submit", on_click=send_handler)
    result_message = Text()

    page.add(
        auth,
        user,
        password,
        body,
        host,
        port,
        queue,
        send_button,
        result_message
    )


if __name__ == '__main__':
    app(target=main)
