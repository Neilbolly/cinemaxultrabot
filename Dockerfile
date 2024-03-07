FROM python:3.10-slim
WORKDIR /app

# Copy just the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install build dependencies only if requirements.txt has changed
RUN apt-get update \
    && apt-get install --no-install-recommends -y git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -U -r requirements.txt \
    && apt-get purge -y git \
    && apt-get autoremove -y

# Copy the rest of the application code
COPY . .

# CMD or ENTRYPOINT command
CMD ["python", "bot.py"]
