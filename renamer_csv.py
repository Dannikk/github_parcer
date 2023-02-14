import os
import shutil
 
directory = 'data_analysis_csv\output'
 
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            print(f"{root}\{file}")
            new_name = root.split('\\')[-1]
            print(f"pretty_csv\{new_name}.csv")
            shutil.copy(f"{root}\{file}", f"pretty_csv\{new_name}.csv")