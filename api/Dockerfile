FROM python:3.11
RUN adduser --disabled-password --gecos '' www-data
WORKDIR /app
COPY . /app
RUN chown -R www-data:www-data /app
USER www-data
RUN pip install streamlit
CMD ["streamlit", "run", "app.py"]
