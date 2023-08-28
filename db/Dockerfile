FROM postgres:latest
ENV POSTGRES_USER usuario
ENV POSTGRES_PASSWORD contraseña
ENV POSTGRES_DB nombre_db
USER www-data
COPY init.sql /docker-entrypoint-initdb.d/
