FROM python:3.13-slim
WORKDIR /app
EXPOSE 8000
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "api.main:app"]