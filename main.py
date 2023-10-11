from fastapi import FastAPI, Form, File, UploadFile
import csv
from pydantic import BaseModel
import requests 


app = FastAPI()

@app.get("/", status_code=200,
    summary="Endpoint raiz",
    description="Endpoint raiz de la API")

def get_contactos():
    response = []

    with open("contactos.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")

        for fila in reader:
            response.append(fila)

    return response

@app.get("/v1/contactos", status_code=298,
    summary="Endpoint para visualizar datos",
    description="Endpoint para visualizar datos")

def get_contactos1():
    response = []

    with open("contactos.csv", "r") as file1, open("contactos_n.csv", "r") as file2:
        reader1 = csv.DictReader(file1, delimiter=",")
        reader2 = csv.DictReader(file2, delimiter=",")

        for fila in reader1:
            response.append(fila)

        for fila in reader2:
            response.append(fila)

    return response

class Contactos(BaseModel):
    id_contacto: int
    nombre: str
    p_apellido: str
    s_apellido: str
    email: str
    telefono: int

@app.post("/v1/static", status_code=200,
    summary="Endpoint para cargar imagen de contacto",
    description="Endpoint para cargar imagen de contacto")
def cargar_imagen(id_contacto: int = Form(...), imagen: UploadFile = Form(...)):
    # Guarda la imagen en un archivo
    with open(f"imagen/{id_contacto}.jpg", "wb") as image_file:
        image_file.write(imagen.file.read())

    return {"mensaje": "Imagen cargada por que si"}

@app.post("/v1/contactos", status_code=201,
    summary="Endpoint para enviar datos",
    description="Endpoint para enviar datos a la API")
def post_contactos(contacto : Contactos):

    with open("contactos_n.csv", "a", newline="") as file:
        fieldnames = ["id_contacto", "nombre", "p_apellido", "s_apellido", "email", "telefono"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        id_contacto= input("Ingrese el Id del contacto: ")
        nombre = input("Ingresa el Nombre: ")
        p_apellido = input("Ingresa el P _Apellido: ")
        s_apellido = input("Ingresa el S_Apellido: ")
        email = input("Ingresa el Email: ")
        telefono = input("Ingresa el Teléfono: ")


    return {"mensaje": "Datos de contacto con éxito"}