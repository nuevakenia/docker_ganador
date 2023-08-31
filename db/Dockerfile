FROM postgres:bullseye
RUN chown -R www-data:www-data /var/lib/postgresql/data
USER www-data
COPY init.sql /docker-entrypoint-initdb.d/
