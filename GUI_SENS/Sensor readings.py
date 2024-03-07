import pandas as pd
import time
import os
import Adafruit_DHT
from datetime import datetime

# Define the update_data function
def update_data():

    # Check if the file exists
    file_path = 'example_plot.csv'
    file_exists = os.path.isfile(file_path)

    # If the file exists, delete it to reset all the data
    if file_exists:
        os.remove(file_path)

    # Create a new DataFrame with the required columns
    df = pd.DataFrame(columns=['Temp', 'Time', 'Humidity'])

    # Set up GPIO pin numbers for each DHT11 sensor
    sensor_pins = [4, 17, 27, 22]

    while True:
        temps = []
        hums = []
        for i, pin in enumerate(sensor_pins):
            humidity, temperature = Adafruit_DHT.read_retry(11, pin)
            if humidity is not None and temperature is not None:
                temps.append(temperature)
                hums.append(humidity)
                print('DHT11 Sensor {0}: Temp: {1:0.1f} C  Humidity: {2:0.1f} %'.format(i+1, temperature, humidity))
            else:
                print('Failed to read data from DHT11 Sensor {0}'.format(i+1))
        if len(temps) > 0 and len(hums) > 0:
            avg_temp = sum(temps) / len(temps)
            avg_hum = sum(hums) / len(hums)
            print('Average Temp: {0:0.1f} C  Average Humidity: {1:0.1f} %'.format(avg_temp, avg_hum))
            # Get the current time
            now = datetime.now()

            # Format the time as a string
            current_time = now.strftime("%H:%M:%S")

            # Package the data as a dictionary
            data = {'Temp': [avg_temp], 'Time': [current_time], 'Humidity':[avg_hum]}

            # Add the new data to the existing DataFrame
            new_df = pd.DataFrame(data)
            df = pd.concat([df, new_df], ignore_index=True)

            # Write the updated DataFrame to the CSV file
            df.to_csv(file_path, index=False)

        # Pause the script for 1 second
        time.sleep(1)


# Call the update_data function
update_data()
