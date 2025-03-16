import camelot
import pandas as pd

# Extract tables from PDF
tables = camelot.read_pdf('Results_CRE.pdf', pages='1-end')

# List to store dataframes
dfs = []

# Iterate through tables and append dataframes to the list
for table in tables:
    dfs.append(table.df)

# Concatenate all dataframes in the list
if dfs:
  combined_df = pd.concat(dfs, ignore_index=True)

  # Save the combined dataframe to a CSV file
  combined_df.to_csv('Results_CRE_2025.csv', index=False)
  print("Combined table saved to Results_CRE_2025.csv")
else:
    print("No tables found in the PDF.")