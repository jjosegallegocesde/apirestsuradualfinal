from sqlalchemy import create_engine,MetaData

motor=create_engine("mysql+pymysql://root@localhost:3310/leonardo")
meta=MetaData()


conexion=motor.connect()

