import pandas as pd
import re
from sqlalchemy import create_engine

# this is our import statement where we state the path, and file name for where we are pulling our data
homework1 = pd.read_excel('C:/Users/Chase/Desktop/InfoProject/state-marriage-rates-90-95-99-17.xlsx',
                          skiprows=4,           # skip the first 4 rows metadata
                          header=[0,1],         # header now takes the fist and second rows
                          skipfooter=7,         # skips the last 7 lines of metadata
                          na_values='---',      # in the original file, all "empty" cells are filled with a
                                                # "---" so this will recognize those as null
                          usecols=51,           # identifies our original data set as 51 columns
                          index_col=[0, 1])     # these are our columns

# this will eliminate all rows within the file that are blank values
homework1.dropna(how='all', inplace=True)   # inplace=True so that these values are updated and not copied

# this will be our pivot statement for our columns to rows, also resetting our index to the 1st and 2nd col
homework1 = homework1.stack([0,1]).reset_index()

# here is we rename the titles of our columns
homework1.rename(columns={homework1.columns[0] : 'States',
                          homework1.columns[1] : 'Drop1', # i kept getting these extra columns that I did not want
                          homework1.columns[2] : 'Drop2', # so i gave them names to make it easier to drop them
                          homework1.columns[3] : 'Years',
                          homework1.columns[4] : 'Marriage Rates'},
                 inplace=True) # avoid copies

# here is where we will drop those extra columns that hold irrelevant data
homework1 = homework1.drop('Drop1', 1)  # the 1 tells python that these are column names not rows
homework1 = homework1.drop('Drop2', 1)

# this will round all float values to the nearest tenth so the data set is uniform throughout
homework1 = homework1.round(decimals=1)

# now our export statement to write the new format to a new excel file
homework1.to_excel(excel_writer='C:/Users/Chase/Desktop/InfoProject/state-marriage-rates-90-95-99-17Clean2.xlsx',
                   sheet_name='Sheet1',
                   na_rep='null',
                   index=False)
