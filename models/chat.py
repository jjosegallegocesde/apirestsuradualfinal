from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta,motor

chat = Table("chat", meta, 
                Column("id", Integer, primary_key=True), 
                Column("pregunta", String(200)),
                Column("respuesta", String(200))
                )

meta.create_all(motor)