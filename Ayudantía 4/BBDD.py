
import functools, sqlite3, math, pandas as pd

def none_guard(func):
    # Source: django
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return None if None in args else func(*args, **kwargs)
    return wrapper

class STDEV:
    # Source: https://stackoverflow.com/questions/2298339/standard-deviation-for-sqlite
    def __init__(self):
        self.M = 0.0
        self.S = 0.0
        self.k = 1

    def step(self, value):
        if value is None:
            return
        tM = self.M
        self.M += (value - tM) / self.k
        self.S += (value - tM) * (value - self.M)
        self.k += 1

    def finalize(self):
        if self.k < 3:
            return None
        return math.sqrt(self.S / (self.k-2))


class sql_interaction( ):
    
    def __init__( self, path ):
        connection = None
        try:
            connection = sqlite3.connect(path)
            connection.text_factory = str
            connection.create_function('sqrt' ,  1, math.sqrt)
            connection.create_function('power',  2, none_guard(math.pow))
            connection.create_aggregate("stdev", 1, STDEV)
        
        except sqlite3.Error as e:
            print(f'El proceso a terminado con el siguiente error "{str(e)}"')
        
        self.connection = connection
    
    def execute(self, query):
        cursor = self.connection.cursor()
        try:
            if query == "": return "Query vacía"
            else:
                cursor.execute(query)
                self.connection.commit()
                return "Query ejecutada exitosamente"
        except sqlite3.Error as e: return f"Error: {str(e)}"

    def script(self, query):
        cursor = self.connection.cursor()
        try:
            if query == "": return "Query vacía"
            else:
                cursor.executescript(query)
                self.connection.commit()
                return "Query ejecutada exitosamente"
        except sqlite3.Error as e: return f"Error: {str(e)}"  
        
        
        
    def query( self, query ):
        temp =  self.connection.execute(query)
        cols =  [i[0] for i in temp.description]
        return pd.DataFrame( temp.fetchall() , columns = cols )
        
        
        