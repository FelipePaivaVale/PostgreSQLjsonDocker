FROM postgres:latest

ENV POSTGRES_DB=pessoas 
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=senha123

RUN apt-get update && apt-get install -y python3.11 python3-pip

RUN mkdir /app

COPY . /app

RUN pip3 install psycopg2

EXPOSE 5432

CMD ["postgres"]

CREATE TABLE pessoas(
    id SERIAL PRIMARY KEY,
    dados JSONB
);