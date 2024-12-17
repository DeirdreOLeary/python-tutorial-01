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


## CLEANSING DATA ##

# Get the course data from the test.datacamp_courses2 table
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM test.datacamp_courses2;"))
    df_course = pd.DataFrame(rs.fetchall())
    df_course.columns = rs.keys()

# Check for duplicates
dupes_course = df_course.duplicated()
print(dupes_course)

# Remove '!' from course_name
df_course['course_name'] = df_course['course_name'].str.strip('!')

# Replace 'SQLL' with 'SQL' in topic
df_course['topic'] = df_course['topic'].str.replace('LL', 'L')

# Convert topic to a category
df_course['topic'] = df_course['topic'].astype('category')

# Set all topics to upper case
df_course['topic'] = df_course['topic'].str.upper()

# Checks for nulls in books_sold
df_course['books_sold'].isna()
df_course = df_course.fillna({'books_sold': 100})

# Drop out-of-range values (i.e. any below 20)
df_course = df_course[df_course['books_sold'] >= 20]

# Get info about the course dataframe
df_course.head(10)
df_course.dtypes
df_course.info()
df_course['topic'].describe()
