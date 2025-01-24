# Start with Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

RUN pip install uv
RUN uv sync
# Expose port
EXPOSE 5000

# Run the application using uv
CMD ["uv", "run", "flask", "run", "--host=0.0.0.0"]