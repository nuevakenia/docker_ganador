FROM python:slim-bookworm
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R www-data:www-data /app
USER www-data
ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port"]
CMD ["8000"]
