import csv

def load_data(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = []
        for row in csv_reader:
            data_list.append(row)
        xpos = [row['xpos'] for row in data_list]
        ypos = [row['ypos'] for row in data_list]
        radius = [row['radius'] for row in data_list]
        return data_list, xpos, ypos, radius



#for n in range(len(data_list)):
#    value = data_list[1]['xpos']
#    print(value)