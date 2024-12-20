
from BBDD import sql_interaction


def q101( conn ):

      # Hint:
      # (sp500_Close - LAG(sp500_Close) OVER (ORDER BY Date)) * 100.0 / LAG(sp500:Close) OVER (ORDER BY Date) AS
      # sp500_return,
      # (nasdaq_Close - LAG(nasdaq_Close) OVER (ORDER BY Date)) * 100.0 / LAG(nasdaq_Close) OVER (ORDER BY Date) AS
      # nasdaq_return

      # Hint:
      # strftime('%Y-%m-%d', sp500.Date) == strftime('%Y-%m-%d', nasdaq.Date)

    sql = '''
          '''

    return conn.query(sql)


def q102( conn ):

    sql = '''
          '''

    return conn.query(sql)


def q103( conn ):

    sql = '''
          '''

    return conn.query(sql)


if __name__ == '__main__':

    # Nos conectamos a la base de datos
    conn = sql_interaction("us_macroeconomic_data.sqlite")

    # r01 = q101(conn)

    # print("Tabla \"Pregunta 1\":")
    # print(r01)
    # print()

#     r02 = q102(conn)

#     print("Tabla \"Pregunta 2\":")
#     print(r02)
#     print()

#     r03 = q103(conn)

#     print("Tabla \"Pregunta 3\":")
#     print(r03)
#     print()

