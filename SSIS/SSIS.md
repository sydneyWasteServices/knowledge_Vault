

Set up @Gender = ? 
? as a parameter in SSIS 


Execute SQL Task
Parameter Mapping => Parameter Size -1 => means resolve itself


Parameter Name  => corresponding as an array of ?  [?,?]
First position is 0
Second => 1 
and then so on 


Result Set as
Result Name => 
    0

Variable Name => 
    User::ResultSetEmployees

Since you can return more than one table 

result Name could 0 to whatever you returning

In variable, you should also create a var for ResultSet to return to.

In variable :           Data type :
ResultSetEmployee       Object          


Use start to debug => check is that having green tick



ForEach Loop container
    Foreach ADO Enumerator  => This is fitted for Table Object


ForEach Loop  Editor
    Variable Mapping :
     <!--predix as column  -->
        Name : Column_

