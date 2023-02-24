# test-tasks-chat_project
simple_chat_jango
Чат на Django и Django Rest Framework 
с использованием двух моделей - Thread и Message.


Установка и запуск
1. Клонируйте репозиторий на свой локальный компьютер:
git clone https://github.com/yourusername/simple-chat.git


2. Создайте и активируйте виртуальное окружение:
python -m venv env
source env/bin/activate # для Unix/Mac
env\Scripts\activate # для Windows

3. Установите зависимости:
pip install -r requirements.txt

4. Создайте базу данных и примените миграции:
python manage.py migrate

5. Запустите сервер:
python manage.py runserver

6. Перейдите на localhost:8000 в своем браузере.

API Endpoints
* /api/threads/: получение списка Thread'ов, создание нового Thread'а или удаление Thread'а.
* /api/threads/<int:pk>/messages/: получение списка сообщений для конкретного Thread'а или создание нового сообщения.
* /api/messages/<int:pk>/: отметка сообщения как прочитанного.
* /api/threads/<int:pk>/unread/: получение количества непрочитанных сообщений для текущего пользователя.

Админка
Админка Django доступна по адресу /admin/. Для создания суперпользователя выполните следующую команду:
python manage.py createsuperuser

Используемые технологии
* Python 3
* Django
* Django Rest Framework
* SQLite3
