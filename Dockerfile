FROM python:3.9-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt && \
    mkdir -p logs migrations/versions && \
    touch logs/bot.log logs/errors.log

COPY . .

CMD alembic upgrade head && python3 bot.py