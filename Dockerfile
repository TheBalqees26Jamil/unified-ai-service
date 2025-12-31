# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy project files
COPY . /app

# 4. Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# 5. Expose port
EXPOSE 8000

# 6. Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
