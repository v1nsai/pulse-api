# build
FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# install deps for compiling mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      pkg-config \
      default-libmysqlclient-dev \
      libmariadb-dev-compat libmariadb-dev \
      git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# pipenv install prod build
RUN python -m pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

EXPOSE 8000
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]