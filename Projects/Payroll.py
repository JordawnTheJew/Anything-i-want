name = input("what is the employees name: " )
hourlywage = input('what is your hourly wage: ')
Hoursworked = input('How many hours did you work:' )

earnings = float(hourlywage) * float(Hoursworked)
"""
if Hoursworked > 40:
    hourlywage * 1.5
"""

print(name, "Worked", hourlywage, 'Hours' " and Earned $",earnings )