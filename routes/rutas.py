from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from models.chat import chat  # Asegúrate de que estás importando la tabla correctamente
from config.db import conexion  # Importa la conexión que has definido

rutas = APIRouter()

@rutas.get("/leonardo")
def consultar_datos():
    """ Consulta todos los registros en la tabla de chat y los devuelve. """
    try:
        # Preparamos la consulta SQL usando 'select'
        stmt = select(chat)  # Usamos 'select' directamente con el objeto de la tabla
        # Ejecutamos la consulta utilizando la conexión directa
        resultado = conexion.execute(stmt).fetchall()
        # Convertimos los resultados en un formato JSON apropiado
        result_list = [{'id': row.id, 'pregunta': row.pregunta, 'respuesta': row.respuesta} for row in resultado]
        return result_list
    except Exception as e:
        # En caso de error en la consulta, lanzamos una excepción HTTP
        raise HTTPException(status_code=500, detail=str(e))
