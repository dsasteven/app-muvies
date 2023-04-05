# Importar los módulos necesarios
import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Definir el nombre del archivo SQLite y obtener el directorio base del archivo actual
sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

# Crear la URL de conexión a la base de datos utilizando el nombre del archivo y el directorio base
database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

# Crear un objeto de conexión a la base de datos utilizando la URL de conexión
engine = create_engine(database_url, echo=True)

# Establecer una sesión utilizando la conexión a la base de datos
Sesion = sessionmaker(bind=engine)

# Crear la clase Base utilizando declarative_base
Base = declarative_base()



