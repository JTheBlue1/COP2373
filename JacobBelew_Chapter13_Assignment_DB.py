##Write a program to create a database called population_(your initials).
##For ex: population_SM would be my database. Create a table named population with the
##following fields; 1. city, 2. year, 3. population. Choose 10 cities in Florida and
##insert data into the population table for the year 2023.
##Create a function to the simulate population growth for the next 20 years at
##a 2% growth rate for each year.Insert this data into the population table.
##Using matplotlib, create a function to show the population growth for a city.
##Let the user know the 10 cities as options and ask them to choose one and
##display the population growth for the city visually. Let the user
##continue to choose a city until they are done.

import sqlite3
from matplotlib import pyplot as plt

# Database name
db_name = 'pop.db'

# Cities
fl_cities = ['Miami', 'Tampa', 'Orlando', 'Jacksonville', 'Tallahassee', 'St. Petersburg', 'Fort Lauderdale', 'Bradenton', 'Sarasota', 'Gainesville']

# 2023 population data
init_pop = [4559224, 403364, 320742, 1713240, 202221, 263553, 184255, 57076, 57602, 145812]

# Utilize database
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Population table
c.execute('''
    CREATE TABLE IF NOT EXISTS population (
        city TEXT,
        year INTEGER,
        population INTEGER
    )
''')

# Add data into population table
for city, population in zip(fl_cities, init_pop):
    c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, 2023, population))

conn.commit()

# Simulate population growth
def pop_sim(years=20, growth_rate=0.02):
    for city in fl_cities:
        for year in range(2024, 2024 + years):

            # Get the last year's population
            c.execute('SELECT population FROM population WHERE city = ? AND year = ?', (city, year - 1))
            last_population = c.fetchone()[0]

            # Calculate the new population
            new_population = int(last_population * (1 + growth_rate))

            # Insert the new data into the table
            c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, new_population))

    conn.commit()

# Plot population growth
def plot_pop():

    print("Cities:", ", ".join(fl_cities))

    city = input("Select the following cities to display their projected population growth: ")

    c.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (city,))
    data = c.fetchall()

    if data:
        years, populations = zip(*data)
        plt.plot(years, populations, marker='o')
        plt.title(f'Population of {city}')
        plt.xlabel('Years')
        plt.ylabel('Population (thousands)')
        plt.grid(True)
        plt.show()
    else:
        print("Invalid City.")

#Close functions and database
pop_sim()
plot_pop()
conn.close()