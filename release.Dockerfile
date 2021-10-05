FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

RUN python3 --version
RUN pip3 --version

WORKDIR /app
COPY ./app /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get install openssl

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80","--timeout", "90", "app:app"]