FROM python:3

WORKDIR /app
COPY . /app

RUN pip install beautifulsoup4
RUN pip install aiogram
RUN pip install requests

CMD ["python", "./polling.py"]
