import csv

timing_data = []
with open('TestTimingData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

column_chart_data = [[""]]


