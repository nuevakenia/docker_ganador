FROM postgres:bullseye
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 123
ENV POSTGRES_DB challenge
RUN chown -R www-data:www-data /var/lib/postgresql/data
USER www-data
COPY init.sql /docker-entrypoint-initdb.d/
