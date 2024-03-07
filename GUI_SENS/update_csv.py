import pandas as pd
import time
import random
from datetime import datetime
import os



# Define the update_data function
def update_data():

    # Check if the file exists
    file_path = 'C:/Users/dunca/OneDrive/Desktop/VS_Code_Beezy/example_plot.csv'
    file_exists = os.path.isfile(file_path)

    # If the file exists, delete it to reset all the data
    if file_exists:
        os.remove(file_path)

    # Create a new DataFrame with the required columns
    df = pd.DataFrame(columns=['Temp', 'Time', 'Humidity'])

    while True:
        # Get the current time
        now = datetime.now()

        # Format the time as a string
        current_time = now.strftime("%H:%M:%S")

        # Generate a random number between 1-3

        temp += random_number
        humid += random_number2

        # Package the data as a dictionary
        data = {'Temp': [temp], 'Time': [current_time], 'Humidity':[humid]}

        # Add the new data to the existing DataFrame
        new_df = pd.DataFrame(data)
        df = pd.concat([df, new_df], ignore_index=True)

        # Write the updated DataFrame to the CSV file
        df.to_csv(file_path, index=False)

        print(df)
        print("---------------")

        # Pause the script for 10 seconds
        time.sleep(10)


# Call the update_data function
update_data()