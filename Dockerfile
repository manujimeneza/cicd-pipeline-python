FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes --only-binary=:all: -r requirements.txt
COPY app/ ./app/
RUN groupadd --system app && useradd --system --gid app --home-dir /app --no-create-home app
USER app
EXPOSE 8000
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "app.app:app"]
