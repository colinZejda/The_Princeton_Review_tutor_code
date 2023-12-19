def read_file(filename):
    try:
        dates, populations = [], []
        with open(filename, 'r') as file:
            next(file)  # Skip header line
            for line in file:
                date, population = line.strip().split(',')
                dates.append(date)
                populations.append(population)
        return dates, populations
    except IOError as e:
        print(f"Error reading file: {e}")
        return [], []

def slice_the_year(dates):
    return [date.split('/')[-1] for date in dates]

def convert_population_datatype(populations):
    return [int(population) for population in populations]

def display_lists(dates, populations):
    for date, population in zip(dates, populations):
        print(f"{date}: {population}")

def create_yearly_change(years, populations):
    changes = {}
    for i in range(len(years) - 1):
        changes[years[i]] = abs(populations[i + 1] - populations[i])
    return changes

def display_yearly_change(yearly_changes):
    for year, change in yearly_changes.items():
        print(f"{year}: {change}")

def find_highest_lowest_increase(yearly_changes):
    highest_increase = max(yearly_changes.values())
    lowest_increase = min(yearly_changes.values())
    highest_year = [year for year, change in yearly_changes.items() if change == highest_increase]
    lowest_year = [year for year, change in yearly_changes.items() if change == lowest_increase]
    return highest_year[0], highest_increase, lowest_year[0], lowest_increase

def calc_average_change(yearly_changes):
    total_change = sum(yearly_changes.values())
    average_change = total_change / len(yearly_changes)
    return average_change

def display_statistics(average_change, highest_year, highest_increase, lowest_year, lowest_increase):
    print(f"Average Change: {average_change}")
    print(f"Highest Population Year: {highest_year}, Increase: {highest_increase}")
    print(f"Lowest Population Year: {lowest_year}, Increase: {lowest_increase}")

def write_file(filename, average_change, highest_year, highest_increase, lowest_year, lowest_increase):
    with open(filename, 'w') as file:
        file.write(f"Average Change: {average_change}\n")
        file.write(f"Highest Population Year: {highest_year}, Increase: {highest_increase}\n")
        file.write(f"Lowest Population Year: {lowest_year}, Increase: {lowest_increase}\n")

if __name__ == "__main__":
    dates, populations = read_file("us_population.txt")
    years = slice_the_year(dates)
    populations = convert_population_datatype(populations)
    display_lists(years, populations)
    yearly_changes = create_yearly_change(years, populations)
    display_yearly_change(yearly_changes)
    highest_year, highest_increase, lowest_year, lowest_increase = find_highest_lowest_increase(yearly_changes)
    average_change = calc_average_change(yearly_changes)
    display_statistics(average_change, highest_year, highest_increase, lowest_year, lowest_increase)
    write_file("pop_stats_file.txt", average_change, highest_year, highest_increase, lowest_year, lowest_increase)
