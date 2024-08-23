import pandas as pd
import sqlite3

# Load the CSV files into DataFrames
csv_for_date_df = pd.read_csv('CSVForDate.csv')  # Update with your actual file path
holidays_list_df = pd.read_csv('Holidays_List.csv')  # Update with your actual file path

# Convert date columns to datetime
csv_for_date_df['Date'] = pd.to_datetime(csv_for_date_df['Date'], format='%d-%b-%y')
holidays_list_df['Date'] = pd.to_datetime(holidays_list_df['Date'], format='%B %d, %Y')

# Connect to SQLite in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create tables and insert data
csv_for_date_df.to_sql('CSVForDate', conn, index=False, if_exists='replace')
holidays_list_df.to_sql('Holidays_List', conn, index=False, if_exists='replace')

# Processing logic for Expiry column
def determine_expiry(date_row):
    date = date_row['Date']
    date_str = date.strftime('%Y-%m-%d')  # Convert Timestamp to string
    weekday = date.weekday()  # 4 means Friday

    if weekday == 4:
        # Check if the Friday is a holiday
        cursor.execute('SELECT * FROM Holidays_List WHERE Date = ?', (date_str,))
        holiday = cursor.fetchone()
        
        if holiday:
            # Check the previous day if it's also a holiday or not
            previous_day = date - pd.Timedelta(days=1)
            previous_day_str = previous_day.strftime('%Y-%m-%d')  # Convert Timestamp to string
            cursor.execute('SELECT * FROM Holidays_List WHERE Date = ?', (previous_day_str,))
            previous_day_holiday = cursor.fetchone()
            if previous_day_holiday:
                return 'Yes'
            else:
                return 'Yes'
        else:
            return 'Yes'
    else:
        return 'No'

# Apply the logic to determine the Expiry column
csv_for_date_df['Expiry'] = csv_for_date_df.apply(determine_expiry, axis=1)

# Save the processed DataFrame to a new CSV file
csv_for_date_df.to_csv('CSVForDate_Sample_output.csv', index=False)

# Close the database connection
conn.close()
