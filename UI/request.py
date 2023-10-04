import requests 

URI = "http://localhost:8000/v1/contactos"

response = requests.get(URI)

print(f"GET : {response.text}")
print(f"GET : {response.status_code}")

data = {
  "id_contacto": 3,
  "nombre": "erick",
  "p_apellido": "gutierritos",
  "s_apellido": "hernades",
  "email": "erick@email.com",
  "telefono": 888888
}
response = requests.post(URI,json = data)

print(f"post : {response.text}")
print(f"post : {response.status_code}")