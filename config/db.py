from sqlalchemy import create_engine,MetaData

motor=create_engine("mysql+pymysql://root@localhost:3306/pruebafast")
meta=MetaData()


conexion=motor.connect()

