from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from routes.rutas import rutas

app=FastAPI()

# Habilitar CORS para permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen. Ajusta según sea necesario.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP. Ajusta según sea necesario.
    allow_headers=["*"],  # Permite todas las cabeceras. Ajusta según sea necesario.
)

app.include_router(rutas)