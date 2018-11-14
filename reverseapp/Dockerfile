FROM python:3.6.2

RUN mkdir -p /home/project/reverseapp
WORKDIR /home/project/reverseapp
COPY requirements.txt /home/project/reverseapp
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/reverseapp

