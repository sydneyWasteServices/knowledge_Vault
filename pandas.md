# SW-SRV1\ATSSQLEXPRESS
# df  = pd.read_csv()

# server = "SW-SRV1\ATSSQLEXPRESS"
# db = ""
# username = "SW-SRV1\gordon"
# password = ""

# driver = "DRIVER={ODBC Driver 11 for SQL Server};"
# server = "SERVER=SW-SRV1\ATSSQLEXPRESS"
# db = "DATABASE=master;"
# win_auth = "Trusted_connection=yes"

# conn_string = f'{driver}{server}{db}{win_auth}'
# print(conn_string)

Create table in a database
<!-- CREATE TABLE [database_name.][schema_name.]table_name (
    pk_column data_type PRIMARY KEY,
    column_1 data_type NOT NULL,
    column_2 data_type,
    ...,
    table_constraints
); -->


.read_csv()

.infor() =>display all data type of dataframe and some other infor

.dtypes => display column type

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])


df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', header=None)
df
 




sql_conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};
                            SERVER=SW-SRV1\ATSSQLEXPRESS;
                            DATABASE=master;
                            Trusted_Connection=yes')

query = "SELECT [BusinessEntityID],[FirstName],[LastName],
                 [PostalCode],[City] FROM [Sales].[vSalesPerson]"


df = pd.read_sql(query, sql_conn)


## ODBC conn with pandas
https://tomaztsql.wordpress.com/2018/07/15/using-python-pandas-dataframe-to-read-and-insert-data-to-microsoft-sql-server/


## juptyer note book shortcut
http://maxmelnick.com/2016/04/19/python-beginner-tips-and-tricks.html

Booking 
CREATE TABLE Finance.test_db_1(
id int IDENTITY(1,1),
date date,
Customer_Name varchar(10000),
Address varchar(10000),
City varchar(5000),	
State varchar(100),
PostCode int,
Qty_Scheduled int, 	

Qty_Serviced int,	
Serv_Type varchar(100)
Bin_Volume dec(10,15)
Status varchar(10)
Truck_number varchar(500)
Route_number varchar(500)
Waste_Type varchar(500)
Price dec(100,40)
)

'Date', 'Customer Name', 'Address 1', 'City', 'State', 'PostCode',

       , 'Qty Serviced', 'Serv Type', 'Bin Volume',
       'Status', 'Truck number', 'Route number', 'Waste Type', 'Price'

        row['Qty Scheduled']
        row 



        # 

# cursor = sql_conn.cursor()

# top_three_rows


# for index,row in top_three_rows.iterrows():
#     cursor.execute("INSERT INTO dbo.vSalesPerson_test([BusinessEntityID],
#                         [FirstName],[LastName]) 
#                          values (?, ?,?)", row['BusinessEntityID'], 
#                                            row['FirstName'], 
#                                            row['LastName']) 
# .. connStr.commit()
# cursor.close()
# connStr.close()



# query = 
# DTABASE=Adventureworks;
# CREATE TABLE test_dbc

# query = "SELECT [BusinessEntityID],[FirstName],[LastName],
#                  [PostalCode],[City] FROM [Sales].[vSalesPerson]"
# df = pd.read_sql(query, sql_conn)
# df.head(3)