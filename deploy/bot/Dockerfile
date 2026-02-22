# === STAGE 1: Builder ===
FROM python:3.13-slim AS builder
WORKDIR /app

RUN pip install poetry poetry-plugin-export

COPY pyproject.toml poetry.lock ./
# Используем группы bot и shared (там логгер и т.д.)
RUN poetry export --with bot,shared --without-hashes --format=requirements.txt > requirements.txt

RUN python -m venv /app/.venv
RUN /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

# === STAGE 2: Runtime ===
FROM python:3.13-slim
WORKDIR /app

RUN useradd -m -u 1000 appuser

COPY --from=builder /app/.venv /app/.venv

COPY src/telegram_bot /app/src/telegram_bot
COPY src/shared /app/src/shared

RUN mkdir -p /app/data/logs/bot && chown -R appuser:appuser /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app:$PYTHONPATH"

# Start bot
CMD ["python", "-m", "src.telegram_bot.app_telegram"]
