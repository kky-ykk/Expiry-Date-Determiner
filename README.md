# Expiry Date Determiner

This project loads data from two CSV files, processes the data to determine expiry dates based on certain conditions, and outputs the result as a new CSV file.

## Project Overview

1. **Load Data:** 
   - Read two CSV files into DataFrames.
   - Convert the 'Date' columns to datetime format.

2. **Database Setup:** 
   - Create an in-memory SQLite database.
   - Populate the database with data from the DataFrames.

3. **Determine Expiry:** 
   - For each date in the main CSV:
     - Check if it's a Friday and if it’s also a holiday.
     - If it’s a holiday, check if the previous day is also a holiday.
     - Populate the "Expiry" column with 'Yes' for Fridays or adjusted dates, and 'No' otherwise.

4. **Output:** 
   - Save the modified DataFrame with the "Expiry" column as a new CSV file.
