import psycopg2
import pandas as pd

def getdblocation():
    # define connection string
    db = psycopg2.connect(
        host="localhost",
        database="156casedb",
        user='postgres',
        port='5432',
        password='Tsuna123!'
    )

    return db

# print(getdblocation())
def modifydatabase(sql, values):
    db = getdblocation()

    # we create a cursor object
    cursor = db.cursor()

    # we execute the query
    cursor.execute(sql, values)

    # we commit the changes
    db.commit()

    # we close the cursor
    cursor.close()

def querydatafromdatabase(sql, values, dfcolumns):
    db = getdblocation()

    # we create a cursor object
    cursor = db.cursor()

    # we execute the query
    cursor.execute(sql, values)

    # we fetch all the results

    # we create a dataframe
    df = pd.DataFrame(cursor.fetchall(), columns=dfcolumns)
    
    # we close the cursor
    cursor.close()

    return df
    