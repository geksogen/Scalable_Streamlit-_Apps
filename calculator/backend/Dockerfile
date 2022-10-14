# temp stage
FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
COPY calculator.py .
RUN pip install -r requirements.txt
RUN apt install uvicorn

# final stag
FROM python:3.9-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8000"]