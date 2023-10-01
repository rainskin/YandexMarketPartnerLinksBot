FROM python:3.8-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install
COPY . .
CMD poetry run python __main__.py