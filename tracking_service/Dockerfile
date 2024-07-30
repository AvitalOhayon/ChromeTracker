FROM python:3.10.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV PYTHONPATH=/app
ENV FLASK_APP=tracking.app:app
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]

