# Start with Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# TODO: What's missing here?
# Hint: Think about uv and pyproject.toml!

# Expose port
EXPOSE 5000

# Run the application using uv
CMD ["uv", "run", "flask", "run", "--host=0.0.0.0"]