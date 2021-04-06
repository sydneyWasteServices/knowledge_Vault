Power Query 
    Left Side bar 
        has => new Group => If you have many tables

    Right Property
        Name of the Table Model, should give it a good name

Clean data
    Top bars 
        =>  Remove Top row 
        => Use First Row as Header
    Filter Out the subtotal in the column 
        => Click on the column
            Filter Rows => does not contain

Insert Step
    Click on right bar steps list 
        => click top bar => Add Column
        => Custom Column


From Column move to Rows
    E.g. 
            Jan 16      Feb 16 ......
product1    figure    figure2
product2

move to
            Product1    product2
Jan 16
Feb 16

    1. High all column that you wanna transform from columns to Rows

    transform
        => unprivot columns 

Formula Bar
    Top Bar => View 
        => Query Settings
            Formula Bar 


Main Power Bi Desktop 

    Top bar 
        => Refresh => will pull data and follow the step


****Build models not report 
    ````````
        Look up table the top 

        Data Table at Bottom 
    ``````

Look up table - dimension

    Who What Where When How 

    E.g. Sales
            Who bought it 
            What did they buy
            Where did I buy territory             
            When did 

    E.g.

    Look up table is about few hundred Rows
        e.g.
            hundreds of Customer
            hundreds of Product
    Not millions of them


    Customer                    Product                 Territories             Calendar        
        addressLine                 Category                Country                 Date
        Brithday                    Color                   Group                   DateKey
        CommuteDistance             DaysToManufacture       Region                  Fiscal_Month
        CustomerKey                 ListPrice               RegionImage             Fiscal_Month_num
        DateFirstPurchase                                                           F_Quarter
        Education                                                                   F_year

            Sales                       Budget
        CustomerKey
        OrderDate
        OrderQuantity
        ProductKey
        PromotionKey
        
    Need to Create Dimension table 

    Customer        Where     Run / Route     Bins    Rev type               
        Infor        Lat
                     Long 

```
Power Bi Modelling best practice
```

Lookup table 
    => drag and drop the relationship
        From lookup to data table or vice versa


### Key to Key 

    Lookup table 
        Customer table
            => Customer key to Sales table Key 


    Customer table => Sales table 
        one to many 

        one customer in Customer table
        Many customer occur in Sales table 


#### relationship 
    => should typically 
        Custemer(lookup table) =>  Sales(Data Table )


Visualisation
    Card => with one field
        and then table 

        Format => left of the 

Report 
    Left hand side 
        => Card or Table 
            => put field 
                => size 
        Top bar can format to $

    Relationship
        => slice to Year 

            left drop down box
                don't sum 

    Filter 
        => filter display data only for 
            one year

            Filter on this page 
                1. data field
                2. All pages
            
            Basic Filter 

    Modelling
        => sort by column 
            => after has relationship



    You can only slice and dice by 
        linked tables

DAX data analytics expression DAX

    Never drag and drop Measure => implicit measure

Explicit measure 
    Click Top bar 
        new Measure 

            Sales = Sum(SalesAmount)


Reasons 
    Control
    Reuse
    Connected reports


Left side bar 
    Table 
        New column 
            => you will have formula 

            New column
            Total Sales Amount = Sales[SalesAmount] + Sales[TaxAmt]

Measure vs Calculate Column 

    New measure Calculate the entire table without reference a specific Column

    While New column Calculate row one by one 


    Row Context => Calculate rows one by one 
        When reference the row directly 

New measure 
    Wrap it an aggregated function

    Total Sales = Sum(Sales[SalesAmount]) + Sum(Sales[TaxAmt])

Measures => smaller size 

Calculated column => bigger size

###Good Practice => use Measure For Math

    => Create a new column (New measure) for the aggregation 
    
    Total Sales Column =>  Use Total Sales Column result as your Report 


Define a new measure, Rather than Drag and drop

    Variance = [Sales] - [Budget]

    Variance% = [Vaiance] / [Budget]

Use DIVIDE => handle divided by Zero
                                            third Parameter , what to return on Zero Result 
    Variance% = DIVIDE([Variance], [Budget]) 


Text   Insert 


    Bar chart can drill down 
        For sub categories 

    Data Colour => ...  => Conditional Formatting => Color Scale

                    Base on Field => Color lowest Value and Highest Value

                    Dril Down


    Left Side bar
        Filter TopN
        Additional Filter 
        Product Name
        Base on what Value 

        



    