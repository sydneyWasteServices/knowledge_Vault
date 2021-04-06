import time
import xlwings as xw
import openpyxl


# if there is an array value assign to one cell 
# it becomes series of row value
# From A1 to C1 
list_of_values = [1, 2, 3]
ws.range('A1').value = list_of_values

# inspect active worksheet by name 
active_sheet_name = wb.sheets.active.name

# Offset example
lst = [1, 2 ,3] 
len(lst)
ws1.range((len(lst),1)).offset(column_offset=5).value = "have 5"

# build column array  - value goes down

lst = [1, 2 ,3]
new_lst = [[i] for i in lst]
ws1.range("A1").value = new_lst


# name a sheet
ws1.name = "lol"


# Delete which  position of sheet
# Delete third worksheet
wb = xw.Book()
wb.sheets[2].delete()


# Change sheets' value 
ws = wb.sheets['sheet1']
ws1 = wb.sheets[1]
ws.range('A1').value = list_of_values
ws1.range((2,1)).value = 'hello world'


# Save and close Workbook
wb.save('abc.xlsx')
wb.close()


# view data frame in a workbook
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
xw.view(df)

# api need to refer pywin32
# Set Font character style 
ws.range('A1').api.Font.Name = "Arial"


# Change a large range of cells Font style

ws = wb.sheets[0]
ws.range("A:AI").api.Font.Name = "Arial"


app = App(visible = False, add_book = False)
wb = app.books.open('Book1.xlsx')
sht = wb.sheets[0]
rng = sht.range('A1')
font_name = rng.api.Font.Name
font_color = rng.api.Font.ColorIndex
font_size = rng.api.Font.Size
print(font_name, font_color, font_size)


# Set Bold ==================================== 
import xlwings as xw
wb = xw.Book()
wb.sheets[0].range('A1').api.Font.Bold = True
# =====================================
wb = xw.Book()
sht = wb.sheets['Sheet1']
sht.range('A1').value = 'Foo 1'
sht.range('A1').api.font_object.font_style.set('bold')


# control column_width
ws.range('A1').column_width = 1.0 

# Orientation Row and Column
>>> wb = Workbook()
>>> Range('A1').value = [[1],[2],[3],[4],[5]]  # Column orientation (nested list)
>>> Range('A1:A5').value
[1.0, 2.0, 3.0, 4.0, 5.0]
>>> Range('A1').value = [1, 2, 3, 4, 5]
>>> Range('A1:E1').value
[1.0, 2.0, 3.0, 4.0, 5.0]


# Row  Height
# *************
import xlwings as xw
wb = xw.Book(...)
wb.sheets[0]['1:1'].api.RowHeight = 100
# *************




>>> xw.Range('A1').color = (255,255,255)

# goes to end
# >>> import xlwings as xw
# >>> wb = xw.Book()
# >>> xw.Range('A1:B2').value = 1
# >>> xw.Range('A1').end('down')
# <Range [Book1]Sheet1!$A$2>
# >>> xw.Range('B2').end('right')
# <Range [Book1]Sheet1!$B$2>