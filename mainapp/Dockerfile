FROM python:3.6.2

RUN mkdir -p /home/project/mainapp
WORKDIR /home/project/mainapp
COPY requirements.txt /home/project/mainapp
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/mainapp

