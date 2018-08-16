import mysql.connector


config = {
   "user":"juan",
    "password":"juan",
    "host":"127.0.0.1",
    "database": 'usuarios'
}

conexion = mysql.connector.connect(**config)
print(conexion)


cursor = conexion.cursor()
cursor.execute("CREATE TABLE TABLA_PY (id INT, datos VARCHAR(900));")


