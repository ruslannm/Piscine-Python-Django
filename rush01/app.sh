#!/bin/sh 
python3 -m venv django_venv
source django_venv/bin/activate

#python3 -m pip3 install --upgrade pip
pip3 install -r requirements.txt


#django-admin startproject d08 .
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
#python3 manage.py runserver

cd django-forum/rush01 
python3 setup.py sdist
pip3 install dist/django-myforum-0.1.tar.gz
cd ..