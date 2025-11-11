import mysql.connector
import datetime
from mysql.connector import errorcode


cursor = None
cnx = None


def conectarBase():
    global cnx, cursor

    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="telo")
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)
def consulta_select_todo():
    Consulta = "SELECT * FROM clientes;"
    cursor.execute(Consulta)
    for x in cursor:
        print(x)
    return cursor.fetchall()
def insertar_reserva(ID_habitacion, ID_cliente, fecha_entrada, fecha_salida):
    consulta = "INSERT INTO reservas (ID_habitacion, ID_cliente, fecha_entrada, fecha_salida) VALUES (%s,%s,%s,%s)"
    cursor.execute(consulta,(ID_habitacion, ID_cliente, fecha_entrada, fecha_salida))
    cnx.commit()
    return cursor.lastrowid
def insertar_cliente(nombre, DNI, telefono, historial_reservas):

    sql = "INSERT INTO clientes (nombre, DNI, telefono, historial_reservas)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(nombre, DNI, telefono, historial_reservas))
    cnx.commit()
    return cursor.lastrowid
def consulta_select_dni(DNI):
    Consulta = f"SELECT * FROM reservas WHERE ID_cliente in(SELECT ID FROM clientes WHERE DNI = {DNI};"
    cursor.execute(Consulta)
    return cursor.fetchall
def Menu():
    conectarBase()
    seguimos = True
    while seguimos:
        Opcion1 = int(input("""
        --------------------------
        | 1-ver beneficios       |
        | 2-buscar cliente       |
        | 3-reservar habitaciones|
        | 4-solicitar servicios  |
        | 5-Kill Your self       | 
        --------------------------
        ingrese un opcion: """))
        if Opcion1 == 1:
            print("beneficios")
        elif Opcion1 == 2:
            print(consulta_select_todo())
        elif Opcion1 == 3:
            insertar_reserva()
            print("Se ha reservado correctamente")
        elif Opcion1 == 4:
            print("beneficios")
        elif Opcion1 == 5:
            print("cerrando programa")
            seguimos = False

    if cnx.is_connected():
        cnx.close()
        print("La conexión a la base de datos ha sido cerrada.")

fecha_entrada = input("Fecha")
fecha_entrada = fecha_entrada.strftime('%d/%m/%Y')
print(fecha_entrada)
