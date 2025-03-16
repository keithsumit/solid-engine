import camelot
import pandas as pd

# Extract tables from PDF
tables = camelot.read_pdf('pdffilename.pdf', pages='1-end')

# List to store dataframes
dfs = []

# Iterate through tables and append dataframes to the list
for table in tables:
    dfs.append(table.df)

# Concatenate all dataframes in the list
if dfs:
  combined_df = pd.concat(dfs, ignore_index=True)

  # Save the combined dataframe to a CSV file
  combined_df.to_csv('csvfilename.csv', index=False)
  print("Combined table saved to csvfilename.csv")
else:
    print("No tables found in the PDF.")
