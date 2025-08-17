# ---------- Stage 1: build wheels ----------
FROM python:3.10-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# install deps
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      pkg-config \
      default-libmysqlclient-dev \
      libmariadb-dev-compat libmariadb-dev \
      git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Pipfile Pipfile.lock ./

# Export requirements for pip wheel to build
RUN pip install --no-cache-dir pipenv==2023.12.1 && \
    pipenv requirements > requirements.txt

RUN pip wheel --wheel-dir /wheels -r requirements.txt

# ---------- Stage 2: runtime ----------
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
      libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# deps compiled in build stage
COPY --from=builder /wheels /wheels
COPY --from=builder /app/requirements.txt /tmp/requirements.txt

# Install with prebuilt libs
RUN pip install --no-index --find-links=/wheels -r /tmp/requirements.txt \
    && rm -rf /wheels /tmp/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]