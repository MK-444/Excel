import pandas as pd
import numpy as np
files = [[r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData.xlsx', r'C:\Users\Svitlana\3D Objects\Excel_Automation-master\datasets\SampleData2.xlsx']
for file in files:
    df = pd.read_excel(file)
    pencil = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    print(file)
    print(pencil)