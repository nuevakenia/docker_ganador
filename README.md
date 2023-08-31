# Manual de Uso para Despliegue del challenge ganador 🥵🥵🥵

## Tabla de Contenidos
- [Manual de Uso para Despliegue del challenge ganador 🥵🥵🥵](#manual-de-uso-para-despliegue-del-challenge-ganador-)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
    - [Bienvenido a la Documentación del Challenge Ganador 🐳](#bienvenido-a-la-documentación-del-challenge-ganador-)
      - [Criterios de Selección de Imágenes 🎯](#criterios-de-selección-de-imágenes-)
      - [Orquestación con Docker Compose 🎶](#orquestación-con-docker-compose-)
  - [Requisitos Previos](#requisitos-previos)
  - [Clonación del Repositorio](#clonación-del-repositorio)
  - [Descargar e Instalar Docker Desktop](#descargar-e-instalar-docker-desktop)
    - [Instalación](#instalación)
  - [Verificación del Docker Daemon](#verificación-del-docker-daemon)
  - [Configuración Inicial](#configuración-inicial)
    - [Configuraciones Preestablecidas](#configuraciones-preestablecidas)
      - [Modificación de Datos de Prueba en la Base de Datos](#modificación-de-datos-de-prueba-en-la-base-de-datos)
  - [Despliegue con Docker Compose](#despliegue-con-docker-compose)
  - [Validación del Despliegue](#validación-del-despliegue)
  - [Uso de la Aplicación](#uso-de-la-aplicación)
  - [FAQ](#faq)
    - [¿Puedo ingresar al backend de manera local con \`0.0.0.0:8000\`?](#puedo-ingresar-al-backend-de-manera-local-con-00008000)
    - [¿Puedo acceder a la base de datos desde mi dispositivo host?](#puedo-acceder-a-la-base-de-datos-desde-mi-dispositivo-host)
    - [¿Si elimino el contenedor, los reportes quedan almacenados?](#si-elimino-el-contenedor-los-reportes-quedan-almacenados)
    - [¿Cómo puedo cambiar las variables de entorno de los servicios?](#cómo-puedo-cambiar-las-variables-de-entorno-de-los-servicios)


## Introducción

### Bienvenido a la Documentación del Challenge Ganador 🐳

Esta solución ha sido construida utilizando varias tecnologías robustas y confiables:

- **Base de Datos:** PostgreSQL 15, basada en Debian Bullseye.
- **Backend:** FastAPI con Uvicorn, utilizando la imagen Python 3.11:slim-bookworm.
- **API/Frontend:** Streamlit, también utilizando la imagen Python 3.11:slim-bookworm.

#### Criterios de Selección de Imágenes 🎯

Las imágenes de Docker utilizadas en este proyecto fueron seleccionadas siguiendo los siguientes criterios:

1. **Certificación "Docker Official Image":** Garantía de mantenimiento y actualizaciones por parte de la comunidad.
2. **Menor Cantidad de Vulnerabilidades:** Elección de imágenes con el menor número de vulnerabilidades conocidas.
3. **Requerimientos Mínimos:** Capacidad para satisfacer las dependencias y necesidades funcionales de las bibliotecas utilizadas.
4. **Optimización del Tamaño:** Uso de imágenes ligeras para acelerar el tiempo de despliegue y reducir el consumo de recursos.

#### Orquestación con Docker Compose 🎶

Se ha utilizado Docker Compose para orquestar la creación y configuración de los contenedores, así como de la red. Este enfoque busca adherirse a las buenas prácticas aprendidas en el workshop anterior.

Espero que el Challenge cumpla con las espectivas y sea el ganador, por que si nó me mato 💀.

---
## Requisitos Previos

Antes de seguir las instrucciones, asegúrese de tener una terminal, PowerShell o consola abierta en su sistema.

---

## Clonación del Repositorio

Para clonar el repositorio, utilice el siguiente comando en su terminal, o en su IDE/aplicación favorita. Si aún no tiene instalado Git, puede [descargarlo aquí](https://git-scm.com/downloads).

\`\`\`bash
git clone https://github.com/nuevakenia/docker_ganador.git
\`\`\`

---

## Descargar e Instalar Docker Desktop

Descargue Docker Desktop según su sistema operativo:

- [Docker para Windows](https://www.docker.com/products/docker-desktop)
- [Docker para Linux](https://docs.docker.com/engine/install/)
- [Docker para Mac](https://docs.docker.com/docker-for-mac/install/)

### Instalación

Siga las instrucciones específicas para su sistema operativo para completar la instalación.

---

## Verificación del Docker Daemon

Para verificar que Docker Daemon se haya iniciado correctamente, ejecute:

\`\`\`bash
docker --version
\`\`\`

Si todo está bien, debería ver la versión de Docker como salida.

---

## Configuración Inicial

Abra la terminal, navegue hasta la carpeta del repositorio clonado y ejecute \`ls\` para confirmar que los archivos y carpetas necesarios están presentes.

\`\`\`bash
cd docker_ganador
ls
\`\`\`

Debería ver una estructura similar a:

\`
README.md  backend  docker-compose.yml  api  db
\`

### Configuraciones Preestablecidas

Todas las configuraciones relacionadas con variables de entorno, credenciales y datos de prueba (mock data) para la base de datos y los servicios de backend y API ya están preestablecidas.

#### Modificación de Datos de Prueba en la Base de Datos

Si desea modificar los datos de prueba de la base de datos, puede hacerlo editando el archivo `init.sql`. Este archivo se encuentra en la ruta `/db`.

Modificación de Variables de Entorno
Para cambiar las variables de entorno, por favor consulte la sección de Preguntas Frecuentes `FAQ` ubicada en la parte final de este documento.

---

## Despliegue con Docker Compose

Para construir y desplegar los contenedores, ejecute el siguiente comando:

\`\`\`bash
docker-compose up --build
\`\`\`

---

## Validación del Despliegue

Busque mensajes similares a los siguientes para confirmar que los contenedores se han desplegado correctamente:

\`
docker_ganador-db-1         | 2023-08-31 02:16:27.586 UTC [1] LOG:  database system is ready to accept connections
docker_ganador-backend-1    | INFO:     Started server process [1]
docker_ganador-backend-1    | INFO:     Waiting for application startup.
docker_ganador-backend-1    | INFO:     Application startup complete.
docker_ganador-backend-1    | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
docker_ganador-streamlit-1  |
docker_ganador-streamlit-1  |   You can now view your Streamlit app in your browser.
docker_ganador-streamlit-1  |
docker_ganador-streamlit-1  |   Network URL: http://172.18.0.3:80
docker_ganador-streamlit-1  |   External URL: http://200.83.159.136:80
...
\`

---

## Uso de la Aplicación

1. Abra su navegador y navegue hasta \`http://0.0.0.0:80\`.
2. Seleccione la sucursal y el rango de fechas(marcaciones disponibles desde el 2023/03/27 - 2023/04/06 si no hay marcaciones no se podrá descargar el reporte).
3. Haga clic en "Enviar".
4. Haga clic en "Visualizar Reportes" y refresque la página haciendo click en el botón hasta que el reporte cambie de estado a "Finalizado" y se pueda descargar.

---

## FAQ

### ¿Puedo ingresar al backend de manera local con \`0.0.0.0:8000\`?

No, debido a las configuraciones de \`network\` en \`docker-compose.yml\`, solo es posible acceder desde el servicio de api streamlit.

### ¿Puedo acceder a la base de datos desde mi dispositivo host?

No, por las mismas razones mencionadas anteriormente.

### ¿Si elimino el contenedor, los reportes quedan almacenados?

Sí, gracias al volumen asignado, los datos son persistentes.

### ¿Cómo puedo cambiar las variables de entorno de los servicios?

Para cambiar las variables de entorno, es necesario abrir el archivo `.env` ubicado en la carpeta raíz del repositorio. En este archivo, puede agregar, modificar o eliminar las variables de entorno según sus necesidades.

Por ejemplo, su archivo `.env` podría lucir de la siguiente manera:

\`\`\`bash
POSTGRES_USER=ganador
POSTGRES_PASSWORD=666
POSTGRES_DB=challenge
DB_USER=ganador
DB_PASS=666
DB_HOST=db
DB_NAME=challenge
ENDPOINT_URL="http://backend:8000/"
BACKEND_PORT=8000
API_PORT=80
\`\`\`

Si elimina, agrega o modifica el nombre de alguna de las variables de entorno, deberá realizar cambios correspondientes en el archivo `docker-compose.yml`.

En la sección de cada contenedor, encontrará el bloque `environment`. A continuación, se muestra un ejemplo:

\`\`\`yaml
environment:
  POSTGRES_USER: ${POSTGRES_USER}
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  POSTGRES_DB: ${POSTGRES_DB}
\`\`\`

Aquí, el nombre a la izquierda (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, etc.) representa la variable de entorno que el servicio utilizará. El valor a la derecha (`${POSTGRES_USER}`, `${POSTGRES_PASSWORD}`, `${POSTGRES_DB}`, etc.) hace referencia al nombre de la variable que se encuentra en su archivo `.env`.


---

