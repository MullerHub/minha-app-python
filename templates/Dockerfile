# Etapa 1: Build
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Final Image
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .
COPY templates ./templates
EXPOSE 8080
CMD ["python", "app.py"]
