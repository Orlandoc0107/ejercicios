import sqlite3

# Crear conexión a la base de datos
conexion = sqlite3.connect('ejemplo.db')

# Crear tabla Alumnos con tres columnas
conexion.execute('''CREATE TABLE Alumnos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellido TEXT
                )''')

# Insertar datos en la tabla Alumnos
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Juan', 'Pérez')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('María', 'García')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Pedro', 'López')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Lucía', 'Fernández')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Javier', 'González')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Ana', 'Martínez')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Marta', 'Ruiz')")
conexion.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Pablo', 'Sánchez')")

# Guardar cambios en la base de datos
conexion.commit()

# Buscar un alumno por nombre y mostrar sus datos por consola
nombre_busqueda = 'Juan'
resultado = conexion.execute(f"SELECT * FROM Alumnos WHERE nombre = '{nombre_busqueda}'").fetchone()
if resultado is None:
    print(f"No se encontró ningún alumno con nombre {nombre_busqueda}")
else:
    print(f"Datos del alumno con nombre {nombre_busqueda}:")
    print(f"ID: {resultado[0]}")
    print(f"Nombre: {resultado[1]}")
    print(f"Apellido: {resultado[2]}")

# Cerrar conexión a la base de datos
conexion.close()
