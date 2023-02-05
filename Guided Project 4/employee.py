import numpy as np

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue',
         'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
call_numbers = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
avarage_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]

data = np.array([], dtype=int)


def append_names(names_list):
    global data
    for i in names_list:
        data = np.append(data, names.index(i))


def append_performance_measures(feature_list):
    global data
    data = np.append(data, feature_list)


append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(avarage_deal_sizes)
append_performance_measures(revenues)

print(data)
print(data.shape)


data = data.reshape(4, 11)
print(data)
print(data.shape)

# print first row
print(data[0])

# print spesific value
print(data[3, 7])


def calculate_employee_performance(employee_name):
    idx = names.index(employee_name)
    number_of_calls = data[1, idx]
    avarage_deal_size = data[2, idx]
    revenue = data[3, idx]

    score = (avarage_deal_size*revenue)/number_of_calls
    return score


print(calculate_employee_performance("Ellen"))
