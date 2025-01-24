# Start with Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY app.py app.py
COPY pyproject.toml pyproject.toml

# install requirements
RUN pip install uv
RUN uv sync

# Run the application using uv
CMD ["uv", "run", "flask", "run", "--host=0.0.0.0"]