#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# 4. Pass the data back to the main.py file, sto that you can print the data from main.py

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
#print(sheet_data)

print(data_manager.get_destination_data())
data_manager.update_destination_codes()