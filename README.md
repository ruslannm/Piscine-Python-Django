# Piscine-Python-Django
Работа с Postgres
1. Сервер pg_ctl -D ~/.brew/var/postgres start|stop|restart|reload
2. Подключение к кластеру psql -d postgres -U djangouser
2.1. Создать базу данных CREATE DATABASE rush01;
2.2. Создать пользователя CREATE USER djangouser WITH password 'secret';
2.3. Изменить владельца базы данных ALTER DATABASE rush01 OWNER TO djangouser;
