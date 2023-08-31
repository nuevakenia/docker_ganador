FROM python:slim-bookworm
WORKDIR /opt/app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/ /opt/app
COPY ./.streamlit/ /opt/app/.streamlit
COPY ./.streamlit/ /opt/.streamlit
RUN chown -R www-data:www-data /opt/app
USER www-data
WORKDIR /opt/
ENTRYPOINT ["streamlit", "run", "/opt/app/app.py", "--server.port"]
CMD ["80"]
