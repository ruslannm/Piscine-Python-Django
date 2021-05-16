#!/bin/sh 
gunicorn -c gunicorn.conf.py rush01.wsgi