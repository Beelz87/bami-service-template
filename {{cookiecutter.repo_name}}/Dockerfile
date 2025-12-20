FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY src ./src
CMD ["uvicorn", "{{cookiecutter.package_name}}.main:app", "--host", "0.0.0.0", "--port", "{{cookiecutter.service_port}}"]
