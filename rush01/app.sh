#!/bin/sh 
python3 -m venv django_venv
source django_venv/bin/activate

#python3 -m pip3 install --upgrade pip
#pip3 install -r requirement.txt


#django-admin startproject d08 .
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
#python3 manage.py runserver

cd django-gallery
python3 setup.py sdist
pip3 install dist/django-gallery-0.1.tar.gz
cd ..