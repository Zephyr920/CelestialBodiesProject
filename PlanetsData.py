import csv

def load_data(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
        body = [row['Body'] for row in data_list]
        xpos = [row['xpos'] for row in data_list]
        ypos = [row['ypos'] for row in data_list]
        xvel = [row['xvel'] for row in data_list]
        yvel = [row['yvel'] for row in data_list]
        mass = [row['mass'] for row in data_list]
        radius = [row['radius'] for row in data_list]
        colour = [row['colour'] for row in data_list]
        return data_list, body, xpos, ypos, xvel, yvel, mass, radius, colour



#for n in range(len(data_list)):
#    value = data_list[1]['xpos']
#    print(value)