centries = int(input())

years = centries * 100
days = centries * 100 * 365.2422
days = int(days)
hours = days * 24
hours = int(hours)
minutes =  hours * 60

print(f'{centries:.0f} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes')
