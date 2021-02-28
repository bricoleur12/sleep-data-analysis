import pandas as pd
import sqlalchemy

print("In Read User Data and add it to the database sleepdata")

# Read the data from the file uploaded by the user to a pandas dataframe
dataset_file_location = "./dataset/user_data.xlsx"

if ( dataset_file_location.find(".xlsx") > -1 ):
    df = pd.read_excel(dataset_file_location)
elif ( dataset_file_location.find(".csv") > -1):
    df = pd.read_csv(dataset_file_location)


# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgresql://postgres:admin@localhost/example")
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())

table_name = 'sleep_data'
df.to_sql(table_name, con, if_exists='replace')

print("The tables list is:")
print(engine.table_names())

con.close()