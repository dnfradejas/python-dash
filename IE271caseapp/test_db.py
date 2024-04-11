import IE271caseapp.apps.dbconnect as db

def addfewgenres():
    sqlcode = """INSERT INTO genres (
        genre_name,
        genre_modified_date,
        genre_delete_ind
    ) 
    VALUES (%s, %s, %s)"""

    from datetime import datetime
    db.modifydatabase(sqlcode, ['Action', datetime.now(), False])
    db.modifydatabase(sqlcode, ['Horror', datetime.now(), False])

    # just some feedback that the code succeeded
    print("Genres added successfully.")

def selectgenres():
    sqlcode = """SELECT * FROM genres"""
    valus = []
    columns = ['genre_id', 'genre_name', 'genre_modified_date', 'genre_delete_ind']
    
    df = db.querydatafromdatabase(sqlcode, valus, columns)
    print(df)

# sql_resetgenres = """TRUNCATE TABLE genres RESTART IDENTITY CASCADE"""
# db.modifydatabase(sql_resetgenres, [])
# addfewgenres()
# df = selectgenres()
# print(df)

