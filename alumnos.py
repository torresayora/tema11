import sqlite3

def main():
    crear_alumno(1,'Roberto', 'Torres Ayora')
    crear_alumno(2,'Gabriela', 'González Ramos')
    crear_alumno(3,'Jessica Alejandra', 'Torres Ayora')
    crear_alumno(4,'Leticia', 'González Ramos')
    crear_alumno(5,'Claudia', 'Torres Hirashi')
    crear_alumno(6,'Susana', 'Torres Hirashi')
    crear_alumno(7,'Rocío', 'González Ramos')
    crear_alumno(8,'Cecilia', 'González Ramos')
   

    buscar_alumno('Roberto')


def crear_alumno(matricula, nombre, apellido):
    conn = sqlite3.connect('alumnado.db')
    cursor = conn.cursor()

    query = f"INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)"
    row = cursor.execute(query, (matricula, nombre, apellido))
    
    conn.commit()
    cursor.close()
    conn.close()

def buscar_alumno(nombre):
    conn = sqlite3.connect('alumnado.db')
    cursor = conn.cursor()

    query = f"SELECT nombre FROM alumnos WHERE nombre = '{nombre}'"
    row = cursor.execute(query)
    
    data = row.fetchone()
    print(data)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
