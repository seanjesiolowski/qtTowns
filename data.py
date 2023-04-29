town_data = {'towns':
             [{'name': 'Croghan',
               'pop_2010': 3093,
               'total_area': 182.03,
               'total_land': 179.18,
               'total_wtr': 2.85},
                 {'name': 'Denmark',
                  'pop_2010': 2860,
                  'total_area': 51.05,
                  'total_land': 50.60,
                  'total_wtr': 0.45},
                 {'name': 'Diana',
                  'pop_2010': 1709,
                  'total_area': 140.83,
                  'total_land': 137.10,
                  'total_wtr': 3.73},
                 {'name': 'Greig',
                  'pop_2010': 1199,
                  'total_area': 94.36,
                  'total_land': 92.99,
                  'total_wtr': 1.37},
                 {'name': 'Harrisburg',
                  'pop_2010': 437,
                  'total_area': 39.91,
                  'total_land': 39.88,
                  'total_wtr': 0.03},
                 {'name': 'Lewis',
                  'pop_2010': 854,
                  'total_area': 65.1,
                  'total_land': 64.6,
                  'total_wtr': 0.5},
                 {'name': 'Leyden',
                  'pop_2010': 1785,
                  'total_area': 33.55,
                  'total_land': 33.33,
                  'total_wtr': 0.22},
                 {'name': 'Lowville',
                  'pop_2010': 4982,
                  'total_area': 38.13,
                  'total_land': 37.83,
                  'total_wtr': 0.29},
                 {'name': 'Lyonsdale',
                  'pop_2010': 1227,
                  'total_area': 70.10,
                  'total_land': 68.74,
                  'total_wtr': 1.36},
                 {'name': 'Martinsburg',
                  'pop_2010': 1433,
                  'total_area': 76.03,
                  'total_land': 75.68,
                  'total_wtr': 0.35},
                 {'name': 'Montague',
                  'pop_2010': 78,
                  'total_area': 65.31,
                  'total_land': 65.15,
                  'total_wtr': 0.16},
                 {'name': 'New Bremen',
                  'pop_2010': 2706,
                  'total_area': 55.79,
                  'total_land': 55.59,
                  'total_wtr': 0.20},
                 {'name': 'Osceola',
                  'pop_2010': 229,
                  'total_area': 87.10,
                  'total_land': 87.01,
                  'total_wtr': 0.09},
                 {'name': 'Pinckney',
                  'pop_2010': 329,
                  'total_area': 41.12,
                  'total_land': 40.97,
                  'total_wtr': 0.14},
                 {'name': 'Turin',
                  'pop_2010': 761,
                  'total_area': 31.38,
                  'total_land': 31.18,
                  'total_wtr': 0.20},
                 {'name': 'Watson',
                  'pop_2010': 1881,
                  'total_area': 115.70,
                  'total_land': 112.74,
                  'total_wtr': 2.96},
                 {'name': 'West Turin',
                  'pop_2010': 1524,
                  'total_area': 102.40,
                  'total_land': 102.05,
                  'total_wtr': 0.34}]}


def get_pop(town_name):
    for town in town_data['towns']:
        if town['name'] == town_name:
            return str(town['pop_2010'])


def get_area(town_name):
    for town in town_data['towns']:
        if town['name'] == town_name:
            return str(town['total_area'])


def get_land(town_name):
    for town in town_data['towns']:
        if town['name'] == town_name:
            return str(town['total_land'])


def get_wtr(town_name):
    for town in town_data['towns']:
        if town['name'] == town_name:
            return str(town['total_wtr'])


def get_dens(town_name):
    for town in town_data['towns']:
        if town['name'] == town_name:
            return str(format(town['pop_2010']/town['total_land'], '.2f'))
