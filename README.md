## Event Sender

Event sender для отправки тестовых объектов в очереди RabbitMQ.

Установка зависимостей
```commandline
pip install -r requirements.txt
```

Сборка проекта
```commandline
pyinstaller --windowed --onefile main.py
```
Сборка с картинкой (только на windows и mac os)
```commandline
pyinstaller --windowed --onefile --icon=logo.ico main.py
```
