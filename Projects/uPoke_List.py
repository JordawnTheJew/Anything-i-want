countries = input("Enter country: ").split(',') # split the input based on ,
result = []
for c in countries: # iterate over the input countries
    result.append(countries(c.strip().lower(), '')) # get value from the dict, empty string if key is not found

print(', '.join(result)) # join the result using ', ' 