# temp stage
FROM python:3.9-slim as builder

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /code/requirements.txt
COPY ./calculator.py /code/calculator.py
RUN pip install -r /code/requirements.txt

# final stag
FROM python:3.9-slim
COPY --from=builder /opt/venv /opt/venv
WORKDIR /code
ENV PATH="/opt/venv/bin:$PATH"
CMD ["uvicorn", "code.fast_api:app", "--host", "0.0.0.0", "--port", "8000"]