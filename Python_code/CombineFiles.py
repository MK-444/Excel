# pip3 install pandas
import pandas as pd
# spycify the files location (or path)
excel_files = [r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData.xlsx', r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData2.xlsx']
# create blank dataframe 
merge = pd.DataFrame()
# loop through every file in the list
for file in excel_files:
# read files into a  DataFrame and skip to the  first row (header)
  df = pd.read_excel( file, skiprows = 1)
  # open result to merge
  merge = merge.append( df, ignore_index = True)
  # create final workbook with merged results
  merge.to_excel('Merged_Files.xlsx')

