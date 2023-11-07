import os
import flet
from src import sender
from config import envconfig as env
from flet import *


def main(page: Page):
    def btnSend(e):
        try:
            sender.send(Host.value, Port.value, Queue.value, User.value, Password.value, 1)
        except:
            t.value = (
                f"Send event failed:  \n"
                f"HOST: '{env.RABBIT_HOST}', \n"
                f"POST: '{env.RABBIT_PORT}', \n"
                f"AUTH: '{User}'. \n"
            )
        page.update()

    t = Text()
    txtAuth = Text("Auth:", size=24)
    User = TextField(label="User", value=f'{env.RABBIT_USER}')
    Password = TextField(label="Password", value=f'{env.RABBIT_PASSWORD}')
    txtData = Text("Data:", size=24)
    Host = TextField(label="Host", value=f'{env.RABBIT_HOST}')
    Port = TextField(label="Port", value=f'{env.RABBIT_PORT}')
    Queue = TextField(label="Queue", value=f'{env.RABBIT_QUEUE_NAME}')
    b = ElevatedButton(text="Submit", on_click=btnSend)

    page.add(
        txtAuth,
        User,
        Password,
        txtData,
        Host,
        Port,
        Queue,
        b,
        t
    )


if __name__ == '__main__':
    flet.app(target=main)
