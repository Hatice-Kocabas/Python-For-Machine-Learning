file = open("employee_revenue.txt", "r")
data = file.read()

lines = data.splitlines()
# print(lines)
string = lines[0]
# print(string)

string = string.strip(" ")
# print(string),

string = string.lower()
# print(string)

string = string.capitalize()
# print(string)

split_string = string.split(" ")
# print(split_string)

name = split_string[0]


call_number = split_string[2]


for i in split_string:
    if '$' in i:
        avarage_deal_size = i.split('$')[0]


dollars_index = split_string.index('dollars')

revenue_index = dollars_index-1


revenue = split_string[revenue_index]


names = []
call_numbers = []
avarage_deal_sizes = []
revenues = []


def clean_extract(lines):

    for employee in lines:
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()

        split_employee = employee.split(" ")
        name = split_employee[0]
        call_number = split_employee[2]

        for i in split_employee:
            if '$' in i:
                avarage_deal_size = i
        avarage_deal_size = avarage_deal_size.split('$')[0]

        dollars_index = split_employee.index('dollars')
        revenue_index = dollars_index-1
        revenue = split_employee[revenue_index]
        avarage_deal_size = int(avarage_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        names.append(name)
        call_numbers.append(call_number)
        avarage_deal_sizes.append(avarage_deal_size)
        revenues.append(revenue)

    return names, call_numbers, avarage_deal_sizes, revenues


names, call_numbers, avarage_deal_sizes, revenues = clean_extract(lines)

print("name:", names)
print("number of calls :", call_numbers)
print("Avarage deal size:", avarage_deal_sizes)
print("revenue:", revenues)

# print(len(names))
IDs = list(range(0, len(names)))
print(IDs)

dictionary1 = dict(zip(IDs, names))
print(dictionary1)

dictionary2 = dict(zip(names, revenues))
print(dictionary2)

sorted_dictionary = sorted(dictionary2)[0:3]
print(sorted_dictionary)
