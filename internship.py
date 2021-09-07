import cx_Oracle
conn=cx_Oracle.connect('system/raj@//localhost:1521/xe')
print(conn.version)

try:
    cur=conn.cursor()
    sql_create="""create table Movieej(Movie_name varchar(50),lead_actor varchar(40),lead_actress varchar(30),r_date DATE,director varchar(40))"""
    cur.execute(sql_create)
except Exception as err:
    print('Error while creating the table',err)
else:
    print('table created')
    try:
        cur=conn.cursor()
        sql_insert="""insert into Movieez values(:1,:2,:3,:4)"""
        data=[('dangal','Aamir khan','fatima','23-DEC-2016','nitesh tiwari'),('ms_dhoni','sushant singh','kiara advani','30-SEP-2016','neeraj pandey'),('kedarnath','sushant singh','sara ali khan','07-DEC-2018','abhishek kapoor'),('dil bechara','sushant singh','sangana sanghi','24-JULY-2020','mukesh chabra')]
        cur.execute(sql_insert,data)
    except Exception as err:
        print('Error while inserting the data',err)
    else:
        print('insert completed')
        conn.commit()
        try:
            cur=conn.cursor()
            sql="""select*from Movieez"""
            cur.execute(sql)
            row=cur.fetchall()
            print(row)
        except Exception as err:
            print('Exception occured while fetching the record',err)
        else:
            print('completed')
            try:
                cur=conn.cursor()
                sql1="""(select movie_name from Movieez where lead_actor='sushant singh')"""
                cur.execute(sql1)
                row1=cur.fetchone()
                print(row1)
            except Exception as err:
                print('Exception occured while fetching the single record',err)
            else:
                print(' fetch completed')
finally:
    cur.close()
    conn.close()

