FROM python:3.6.2

RUN mkdir -p /home/project/main_app
WORKDIR /home/project/main_app
COPY requirements.txt /home/project/main_app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/main_app

