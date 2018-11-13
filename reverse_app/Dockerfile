FROM python:3.6.2

RUN mkdir -p /home/project/reverse_app
WORKDIR /home/project/reverse_app
COPY requirements.txt /home/project/reverse_app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/reverse_app

