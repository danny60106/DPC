# Initialize `fahrenheit` dictionary 
fahrenheit = {'d1':-30, 'd2':-20, 'd3':-10, 'd4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: float(5/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

# Initialize the `fahrenheit` dictionary 
fahrenheit = {'d1': -30,'d2': -20,'d3': -10,'d4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:float(5/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)