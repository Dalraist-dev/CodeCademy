# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
# test function by updating damages

def convert_damages(damage_list):
  converted_damages = []
  for damage in damage_list:
    if damage == 'Damages not recorded':
      converted_damages.append(damage)
    elif damage[-1] == "M":
      converted_damages.append(float(damage[:-1]) * 1000000)
    elif damage[-1] == "B":
      converted_damages.append(float(damage[:-1]) * 1000000000)
    else:
      converted_damages.append(damage + " Unexpected Format Alert")
  return converted_damages

converted_damages = convert_damages(damages)

print(converted_damages)
print('\n')

# 2 
# Organizing by Name
# create a dictionary of hurricanes with name as key

def hurri_name_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurri_names = {}

  for i in range(0, len(names)):

    hurri_names[names[i]] = {
                            'Name': names[i], 
                            'Month': months[i], 
                            'Year': years[i], 
                            'Max Sustained Wind': max_sustained_winds[i], 
                            'Areas Affected': areas_affected[i], 
                            'Damage': damages[i], 
                            'Deaths': deaths[i]
                            }
  return hurri_names

hurri_names = hurri_name_dict(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)

print(hurri_names)
print('\n')


# 3
# Organizing by Year
# create a new dictionary of hurricanes with year as key - Use Dictionary created in last task, Not original lists.

def hurri_year_dict(hurri_dict):
  unique_years = []
  hurri_years = {}

  for i in range(len(hurri_dict)):

    hurri_sub_dict = list(hurri_dict.values())[i]
    year_index = list(hurri_sub_dict).index('Year')
    year = list(hurri_sub_dict.values())[year_index]

    if year not in unique_years:
      unique_years.append(year)
      hurri_years[year] = [hurri_sub_dict]
    elif year in unique_years:
      hurri_years[year].append(hurri_sub_dict)
      
  return hurri_years

hurri_years = hurri_year_dict(hurri_names)

print(hurri_years)
print('\n')

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

def hurri_count_areas(hurri_dict):
  unique_areas = []
  hurri_areas_count = {}

  for i in range(len(hurri_dict)):

    hurri_sub_dict = list(hurri_dict.values())[i]
    areas_affected_index = list(hurri_sub_dict).index('Areas Affected')
    areas_affected = list(hurri_sub_dict.values())[areas_affected_index]

    for x in range(len(areas_affected)):

      area_affected = areas_affected[x]
      if area_affected not in unique_areas:
        unique_areas.append(area_affected)
        hurri_areas_count[area_affected] = 1
      elif area_affected in unique_areas:
        hurri_areas_count[area_affected] += 1
      
  hurri_areas_count = {area: count for area, count in sorted(hurri_areas_count.items(), key = lambda area: area[1], reverse=True)}
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# https://www.w3schools.com/python/ref_func_sorted.asp
# https://www.w3schools.com/python/python_lambda.asp 

  return hurri_areas_count

hurri_areas_count = hurri_count_areas(hurri_names)

print(hurri_areas_count)
print('\n')

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of times that hurricanes hit the area

def area_most_affected(hurri_dict):
  most_affected = ""
  times_affected = 0
  areas_list = list(hurri_dict.keys())

  for i in range(len(areas_list)):
    area_key = areas_list[i]
    if hurri_dict.get(area_key) > times_affected:
      most_affected = area_key
      times_affected = hurri_dict[area_key]

  print("The area most affected by hurricanes was " + most_affected + ". It was hit " + str(times_affected) + " times!")

area_most_affected(hurri_areas_count)
print('\n')


# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def most_hurri_deaths(hurri_dict):
  most_deadly = ""
  max_death_count = 0
  names_list = list(hurri_dict.keys())

  for i in range(len(names_list)):
    hurri_key = names_list[i]
    this_death_count = (hurri_dict.get(hurri_key)).get('Deaths')

    if this_death_count > max_death_count:
      most_deadly = hurri_key
      max_death_count = this_death_count

  print(most_deadly + " had the highest mortality of all! " + str(max_death_count) + " people died during the hurricane!")

most_hurri_deaths(hurri_names)
print('\n')

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}

def hurri_mortality_scale(hurri_dict):
  names_list = list(hurri_dict.keys())
  # mortality_keys = [5, 4, 3, 2, 1, 0]
  # hurri_mortalities = dict.fromkeys(mortality_keys)
  hurri_mortalities = {5: [], 4: [], 3: [], 2: [], 1: []}

  for i in range(len(names_list)):
    hurri_sub_dict = hurri_dict.get(names_list[i])
    this_death_count = (hurri_sub_dict).get('Deaths')

    if this_death_count > 10000:
      hurri_mortalities[5].append(hurri_sub_dict)
    elif this_death_count > 1000 and this_death_count <= 10000:
      hurri_mortalities[4].append(hurri_sub_dict)
    elif this_death_count > 500 and this_death_count <= 1000:
      hurri_mortalities[3].append(hurri_sub_dict)
    elif this_death_count > 100 and this_death_count <= 500:
      hurri_mortalities[2].append(hurri_sub_dict)
    elif this_death_count > 0 and this_death_count <= 100:
      hurri_mortalities[1].append(hurri_sub_dict)
    # else:
    #   hurri_mortalities[0].append(hurri_sub_dict)
    # The above was originally added due to the way the task was worded on CodeCademy. If   included later, add "0: []" to the initialization of hurri_mortalities above. No hurricanes were deathless.
  
  return hurri_mortalities

hurri_mortalities = hurri_mortality_scale(hurri_names)

print(hurri_mortalities)
print('\n')


# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def most_costly_hurri(hurri_dict):
  most_costly = ""
  max_cost = 0
  names_list = list(hurri_dict.keys())

  for i in range(len(names_list)):
    hurri_key = names_list[i]
    this_cost = (hurri_dict.get(hurri_key)).get('Damage')

    if this_cost == "Damages not recorded":
      continue
    else:
      if this_cost > max_cost:
        most_costly = hurri_key
        max_cost = this_cost

  print(most_costly + " was the most costly hurricane! With approximently $" + str(max_cost) + " in total damages!")

most_costly_hurri(hurri_names)
print('\n')

# 9
# Rating Hurricanes by Damage  
# categorize hurricanes in new dictionary with damage severity as key
# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}

def hurri_damage_scale(hurri_dict):
  names_list = list(hurri_dict.keys())
  hurri_damages = {5: [], 4: [], 3: [], 2: [], 1: [], 0: []}

  for i in range(len(names_list)):
    hurri_sub_dict = hurri_dict.get(names_list[i])
    this_cost = (hurri_sub_dict).get('Damage')

    if this_cost == "Damages not recorded":
      this_cost = 0

    if this_cost > 50000000000:
      hurri_damages[5].append(hurri_sub_dict)
    elif this_cost > 10000000000 and this_cost <= 50000000000:
      hurri_damages[4].append(hurri_sub_dict)
    elif this_cost > 1000000000 and this_cost <= 10000000000:
      hurri_damages[3].append(hurri_sub_dict)
    elif this_cost > 100000000 and this_cost <= 1000000000:
      hurri_damages[2].append(hurri_sub_dict)
    elif this_cost > 0 and this_cost <= 100000000:
      hurri_damages[1].append(hurri_sub_dict)
    else:
      hurri_damages[0].append(hurri_sub_dict)

  
  return hurri_damages

hurri_damages = hurri_damage_scale(hurri_names)

print(hurri_damages)
print('\n')
