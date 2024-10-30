FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

CMD ["uvicorn", "resultsapi.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
