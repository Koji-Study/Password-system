FROM python:3.8
RUN pip install django==3.2.7
WORKDIR /Django
RUN django-admin startproject djangoproj
