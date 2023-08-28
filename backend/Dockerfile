FROM python:3.11
RUN adduser --disabled-password --gecos '' www-data
WORKDIR /app
COPY . /app
RUN chown -R www-data:www-data /app
USER www-data
RUN pip install fastapi uvicorn psycopg2-binary
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
