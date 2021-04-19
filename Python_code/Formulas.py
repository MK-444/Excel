import openpyxl

excel_files = [r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData.xlsx', r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData2.xlsx']

for file in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb['SalesOrders']
    worksheet['G46']'=AVERAGE(G3:G45)'
wb.save(file)