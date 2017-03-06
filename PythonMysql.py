# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:07:22 2017

@author: Mache
"""
# 0. Tener instalado MySql
# 1. Crear la base de datos por consola desde MySql : create database BaseDeDatosPython;
# 2. Tener instalado el módulo de MySQLdb

#!/usr/bin/python

import MySQLdb

# -----------------------------------------------
# Conceptos básicos
# -----------------------------------------------

# Conexión con la base de datos: hosting-usuario-password-nombre base de datos
bd = MySQLdb.connect("localhost","root","Usuario","baseDeDatos" )

# Cursor para operar la BDD
cursor = bd.cursor()

# Consulta simple usando execute
print "numero registros devueltos: %d" % cursor.execute("SELECT VERSION()")

#Extraer una fila de la respuesta con fetchone()
print "Versión: %s" % cursor.fetchone()

# -----------------------------------------------
# Crear tablas simples
# -----------------------------------------------

# String de una tabla (\ permite escribir en varias líneas sin cortar el string)
TablaSql = "CREATE TABLE IF NOT EXISTS ARTICULO (\
         NOMBRE  CHAR(20) NOT NULL,\
         STOCK  INT,\
         PRECIO FLOAT\
         )"
# Se ejecuta la consulta
cursor.execute(TablaSql)

# -----------------------------------------------
# Ingresar registro a tabla
# -----------------------------------------------
"""
# String para insertar registro
InsertSql = "INSERT INTO ARTICULO (NOMBRE,\
         STOCK, PRECIO)\
         VALUES ('Notebook Lenovo', 22, 599.99)"

try:
   # Se ejecuta la consulta
   cursor.execute(InsertSql)
   # Se efectuan los cambios en la base de datos
   bd.commit()
except:
   # Si hay error, se revierte la operación
   bd.rollback()
"""

# -----------------------------------------------
# Modificar registros de una tabla
# -----------------------------------------------

# String de la consulta 
UpdateSql = "UPDATE ARTICULO SET PRECIO = 250.99 WHERE Nombre = 'Notebook'"

try:
   # Se ejecuta la consulta
   cursor.execute(UpdateSql)
   # Se efectuan los cambios en la base de datos
   bd.commit()
except:
   # Si hay error, se revierte la operación
   bd.rollback()
     
# -----------------------------------------------
# Eliminar registros de una tabla
# -----------------------------------------------

# String de la consulta 
DeleteSql = "DELETE FROM ARTICULO WHERE NOMBRE='Notebook'"

try:
   # Se ejecuta la consulta
   cursor.execute(DeleteSql)
   # Se efectuan los cambios en la base de datos
   bd.commit()
except:
   # Si hay error, se revierte la operación
   bd.rollback()
   
# -----------------------------------------------
# Obtener registros de una tabla
# -----------------------------------------------
# String de la consulta 
ConsultaSql = "SELECT * FROM ARTICULO"

try:
   # Se ejecuta la consulta
   cursor.execute(ConsultaSql)
   # Se obtienen los registros en lista de listas
   Registros = cursor.fetchall()
   for registro in Registros:
      Nombre = registro[0]
      Stock = registro[1]
      Precio = registro[2]

      # Imprimimos los resultados obtenidos
      print "Nombre = %s, Stock = %d, Precio = %f" % (Nombre, Stock, Precio)
except:
   print "Error: No se puede obtener la información de la base de datos".decode("utf8")
   
#Cerrar conexión
bd.close()



