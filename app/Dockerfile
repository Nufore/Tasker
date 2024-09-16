FROM python:3.11.8-slim

ADD requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ADD main.py /app/main.py
ADD config.py /app/config.py
ADD routes.py /app/routes.py

COPY /database /app/database

COPY .env /app/.env

CMD ["python", "app/main.py"]