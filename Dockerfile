FROM python:3.12-slim

WORKDIR /src

COPY poetry.lock /src
COPY pyproject.toml /src

RUN pip install poetry
RUN poetry install --no-root --no-dev

RUN pip install uvicorn

COPY ./src /src

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]
