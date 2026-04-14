# syntax=docker/dockerfile:1
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/m-spangenberg/demo-python-package"

WORKDIR /app

COPY . /app

RUN pip install .

CMD ["python3", "-m", "python_demo_package_9999.demo"]
