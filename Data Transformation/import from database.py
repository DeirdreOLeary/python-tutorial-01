## PARSE PASSWORD WITH SPECIAL CHARACTERS ##

from sqlalchemy import create_engine, text
import pandas as pd
import urllib.parse as ulp

ulp.quote_plus("<password>")

## BASIC IMPORT FROM DATABASE ##

# Connect to the scratch database on the local postgres instance using pg8000 driver
engine = create_engine(
    "postgresql+pg8000://postgres:<password>@localhost/scratch")

# Get the schema & names of the user tables in the database
with engine.connect() as con:
    tables = con.execute(text(
        "SELECT schemaname, tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema');"))
    for table in tables:
        print(table)

# Get the employee data from the public.windowing1 table
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM public.windowing1;"))
    df_emp = pd.DataFrame(rs.fetchall())
    df_emp.columns = rs.keys()

# Query the first rows of employee data & get some high level information
df_emp.head()

df_emp.describe()


## IMPORT USING PANDAS ##

# Alternative to con.connect & execute, import using pandas
df_emp2 = pd.read_sql_query("SELECT * FROM public.windowing1;", engine)

df_emp2.head()
