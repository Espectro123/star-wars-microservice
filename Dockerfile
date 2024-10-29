FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

COPY src/ ./src/

# Set the environment variable for Python to not buffer the output.
ENV PYTHONUNBUFFERED=1

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app.
EXPOSE 5000

# Run the application when the container launches.
CMD ["python", "-m", "src.infrastructure.api.server"]
