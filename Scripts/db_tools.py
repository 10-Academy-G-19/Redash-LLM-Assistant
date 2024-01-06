import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def run_query (connection_details: dict, query: str) -> None:
    """
    Run a SQL query and return the results as a pandas DataFrame.
    """
    try:

        conn = psycopg2.connect(**connection_details)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cursor.close()
        conn.close()
        return 1
    
def fill_db(connection_details: dict, df: pd.DataFrame, table_name: str) -> None:
    """
    Fill the database with the given data.
    """
    try:
        db_url = f"postgresql://{connection_details['user']}:{connection_details['password']}@{connection_details['host']}:{connection_details['port']}/{connection_details['dbname']}"
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 1
    
    finally:
        if engine:
            engine.dispose()

    return None


def create_table_query(df: pd.DataFrame, table_name: str) -> str:
    """
    Create a SQL query to create a table in the database.
    """
    # columns = list(df.columns)
    # columns = [f"{column} VARCHAR(255)" for column in columns]
    # columns = ", ".join(columns)
    # query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
    # return query

    dtype_mapping = {
        'object': 'TEXT',
        'int64': 'INTEGER',
        'float64': 'REAL',
        'datetime64': 'TIMESTAMP'
    }

    # Generate column definitions for the CREATE TABLE query
    column_definitions = ', '.join([f'"{column}" {dtype_mapping.get(str(df[column].dtype), "TEXT")}' for column in df.columns])

    primary_key_cols = ['"' + df.columns[0] + '"']

    if table_name in [
        'viewership_by_date_table_data',
        'totals_table_data'
    ]:
        primary_key_cols = ['"' + df.columns[0] + '"']

    elif df.columns[0] == "Date":
        primary_key_cols.append('"' + df.columns[1] + '"')

    primary_key_constraint = f'PRIMARY KEY ({", ".join(primary_key_cols)})'

    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({column_definitions}, {primary_key_constraint});'

    return query

