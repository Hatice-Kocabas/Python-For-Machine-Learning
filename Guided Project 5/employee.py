import pandas as pd
import numpy as np

last_year = pd.read_csv("employee_revenue_lastyear.csv")
print(last_year.head())

last_year["Year"] = 2022
print(last_year)


names = np.array(['Ben', 'Omer', 'Karen', 'Celine', 'Sue',
                  'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude'])
call_numbers = np.array([300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80])
avarage_deal_sizes = np.array([8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12])
revenues = np.array([2400, 60, 12000, 2275, 500,
                    770, 4000, 6000, 800, 1200, 500])


dictionary = {
    "name": names,
    "call_number": call_numbers,
    "avarage_deal_size": avarage_deal_sizes,
    "revenue": revenues
}

current_year = pd.DataFrame(dictionary)
print(current_year.head())
current_year["Year"] = 2023

current_year.columns = last_year.columns
all_data = pd.concat([last_year, current_year], axis=0)
print(all_data)

all_data.reset_index(drop=True, inplace=True)
print(all_data)


print(all_data.isna().any())

all_data.fillna(value=np.mean(all_data), inplace=True)

print(all_data)


print(all_data.describe())
