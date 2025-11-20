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
    global cnx,cursor
    Consulta = "SELECT * FROM clientes;"
    cursor.execute(Consulta)
    for x in cursor:
        print(x)
    return cursor.fetchall()
def insertar_reserva_habitacion(ID_habitacion, ID_cliente, año_entrada, mes_entrada, dia_entrada, año_salida, mes_salida, dia_salida,ID_servicio):
    fecha_entrada = datetime.date(año_entrada, mes_entrada, dia_entrada)
    fecha_salida = datetime.date(año_salida, mes_salida, dia_salida)
    consulta = "INSERT INTO reservas (ID_habitacion, ID_cliente, fecha_entrada, fecha_salida,ID_servicio) VALUES (%s,%s,%s,%s)"
    cursor.execute(consulta,(ID_habitacion, ID_cliente, fecha_entrada, fecha_salida,ID_servicio))
    cnx.commit()
    return cursor.lastrowid
def insertar_cliente(nombre, DNI, telefono, año_entrada, mes_entrada, dia_entrada):
    usuarios = consulta_select_todo()
    print(usuarios)
    for usuario in usuarios:
        if usuario["DNI"] == DNI:
            print("El Cliente ya existe")
            return None
    fecha_entrada = datetime.date(año_entrada, mes_entrada, dia_entrada)
    sql = "INSERT INTO clientes (nombre, DNI, telefono, ultima_reserva)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(nombre, DNI, telefono,fecha_entrada))
    cnx.commit()
    return cursor.lastrowid
def consulta_select_dni(DNI):
    Consulta = f"SELECT * FROM reservas WHERE ID_cliente in(SELECT ID FROM clientes WHERE DNI = {DNI};"
    cursor.execute(Consulta)
    return cursor.fetchall
def consulta_select_todo_servicios():
    global cnx,cursor
    Consulta = "SELECT * FROM servicios;"
    cursor.execute(Consulta)
    for x in cursor:
        print(x)
    return cursor.fetchall()
def consulta_update_reserva(ID_Reserva, ID):
    Consulta = f"UPDATE servicios SET ID_Reserva ={ID_Reserva} WHERE ID = {ID} "
    cursor.execute(Consulta)
    return cursor.fetchall
def insertar_reserva(ID_habitacion, ID_cliente, año_entrada, mes_entrada, dia_entrada, año_salida, mes_salida, dia_salida, ID_servicio):
    fecha_entrada = datetime.date(año_entrada, mes_entrada, dia_entrada)
    fecha_salida = datetime.date(año_salida, mes_salida, dia_salida)
    consulta = "INSERT INTO reservas (ID_habitacion, ID_cliente, fecha_entrada, fecha_salida, ID_servicio) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(consulta,(ID_habitacion, ID_cliente, fecha_entrada, fecha_salida, ID_servicio))
    cnx.commit()
    return cursor.lastrowid

def Menu():
    conectarBase()
    seguimos = True
    while seguimos:
        Opcion1 = int(input("""
        --------------------------
        | 1-Show All Clients     |
        | 2-ingresar cliente     |
        | 3-reservar habitaciones|
        | 4-ver servicios        |
        | 5-solicitar servicios  |
        | 6-Kill Your self       | 
        --------------------------
        ingrese un opcion: """))
        if Opcion1 == 1:
            print(consulta_select_todo())
        elif Opcion1 == 2:
            nombre = input("Ingrese el nombre: ")
            DNI = input("Ingrese el DNI: ")
            telefono = input("Ingrese el Telefono: ")
            año_entrada = int(input("ingrese año entrada: "))
            mes_entrada = int(input("ingrese mes entrada: "))
            dia_entrada = int(input("ingrese día entrada: "))
            insertar_cliente(nombre, DNI, telefono,año_entrada, mes_entrada, dia_entrada)
        elif Opcion1 == 3:
            id = int(input("ingrese id habitacion: "))
            id_cliente = int(input("ingrese id cliente: "))
            ID_servicio = int(input("ingrese ID servicio: "))
            año_entrada = int(input("ingrese año entrada: "))
            mes_entrada = int(input("ingrese mes entrada: "))
            dia_entrada = int(input("ingrese día entrada: "))
            año_salida = int(input("ingrese año salida: "))
            mes_salida = int(input("ingrese mes salida: "))
            dia_salida = int(input("ingrese día salida: "))
            insertar_reserva(id,id_cliente,año_entrada,mes_entrada, dia_entrada, año_salida, mes_salida, dia_salida,ID_servicio)
        elif Opcion1 == 4:
            print(consulta_select_todo_servicios())
        elif Opcion1 == 5:
            id = int(input("ingrese id habitacion: "))
            id_cliente = int(input("ingrese id cliente: "))
            año_entrada = int(input("ingrese año entrada: "))
            mes_entrada = int(input("ingrese mes entrada: "))
            dia_entrada = int(input("ingrese día entrada: "))
            año_salida = int(input("ingrese año salida: "))
            mes_salida = int(input("ingrese mes salida: "))
            dia_salida = int(input("ingrese día salida: "))
            ID_servicio  = int(input("""
                               --------------------------
                               | 1-Desayuno buffet      |
                               | 2-Spa                  |
                               | 3-Servicio de limmpieza|
                               | 4-Pileta               |
                               | 5-estacionamiento      |
                               | 6-servicios tecnicos   |
                               | 7-desayuno a la cama   | 
                               --------------------------
                               ingrese un opcion: """))
            insertar_reserva(id,id_cliente,año_entrada,mes_entrada, dia_entrada, año_salida, mes_salida, dia_salida,ID_servicio)
        elif Opcion1 == 6:
            print("cerrando programa")
            seguimos = False

    if cnx.is_connected():
        cnx.close()
        print("La conexión a la base de datos ha sido cerrada.")

Menu()




