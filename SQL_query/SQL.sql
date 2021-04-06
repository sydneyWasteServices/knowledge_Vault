SW-SRV1\ATSSQLEXPRESS

sql server cli => sqlcmd

 Alt+Shift+T = > move line down

crt + k  crt + c => commenting

crt + k crt crt + U


It becomes 
    dbo.TableYouCreated


bracket is delimiter

if there is space between 
    [product name]


USE tempdb 
    IF OBJECT_ID('dbo.Employees','U') IS NOT NULL
DROP TABLE dbo.Employees;


CREATE TABLE dbo.Employees
(
    empid INT NOT NULL,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    hiredate DATE NOT NULL,
    mgrid INT NULL,
    ssn VARCHAR(20) NOT NULL,
    salary MONEY NOT NULL
);


USE master;
Go
CREATE DATABASE test_db


--create table test_table (id varchar(10),salary varchar(10));

--insert INTO test_table values (3, 1000);
--insert INTO test_table values (4, 2000);

select * from test_table;




-- to compare table column within own table column

DECLARE @GENDER VARCHAR(10)
DECLARE @HIREDATE DATETIME

-- ? => parametrizartion of what to assign in Gender 
SET @GENDER = ?
SET @HIREDATE = ? 

SELECT a.BusinessEntityID, a.FirstName, a.LastNam, b.Job_Title
FROM Person.Person a
INNER JOIN HumanResource.Employee b ON a.BusinessEntityID = b.BusinessEntityID
WHERE b.Gender = @GENDER AND
    b.HireDate > @HIREDATE

