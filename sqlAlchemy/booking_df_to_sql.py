from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Float, Date, Time, SmallInteger, DateTime, Text
import sqlalchemy
import pandas as pd
import pyodbc
import pymssql
import csv
from io import StringIO
# meta = MetaData()


engine = create_engine(
    'mssql+pymssql://SW-SRV1\\ATSSQLEXPRESS/OLTP_SOURCE_COPY_TEST')

df = pd.read_csv("../../../dataVault/booking/27.01.2021_02.02.2021.csv",
                 dtype={"Schd Time Start": object, "PO": str})

# df = df.fillna(0)


df.to_sql(name="staging_table_test", con=engine, if_exists="replace", dtype={
    'Job No': Float(precision=5),
    'Date': String(length=350),
    'Schd Time Start': String(length=350),
    'Schd Time End': String(length=350),
    'Latitude': Float(precision=7, asdecimal=True),
    'Longitude': Float(precision=7, asdecimal=True),
    'Customer number': Float(precision=4),
    'Customer Name': String(length=800),
    'Site Name': String(length=800),
    'Address 1': String(length=1200),
    'Address 2': String(length=1200),
    'City': String(length=500),
    'State': String(length=30),
    'PostCode': Integer(),
    'Zone': String(length=500),
    'Phone': String(length=600),
    'Qty Scheduled': SmallInteger(),
    'Qty Serviced': SmallInteger(),
    'Serv Type': String(length=600),
    'Container Type': String(length=20),
    'Bin Volume': Float(precision=5),
    'Status': String(length=5),
    'Truck number': String(length=50),
    'Route number': String(length=50),
    'Generate ID': String(length=500),
    'Initial Entry Date': String(length=350),
    'Weight': Float(precision=5),
    'Prorated Weight': Float(precision=5),
    'Booking Reference 1': String(length=200),
    'Booking Reference 2': String(length=200),
    'Alternate Ref No 1': String(length=200),
    'Alternate Ref No 2': String(length=200),
    'Alternate Service Ref 1': String(length=200),
    'Alternate Service Ref 2': String(length=200),
    'Notes': Text(length=8000),
    'Directions': Text(length=8000),
    'CheckLists': String(length=300),
    'Waste Type': String(length=350),
    'Tip Site': String(length=450),
    'Price': Integer(),
    'PO': String(length=200)
})




# except:

    # except ValueError:
    #     print(ValueError)
    # except sqlalchemy.exc.OperationalError:
    #     print(sqlalchemy.exc.OperationalError)

    #  pymssql.OperationalError as e:
    #     print("Mssql error "+e)

    # sqlalchemy.exc.OperationalError: (pymssql.OperationalError)
    # (242, b'The conversion of a nvarchar data type to a datetime data type
    # resulted in an out-of-range value.DB-Lib error message 20018,
    # severity 16:\nGeneral SQL Server error: C heck messages from the SQL Server\n')



# Float(asdecimal=True)
# precision=3
#
# It means they definitly have 00.000  has three decimal point even it is zero

# try:


# def psql_insert_copy(table, conn, keys, data_iter):
#     """
#     Execute SQL statement inserting data

#     Parameters
#     ----------
#     table : pandas.io.sql.SQLTable
#     conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
#     keys : list of str
#         Column names
#     data_iter : Iterable that iterates the values to be inserted
#     """
#     # gets a DBAPI connection that can provide a cursor
#     dbapi_conn = conn.connection
#     with dbapi_conn.cursor() as cur:
#         s_buf = StringIO()
#         writer = csv.writer(s_buf)
#         writer.writerows(data_iter)
#         s_buf.seek(0)
#         print(data_iter)

#         columns = ', '.join('"{}"'.format(k) for k in keys)
#         if table.schema:
#             table_name = '{}.{}'.format(table.schema, table.name)
#         else:
#             table_name = table.name

#         sql = 'INSERT INTO {} ({}) FROM STDIN WITH CSV'.format(
#             table_name, columns)
#         cur.copy_expert(sql=sql, file=s_buf)

# def sql_callable_test(a,b,c,d):
#     print(f"{a}, {b}, {c}, {d}")