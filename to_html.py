import pandas as pd  

a = pd.read_csv("Resources/city_data.csv") 
# to save as html file 
# named as "Table" 
a.to_html("Table.htm") 
# assign it to a  
# variable (string) 
html_file = a.to_html()