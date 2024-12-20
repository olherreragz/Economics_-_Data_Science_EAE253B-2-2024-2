
from BBDD import sql_interaction


def q101( conn ):

      # Hint:
      # (sp500.Close - LAG(sp500.Close) OVER (ORDER BY Date)) * 100.0 / LAG(sp500.Close) OVER (ORDER BY Date) AS
      # sp500_return,
      # (nasdaq.Close - LAG(nasdaq.Close) OVER (ORDER BY Date)) * 100.0 / LAG(nasdaq.Close) OVER (ORDER BY Date) AS
      # nasdaq_return

      # Hint:
      # strftime('%Y-%m-%d', sp500.Date) == strftime('%Y-%m-%d', nasdaq.Date)

    sql = '''
            SELECT 
                  Date,
                  (sp500_Close - LAG(sp500_Close) OVER (ORDER BY Date)) * 100.0 / LAG(sp500_Close) OVER (ORDER BY Date) AS
                  sp500_return,
                  (nasdaq_Close - LAG(nasdaq_Close) OVER (ORDER BY Date)) * 100.0 / LAG(nasdaq_Close) OVER (ORDER BY Date) AS
                  nasdaq_return
            FROM(
                  SELECT sp500.Date as Date, sp500.Close as sp500_Close, nasdaq.Close as nasdaq_Close
                  FROM(
                        sp500 INNER JOIN nasdaq ON
                        strftime('%Y-%m-%d', sp500.Date) == strftime('%Y-%m-%d', nasdaq.Date)
                  )
            )
          '''

    return conn.query(sql)


def q102( conn ):

    sql = '''
          WITH TABLA_TEMPORAL_AUXILIAR_1 AS (
            SELECT 
                  Date,
                  (sp500_Close - LAG(sp500_Close) OVER (ORDER BY Date)) * 100.0 / LAG(sp500_Close) OVER (ORDER BY Date) AS
                  sp500_return,
                  (nasdaq_Close - LAG(nasdaq_Close) OVER (ORDER BY Date)) * 100.0 / LAG(nasdaq_Close) OVER (ORDER BY Date) AS
                  nasdaq_return
            FROM(
                  SELECT sp500.Date as Date, sp500.Close as sp500_Close, nasdaq.Close as nasdaq_Close
                  FROM(
                        sp500 INNER JOIN nasdaq ON
                        strftime('%Y-%m-%d', sp500.Date) == strftime('%Y-%m-%d', nasdaq.Date)
                  )
            )
          )
          SELECT
            TABLA_TEMPORAL_AUXILIAR_1.*,
            us_macrodata.TB3SMFFM
          FROM TABLA_TEMPORAL_AUXILIAR_1 INNER JOIN us_macrodata ON
                  strftime('%Y-%m-%d', TABLA_TEMPORAL_AUXILIAR_1.Date) == strftime('%Y-%m-%d', us_macrodata.Date)
          '''

    return conn.query(sql)


def q103( conn ):

    sql = '''

         SELECT
            Regime,
            AVG(sp500_return),
            AVG(nasdaq_return),
            AVG(TB3SMFFM)
         FROM(
                  WITH TABLA_TEMPORAL_AUXILIAR_2 AS (
                        WITH TABLA_TEMPORAL_AUXILIAR_1 AS (
                              SELECT 
                                    Date,
                                    (sp500_Close - LAG(sp500_Close) OVER (ORDER BY Date)) * 100.0 / LAG(sp500_Close) OVER (ORDER BY Date) AS
                                    sp500_return,
                                    (nasdaq_Close - LAG(nasdaq_Close) OVER (ORDER BY Date)) * 100.0 / LAG(nasdaq_Close) OVER (ORDER BY Date) AS
                                    nasdaq_return
                              FROM(
                                    SELECT sp500.Date as Date, sp500.Close as sp500_Close, nasdaq.Close as nasdaq_Close
                                    FROM(
                                          sp500 INNER JOIN nasdaq ON
                                          strftime('%Y-%m-%d', sp500.Date) == strftime('%Y-%m-%d', nasdaq.Date)
                                    )
                              )
                        )
                        SELECT
                              TABLA_TEMPORAL_AUXILIAR_1.*,
                              us_macrodata.TB3SMFFM
                        FROM TABLA_TEMPORAL_AUXILIAR_1 INNER JOIN us_macrodata ON
                                    strftime('%Y-%m-%d', TABLA_TEMPORAL_AUXILIAR_1.Date) == strftime('%Y-%m-%d', us_macrodata.Date)
                  )
                  SELECT TABLA_TEMPORAL_AUXILIAR_2.Date,
                              sp500_return,
                              nasdaq_return,
                              TB3SMFFM,
                              Regime
                  FROM TABLA_TEMPORAL_AUXILIAR_2 INNER JOIN Recessions ON
                              strftime('%Y-%m-%d', TABLA_TEMPORAL_AUXILIAR_2.Date) == strftime('%Y-%m-%d', Recessions.Date)
         )
         GROUP BY Regime
          '''

    return conn.query(sql)


if __name__ == '__main__':

    # Nos conectamos a la base de datos
    conn = sql_interaction("us_macroeconomic_data.sqlite")

    r01 = q101(conn)

    print("Tabla \"Pregunta 1\":")
    print(r01)
    print()

    r02 = q102(conn)

    print("Tabla \"Pregunta 2\":")
    print(r02)
    print()

    r03 = q103(conn)

    print("Tabla \"Pregunta 3\":")
    print(r03)
    print()

