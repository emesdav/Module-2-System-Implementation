#!/usr/bin/python3
import mysql.connector


class Database:

  def Connect():
    dbConnection = mysql.connector.connect(
      host="127.0.0.1",
      user="admin",
      password="nimda",
      database="HealthDB"
    )

    cursor = dbConnection.cursor()
    return (dbConnection, cursor)

  def Insert(sql, val):
    (dbConnection, cursor) = Database.Connect()
    cursor.execute(sql, val)

    dbConnection.commit()

    return cursor.lastrowid

    Database.Disconnect(dbConnection, cursor)

  def Update(sql, val):
    (dbConnection, cursor) = Database.Connect()
    cursor.execute(sql, val)
    dbConnection.commit()

    return cursor.lastrowid

    Database.Disconnect(dbConnection, cursor)

  def Delete(sql, val):
    (dbConnection, cursor) = Database.Connect()
    cursor.execute(sql, val)

    dbConnection.commit()

    return cursor.rowcount

    Database.Disconnect(dbConnection, cursor)


  def Read(sql, val):
    (dbConnection, cursor) = Database.Connect()

    #Lets allow for when there are no parameters
    if val != "":
      cursor.execute(sql, val)
    else:
      cursor.execute(sql)

    #dbConnection.commit()

    result = cursor.fetchall()
    return result

    Database.Disconnect(dbConnection, cursor)

  def Disconnect(connection, cursor):
    if connection.is_connected():
      cursor.close()
      connection.close()
    
    return True
