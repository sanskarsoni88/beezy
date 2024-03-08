import serial
import csv
from datetime import datetime
import os

# Serial port configuration
serial_port = '/dev/ttyAMA0'
baud_rate = 115200

# CSV file path
csv_file_path = os.path.expanduser('~/sensors_data.csv')

def save_to_csv(data):
    # Check if the CSV file exists, add header if it's being created
    file_exists = os.path.isfile(csv_file_path)
    
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "temp1", "hum1", "temp2", "hum2", "temp3", "hum3", "temp4", "hum4", "co2Value"])
        writer.writerow(data)

try:
    ser = serial.Serial(serial_port, baud_rate)
    print(f"Listening for data on {serial_port} at {baud_rate} baud rate...")
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            data = line.split(',')
            # Add current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data.insert(0, timestamp)
            print(f"Data received: {data}")
            save_to_csv(data)

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    if 'ser' in locals() or 'ser' in globals():
        ser.close
