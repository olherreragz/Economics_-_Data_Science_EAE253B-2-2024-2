
from BBDD import sql_interaction


def q101( conn ):

    sql = '''
        SELECT AVG(Close) as precio_promedio, STDEV(Close) as SD, MIN(Close) as minimo, MAX(Close) as maximo
        FROM gold_price;
          '''

    return conn.query(sql)


def q102( conn ):

    sql = '''
         SELECT Regime, AVG(Close) as precio_promedio
         FROM (
         gold_price INNER JOIN recessions ON
         strftime('%Y-%m-%d', gold_price.Date) == strftime('%Y-%m-%d', recessions.Date)
         )
         GROUP BY Regime;
          '''

    return conn.query(sql)


def q103( conn ):

    sql = '''
         SELECT Regime, AVG(Close) as precio_promedio, STDEV(Close) as SD
         FROM (
         gold_price INNER JOIN recessions ON
         strftime('%Y-%m-%d', gold_price.Date) == strftime('%Y-%m-%d', recessions.Date)
         )
         GROUP BY Regime;
          '''

    return conn.query(sql)


def q104( conn ):

    sql = '''
          SELECT Regime, AVG(ABS(Low-High)) as Max_Diff_intramensual
            FROM (
            gold_price INNER JOIN recessions ON
            strftime('%Y-%m-%d', gold_price.Date) == strftime('%Y-%m-%d', recessions.Date)
            )
            GROUP BY Regime;
        '''

    return conn.query(sql)


def q105( conn ):

    sql = '''
          SELECT Date, Close
          FROM gold_price
          WHERE strftime('%Y', Date) >= "2019";
          '''

    return conn.query(sql)

def q106( conn ):

    sql = '''
          select strftime('%Y', Date) as Year, AVG(close) as Average_Close_Price
          FROM gold_price
          GROUP BY Year;
          '''

    return conn.query(sql)


def q107( conn ):

    sql = '''
          select strftime('%Y', Date) as Year, AVG(close) as Average_Close_Price
          FROM gold_price
          GROUP BY Year
          ORDER BY Year DESC LIMIT 20
          '''
    return conn.query(sql)


def q108( conn ):

    sql = '''
          select strftime('%Y', Date) as Year, AVG(close) as Average_Close_Price
          FROM gold_price
          GROUP BY Year
          HAVING Year >= "2008" OR Average_Close_Price > 21
          '''
    
    return conn.query(sql)


def q109( conn ):


    sql = '''
          SELECT Date,
            (Close - LAG(Close) OVER (ORDER BY Date)) * 100.0 / LAG(Close) OVER (ORDER BY Date) AS Cambio_porcentual_precio,
            (Volume - LAG(Volume) OVER (ORDER BY Date)) * 100.0 / LAG(Volume) OVER (ORDER BY Date) AS Cambio_porcentual_volumen
            FROM gold_price
          EXCEPT
          SELECT Date,
        (Close - LAG(Close) OVER (ORDER BY Date)) * 100.0 / LAG(Close) OVER (ORDER BY Date) AS Cambio_porcentual_precio,
        (Volume - LAG(Volume) OVER (ORDER BY Date)) * 100.0 / LAG(Volume) OVER (ORDER BY Date) AS Cambio_porcentual_volumen
        FROM gold_price
        WHERE Date == "1996-01-01" OR Date BETWEEN "1999-01-01" AND "2020-12-01";
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

    r04 = q104(conn)

    print("Tabla \"Pregunta 4\":")
    print(r04)
    print()

    r05 = q105(conn)

    print("Tabla \"Pregunta 5\":")
    print(r05)
    print()

    r06 = q106(conn)

    print("Tabla \"Pregunta 6\":")
    print(r06)
    print()

    r07 = q107(conn)

    print("Tabla \"Pregunta 7\":")
    print(r07)
    print()

    r08 = q108(conn)

    print("Tabla \"Pregunta 8\":")
    print(r08)
    print()

    r09 = q109(conn)

    print("Tabla \"Pregunta 9\":")
    print(r09)
    print()