
from BBDD import sql_interaction


def info_db(conn):
    sql = 'select sql from sqlite_schema'
    return conn.query(sql)


def info_table(conn, table='grades'):
    sql = f"pragma table_info('{table}');"
    return conn.query(sql)


def query_gold_table(conn, table='gold_price'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_sp500_table(conn, table='sp500'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_nasdaq_table(conn, table='nasdaq'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_macrodata_table(conn, table='us_macrodata'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_recessions_table(conn, table='recessions'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_sp_dividend_yield_table(conn, table='sp_dividend_yield'):
    sql = f'select * from {table}'
    return conn.query(sql)


def query_sp_PE_ratio_table(conn, table='sp_PE_ratio'):
    sql = f'select * from {table}'
    return conn.query(sql)


if __name__ == '__main__':

    # Nos conectamos a la base de datos
    conn = sql_interaction("us_macroeconomic_data.sqlite")

    ej1 = info_db(conn)

    print("Output consulta \"Schema\":")
    print(ej1)
    print()

    print("\nType del output:")
    print(type(ej1))
    print()

    print("\nIterando rows:")
    for index, row in ej1.iterrows():
        print(f"Row {index}:\n{row['sql']}\n")
    print()
    
    tables = ['gold_price', 'sp500', 'nasdaq', 'us_macrodata', 'recessions', 'sp_dividend_yield', 'sp_PE_ratio']
    
    for table in tables:
        ej2 = info_table(conn, table)
        print(f"Output consulta \"Tipos de datos {table}\":")
        print(ej2)
        print()

    query_gold = query_gold_table(conn, 'gold_price')

    print("Tabla \"Gold Price\":")
    print(query_gold)
    print()

    query_sp500 = query_sp500_table(conn, 'sp500')

    print("Tabla \"SP500\":")
    print(query_sp500)
    print()

    query_nasdaq = query_nasdaq_table(conn, 'nasdaq')

    print("Tabla \"Nasdaq\":")
    print(query_nasdaq)
    print()

    query_macrodata = query_macrodata_table(conn, 'us_macrodata')

    print("Tabla \"US Macroeconomic Data\":")
    print(query_macrodata)
    print()

    query_recessions = query_recessions_table(conn, 'recessions')
    print("Tabla \"Recessions\":")
    print(query_recessions)
    print()

    query_sp_dividend_yield = query_sp_dividend_yield_table(conn, 'sp_dividend_yield')

    print("Tabla \"S&P Dividend Yield\":")
    print(query_sp_dividend_yield)
    print()

    query_sp_PE_ratio = query_sp_PE_ratio_table(conn, 'sp_PE_ratio')

    print("Tabla \"S&P PE Ratio\":")
    print(query_sp_PE_ratio)
    print()
