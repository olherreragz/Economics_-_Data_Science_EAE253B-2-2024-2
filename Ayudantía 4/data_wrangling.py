import sqlite3
import pandas as pd

# Función para cargar CSVs a bbdds SQLite
def load_csv_to_sqlite(db_name, csv_files, table_names):

    conn = sqlite3.connect(db_name)
    
    cursor = conn.cursor()

    # Crear tablas en SQL
    cursor.executescript('''
    -- Dropear todas las tablas si existen
    PRAGMA writable_schema = 1;
    DELETE FROM sqlite_master WHERE type IN ('table', 'index', 'trigger');
    PRAGMA writable_schema = 0;
    VACUUM;
    PRAGMA INTEGRITY_CHECK;

    -- Crear tablas (vacías)
    CREATE TABLE IF NOT EXISTS gold_price (
        Date TEXT,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Adj_Close REAL,
        Volume INTEGER
    );

    CREATE TABLE IF NOT EXISTS sp500 (
        Date TEXT,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Adj_Close REAL,
        Volume INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS nasdaq (
        Date TEXT,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Adj_Close REAL,
        Volume INTEGER
    );

    CREATE TABLE IF NOT EXISTS us_macrodata (
        Date TEXT,
        RPI REAL,
        INDPRO REAL,
        CE16OV REAL,
        UNRATE REAL,
        PAYEMS REAL,
        USGOOD REAL,
        USTPU REAL,
        HOUST REAL,
        PERMIT REAL,
        DPCERA3M086SBEA REAL,
        AMTMTI REAL,
        AMTMNO REAL,
        ACOGNO REAL,
        AMDMUO REAL,
        BUSINV REAL,
        ISRATIO REAL,
        M1SL REAL,
        M2SL REAL,
        TOTRESNS REAL,
        BUSLOANS REAL,
        REALLN REAL,
        DTCTHFNM REAL,
        FEDFUNDS REAL,
        TB3MS REAL,
        TB6MS REAL,
        GS1 REAL,
        GS5 REAL,
        GS10 REAL,
        AAA REAL,
        TB3SMFFM REAL,
        T1YFFM REAL,
        AAAFFM REAL,
        EXSZUS REAL,
        EXCAUS REAL,
        EXUSUK REAL,
        WPSFD49207 REAL,
        WPSID61 REAL,
        CPIAUCSL REAL,
        SP500 REAL,
        NASDAQ REAL,
        GOLDBAR REAL,
        Regime TEXT,
        PE REAL,
        Dividend_Yield REAL
    );

    CREATE TABLE IF NOT EXISTS recessions (
        Date TEXT,
        Regime TEXT
    );

    CREATE TABLE IF NOT EXISTS sp_dividend_yield (
        DateTime TEXT,
        Dividend_Yield REAL
    );

    CREATE TABLE IF NOT EXISTS sp_PE_ratio (
        date TEXT,
        value REAL
    );
    ''')

    conn.commit()  # Commit cambios a la bbdd

    # Loop para los CSVs
    # Aquí se cargan los datos a cada tabla creada

    for csv_file, table_name in zip(csv_files, table_names):
        # Read CSV (pandas DataFrame)
        df = pd.read_csv(csv_file)
        
        # Convertir 'Date' o 'DateTime' (strings) a fechas
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
        if 'DateTime' in df.columns:
            df['DateTime'] = pd.to_datetime(df['DateTime']).dt.strftime('%Y-%m-%d %H:%M:%S')

        # Escribir los DataFrames en la bbdd SQLite
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Tabla '{table_name}' creada exitosamente como '{db_name}'.")

    # Cerrar conexión a la bbdd
    conn.close()

# CSV paths
csv_files = [
    'data/GOLD.csv',
    'data/GSPC (1).csv',
    'data/IXIC.csv',
    'data/macrodata.csv',
    'data/Recession_Periods.csv',
    'data/snpdiv.csv',
    'data/sp-500-pe-ratio-price-to-earnings-chart.csv'
]

table_names = [
    'gold_price', 
    'sp500', 
    'nasdaq', 
    'us_macrodata', 
    'recessions',
    'sp_dividend_yield',
    'sp_PE_ratio'
]

# Nombre de la nueva bbdds SQLite
db_name = 'us_macroeconomic_data.sqlite'

# Ejecutar la creación
load_csv_to_sqlite(db_name, csv_files, table_names)
