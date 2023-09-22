# Desing Document: API REST CONTACTOS

## 1. Descripcion
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de base de datos [SQLite3](https://www.sqlite.org/) con las siguientes tablas:

### 3.1 Tabla: contactos

|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contacto|int|PRYMARY KEY|Llave primaria de la tabla|
|2|nombre|varchar(100)|Not Null|Nombre del contacto|
|3|primer_apellido|varchar(50)|Not Null|Primer Apellido del contacto|
|4|segundo_apellido|varchar(50)|Not Null|Segundo Apellido del contacto|
|5|email|varchar(100)|Not Null|Email del contacto|
|6|telefono|varchar(13)|Not Null|Telefono del contacto|

### 3.2 Script

CREATE TABLE IF NOT EXISTS contactos (
    id_contacto INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);
