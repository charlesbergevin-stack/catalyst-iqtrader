# ---- Build FastAPI API ----
FROM python:3.11-slim

WORKDIR /app
COPY ./apps/api /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:API", "--host", "0.0.0.0", "--port", "8000"]
