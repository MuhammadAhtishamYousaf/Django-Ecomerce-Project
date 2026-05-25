
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential gcc libpq-dev \
	&& rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
	&& pip install -r /app/requirements.txt

# Copy project
COPY . /app/

# Collect static files (if configured)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Use Gunicorn for production; adjust module path if your project uses a different name
CMD ["gunicorn", "first.wsgi:application", "--bind", "0.0.0.0:8000"]
