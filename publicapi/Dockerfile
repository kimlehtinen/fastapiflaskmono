FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app


CMD ["python", "-m", "flask", "--app", "publicapi.app", "run", "--host=0.0.0.0", "--port=5000"]
