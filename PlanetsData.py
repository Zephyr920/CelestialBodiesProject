import csv
import Planet as p

CONVERSION = 1e3

def load_data(filename):
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
            mass = float(row['mass'])
            xpos = float(row['xpos'])
            ypos = float(row['ypos'])
            zpos = float(row['zpos'])
            xvel = float(row['xvel'])
            yvel = float(row['yvel'])
            zvel = float(row['zvel'])
            return data_list, mass, xpos * CONVERSION, ypos * CONVERSION, zpos * CONVERSION, xvel, yvel, zvel