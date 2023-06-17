# connecting to the Oracle database
# import cx_Oracle
# #dsn_tns=cx_Oracle.connect('hr/hr@localhost')
# conn=cx_Oracle.connect('hr/hr@localhost')
# c=conn.cursor()
# c.execute('select * from employees where salary between 10000 and 25000 order by salary desc')
# for row in c:
#     print (row[0],'-',row[1]+' '+row[2],'-',row[7])
#
# conn.close()

# connecting to the SQL Server database
# import pyodbc
import pyodbc
cnxn = pyodbc.connect(r'Driver=SQL Server;Server=HP-PC\SQLEXPRESS;Database=AdventureWorks2012;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute('select * from dbo.department')
#
for row in cursor:
   # print ('row=%r'%(row,))
    print(row[0], ' - ', row[1] + ' - ' + row[2], ' - ', row[3])

# connecting to the Mongodb
