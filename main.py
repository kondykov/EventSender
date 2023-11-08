from collections import defaultdict

import flet as ft

from src import sender, saver


def main(page: ft.Page):
    def send_handler(e):
        data = {
            'host': host.value,
            'port': port.value,
            'queue': queue.value,
            'username': user.value,
            'password': password.value,
            'body': body_json.value
        }

        ok, err = sender.send(data, body)
        if ok:
            result_message.value = f'Сообщение успешно отправлено в очередь {data["queue"]}'
            saver.save_data(data)
        else:
            result_message.value = f'Ошибка отправки: {err.args}'
        page.update()

    saved_data = defaultdict(str, saver.read_data())
    auth = ft.Text("Auth:", size=24)
    user = ft.TextField(label="User", value=saved_data['username'])
    password = ft.TextField(label="Password", value=saved_data['password'],
                            password=True, can_reveal_password=True)
    body = ft.Text("Data:", size=24)
    host = ft.TextField(label="Host", value=saved_data['host'])
    port = ft.TextField(label="Port", value=saved_data['port'])
    queue = ft.TextField(label="Queue", value=saved_data['queue'])
    send_button = ft.ElevatedButton(text="Submit", on_click=send_handler)
    body_json = ft.TextField(label="Body", multiline=True, value=saved_data['body'])
    result_message = ft.Text()

    page.add(
        auth,
        user,
        password,
        body,
        host,
        port,
        queue,
        body_json,
        send_button,
        result_message
    )


if __name__ == '__main__':
    ft.app(target=main)
