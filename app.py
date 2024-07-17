from fastapi import FastAPI

from routes.rutas import rutas

app=FastAPI()

app.include_router(rutas)