#Danielle Santucci 
#Informatics Project
#HWA 1 Assignment 1.2

import pandas as pd

from sqlalchemy import create_engine


divorceRates=pd.read_excel('state-divorce-rates-90-95-99-17.xlsx', #Reads assignment
                           skiprows=5, #skip the first 5 rows
                           
                           index_col=0, #Columns 
                           skipfooter=0, #skip ending metadata
                           
                           na_values='---' #values that display --- are null values
                          
)


divorceRates.dropna(how='all', inplace=True)   
 #drop rows that have null values but modifies original object rather than returning a copy
divorceRates=divorceRates.stack(dropna=False) #stacks labels and put index into cols and adds dropna false to return empty values as null


divorceRates.index.names=['State', 'Year'] #Displays index names state and year and places data
divorceRates.name="Divorce Rates" #Displays column 2 as divorce rates



divorceRates.to_excel(excel_writer='divorceRates_clean.xlsx', #Makes new excel file called divorce rates clean
                      sheet_name='divorceRates', #names the sheet name divorceRates
                      na_rep='null',
                                      #n/a data is declared as null
                      )                          

#Extra Credit database
#Create database connection
sqlite=create_engine('sqlite:///divorceRates.db') #creates new sqlite database in folder
divorceRates.to_sql('divorceRates', #export database to divorceRates table
                    sqlite,
                    if_exists='replace', #If it already exists than replace
                    index=False) #do not include pandas index
sqlite.dispose() #Close all connections associated with each engine