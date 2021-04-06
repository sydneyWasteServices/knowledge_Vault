
CDC => Change Data Capture

ODBC vs OLE DB
ODBC is constrained to relational data stores; 

OLE DB supports all forms of data stores (relational, hierarchical, etc) In general, OLE DB provides a richer and more flexible interface for data access because it is not tightly bound to a command syntax (like SQL in the case of ODBC).


## Project Scope is very Important 
## It affects the visbility of Variables


### Load csv from ssis

If there is none of them in SSIS Toolbox, open SSIS Toolbox

Data Control flow 
1. Flat file source


2. OLE DB destination 

    connection configure

    Data access mode:

        Table or view - fast load
        


[Flat File Source [2]] Error: Data conversion failed. The data conversion for column "Customer Name" returned status value 4 and status text "Text was truncated or one or more characters had no match in the target code page.".

[Flat File Source [2]] Error: The "Flat File Source.Outputs[Flat File Source Output].Columns[Customer Name]" failed because truncation occurred, and the truncation row disposition on "Flat File Source.Outputs[Flat File Source Output].Columns[Customer Name]" specifies failure on truncation. A truncation error occurred on the specified object of the specified component.


Data Soruce -> Advanced -> Look at the column that goes in error -> change OutputColumnWidth to 200 and try again.


Loop container

    Set up Variable 
    Scope => Foreach Loop 
    
    Foreach Loop editor
        Collection
            Foreach FileEnumerator
    
    Variable Mappings 
        Variable Index
        YourVar    0

    In OLE DB connection Editor:
        Data access mode:
            Table or View :
                If you haven't yet created the Table, 
                can use Table or View to create table


Connect Manager To Use the Variable
    To use Connect Manager, you must create Connection under the Project 
    
    Solution Explore
        <ProjectName> Project
            Connection Manager
                FlatFile Connection Manager
     