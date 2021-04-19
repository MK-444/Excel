import openpyxl
excel_files = [r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData.xlsx', r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData2.xlsx']
values = []
if file in excel_files:
    woorkbook = openpyxl.load_workbook(file)
    worksheet = woorkbook['SalesOrders']
    cell_value = worksheet['G11'].value
    values.appent(cell_value)
    print(cell_value)