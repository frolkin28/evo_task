File sharing task

You can try application on http://34.76.36.43:5000

To deploy project:

1) create .env file

Example:
# Postgres
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_PORT=<port>
POSTGRES_DB=<db_name>
POSTGRES_HOST=<db_container_name>

# timezone
TZ=Europe/Kiev

2) run make start