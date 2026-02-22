# === STAGE 1: Builder ===
FROM python:3.13-slim AS builder
WORKDIR /app

RUN pip install poetry poetry-plugin-export

COPY pyproject.toml poetry.lock ./
# Используем группу shared для воркера (arq там)
RUN poetry export --with shared --without-hashes --format=requirements.txt > requirements.txt

RUN python -m venv /app/.venv
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

# === STAGE 2: Runtime ===
FROM python:3.13-slim
WORKDIR /app

RUN useradd -m -u 1000 appuser

COPY --from=builder /app/.venv /app/.venv

COPY src/workers /app/src/workers
COPY src/shared /app/src/shared

# Create logs directory and set permissions
RUN mkdir -p /app/data/logs/worker && chown -R appuser:appuser /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app:$PYTHONPATH"

# Запуск воркера
CMD ["arq", "src.workers.notification_worker.worker.WorkerSettings"]
